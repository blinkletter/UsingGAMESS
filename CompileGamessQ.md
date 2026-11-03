# GamessQ 1.2.2 — macOS build notes

Source: ~/gamess2023R2claude/GamessQ/gamessq-1.2.2 (extracted from gamessq-1.2.2.tar)

## From INSTALL
- Requires wxWidgets >= 3.0 (wx-config on PATH, or `./configure --with-wx-config=...`)
- `./configure && make`; on macOS `./bundle.sh` makes GamessQ.app
- Builds two programs: `gamessq` (GUI + CLI) and `gamessqd` (background daemon)

## Plan (macOS, zsh)
1. `xcode-select --install`
2. `brew install wxwidgets`; check `wx-config --version`
3. Fix typo in configure: `sed -i '' 's/headerpod_max/headerpad_max/' configure configure.ac`
4. `./configure --with-wx-config="$(brew --prefix)/bin/wx-config"`
5. `make`
6. `./bundle.sh`, then `codesign --force --deep -s - GamessQ.app` (install_name_tool breaks signatures on Apple Silicon)
7. Move GamessQ.app to /Applications

## Findings / caveats
- configure.ac line `WX_LIBS+=" -headerpod_max_install_names"` is a typo for -headerpad_max_install_names
- config.guess/config.sub date from 2013; if configure can't guess the system, pass `--build=aarch64-apple-darwin` or replace them with current copies
- bundle.sh copies only libwx* dylibs into the app; other Homebrew deps (libpng, jpeg, tiff, pcre2) stay linked to /opt/homebrew, so the app only runs on a Mac with Homebrew
- Code targets wx 3.0; Homebrew ships 3.2+, so expect possible deprecation warnings or errors
- Runtime: GAMESS Path setting must point to the directory with the `gms` script; rungms must write .dat/.trj into the current directory (see GamessQ.html)