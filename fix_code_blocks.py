#!/usr/bin/env python3
"""
fix_code_blocks.py
Find code blocks with no language in every .md file in a folder (and its
subfolders) and turn them into plain-text blocks.

  ```{code-block}              ->   ```{code-block} text
  ---                               :label: butane-scan-inp
  name: butane-SCAN.inp             :filename: butane-SCAN.inp
  caption: butane-SCAN.inp
  ---                               <code unchanged>
  <code>

  ```  (plain fence, no language)  ->  ```text

Option mapping:  caption -> :filename:  (when it looks like a file name)
                 name    -> :label:     (cleaned to letters, digits, dashes)
                 others  -> kept as :option: value
References to a renamed label ([](#old), {ref}`old`, {numref}`old`) in the
same folder are updated too. Code blocks nested inside other code blocks
(e.g. a ````markdown example) are left alone.

Usage:
    python fix_code_blocks.py UsingGAMESS            # dry run: report only
    python fix_code_blocks.py UsingGAMESS --apply    # make the changes
The list of changed files is printed and saved to changed_files.txt.
"""
import argparse
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
DIRECTIVE = re.compile(r"^\{(code-block|code|sourcecode)\}\s*$")
COLON_OPT = re.compile(r"^\s*:([\w-]+):\s*(.*)$")


def clean_label(name):
    return re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-").lower()


def looks_like_filename(text):
    return bool(text) and " " not in text and "." in text


def convert_options(opts):
    """opts: list of (key, value). Returns new list and (old_label, new_label) or None."""
    out, rename = [], None
    keys = {k for k, _ in opts}
    for key, value in opts:
        if key == "name":
            new = clean_label(value)
            out.append(("label", new))
            if new != value:
                rename = (value, new)
        elif key == "caption" and looks_like_filename(value) and "filename" not in keys:
            out.append(("filename", value))
        else:
            out.append((key, value))
    order = {"label": 0, "filename": 1}          # label and filename first
    out.sort(key=lambda kv: order.get(kv[0], 2))
    return out, rename


def read_options(lines, i):
    """Read directive options starting at lines[i]. Returns (opts, next_index)."""
    opts = []
    if i < len(lines) and lines[i].strip() == "---":          # YAML block
        j = i + 1
        while j < len(lines) and lines[j].strip() != "---":
            if ":" in lines[j]:
                k, v = lines[j].split(":", 1)
                opts.append((k.strip(), v.strip().strip("'\"")))
            j += 1
        return opts, j + 1
    while i < len(lines) and COLON_OPT.match(lines[i]):        # :key: value lines
        m = COLON_OPT.match(lines[i])
        opts.append((m.group(1), m.group(2).strip()))
        i += 1
    if i < len(lines) and lines[i].strip() == "" and opts:
        i += 1
    return opts, i


def process(text):
    lines = text.split("\n")
    out, i = [], 0
    changes, renames = 0, []
    while i < len(lines):
        m = FENCE.match(lines[i])
        if not m:
            out.append(lines[i]); i += 1
            continue
        indent, fence, info = m.group("indent"), m.group("fence"), m.group("info").strip()
        start = i
        # find the matching closing fence (same char, at least as long, nothing after)
        close = re.compile(r"^[ \t]*" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$")
        j = i + 1
        while j < len(lines) and not close.match(lines[j]):
            j += 1
        body_end = j                                            # index of closing fence

        if info == "":                                          # plain fence, no language
            out.append(f"{indent}{fence}text")
            out.extend(lines[start + 1:body_end + 1])
            changes += 1
        elif DIRECTIVE.match(info):                             # {code-block} with no language
            opts, k = read_options(lines, start + 1)
            opts, rename = convert_options(opts)
            if rename:
                renames.append(rename)
            out.append(f"{indent}{fence}{info} text")
            out.extend(f"{indent}:{key}: {val}".rstrip() for key, val in opts)
            if opts:
                out.append("")
            out.extend(lines[k:body_end + 1])
            changes += 1
        else:                                                   # already has a language
            out.extend(lines[start:body_end + 1])
        i = body_end + 1
    return "\n".join(out), changes, renames


def update_refs(text, renames):
    count = 0
    for old, new in renames:
        for pat, rep in [(r"\(#" + re.escape(old) + r"\)", f"(#{new})"),
                         (r"(\{(?:ref|numref)\}`(?:[^`<]*<)?)" + re.escape(old) + r"(>?`)",
                          r"\g<1>" + new + r"\g<2>")]:
            text, n = re.subn(pat, rep, text)
            count += n
    return text, count


def main():
    ap = argparse.ArgumentParser(description="Give language-less code blocks the 'text' language.")
    ap.add_argument("folder", help="folder to process, e.g. UsingGAMESS")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    args = ap.parse_args()

    folder = Path(args.folder).resolve()
    if not folder.is_dir():
        sys.exit(f"Not a folder: {folder}")
    files = sorted(p for p in folder.rglob("*.md")
                   if not {"_build", ".git", ".ipynb_checkpoints"} & set(p.parts))

    results, all_renames = {}, []
    for path in files:
        original = path.read_text(encoding="utf-8")
        new, n, renames = process(original)
        all_renames += renames
        results[path] = [original, new, n, 0]

    for path, r in results.items():                            # fix references to renamed labels
        r[1], r[3] = update_refs(r[1], all_renames)

    changed = [(p, r) for p, r in results.items() if r[1] != r[0]]
    print("DRY RUN (nothing written)\n" if not args.apply else "APPLYING\n")
    for old, new in all_renames:
        print(f"  label renamed: {old} -> {new}")
    if all_renames:
        print()

    lines = []
    for path, (_, new, n, refs) in changed:
        rel = path.relative_to(folder.parent)
        detail = f"{n} code block{'s' if n != 1 else ''}" + (f", {refs} reference(s)" if refs else "")
        lines.append(f"{rel}  ({detail})")
        if args.apply:
            path.write_text(new, encoding="utf-8")

    print("Files changed:" if args.apply else "Files that would change:")
    print("\n".join(f"  {l}" for l in lines) if lines else "  (none)")
    print(f"\n{len(changed)} of {len(files)} .md file(s), "
          f"{sum(r[2] for _, r in changed)} code block(s).")

    if args.apply and lines:
        Path("changed_files.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("List saved to changed_files.txt")
    elif not args.apply:
        print("Run again with --apply to make the changes.")


if __name__ == "__main__":
    main()
