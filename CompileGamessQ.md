# GamessQ 1.2.2 — macOS build notes

Source: ~/gamess2023R2claude/GamessQ/gamessq-1.2.2 (extracted from gamessq-1.2.2.tar)

## Status (2026-11-03)
- WORKING: GamessQ.app opens (after Info.plist fix + ad-hoc re-sign, with gamessqd started manually)
- `make` built src/gamessq and src/gamessqd as arm64 Mach-O, linked against Homebrew wxWidgets 3.3; configured with CXX=/usr/bin/clang++
- Running bare ./src/gamessq (outside the bundle) crashes or freezes — always use GamessQ.app
- `./src/gamessq -h` prints help then hangs on exit (CLI mode skips wx GUI init; likely wx 3.3 shutdown issue) — unresolved; command-line interface may be unreliable
- Next: put gamessqd in /usr/local/bin, configure spool dir + GAMESS path (dir containing `gms`), test a job

## From INSTALL
- Requires wxWidgets >= 3.0 (wx-config on PATH, or `./configure --with-wx-config=...`)
- `./configure && make`; on macOS `./bundle.sh` makes GamessQ.app
- Builds two programs: `gamessq` (GUI + CLI) and `gamessqd` (background daemon)

## Steps used (macOS, zsh)
1. `xcode-select --install`
2. `brew install wxwidgets` (got 3.3)
3. Fix typo: `sed -i.bak 's/headerpod_max/headerpad_max/' configure configure.ac` (user's sed is GNU, so `sed -i ''` fails; `-i.bak` works with both)
4. `./configure CC=/usr/bin/clang CXX=/usr/bin/clang++ --with-wx-config="$(brew --prefix)/bin/wx-config"`
5. `make`
6. `./bundle.sh`, then `codesign --force --deep -s - GamessQ.app`
7. `sudo cp src/gamessqd /usr/local/bin/` (gamessq looks for gamessqd next to GamessQ.app, then /usr/local/bin — NOT inside Contents/MacOS)
8. Move GamessQ.app to /Applications

## Fixes applied to source
- configure/configure.ac: `-headerpod_max_install_names` → `-headerpad_...` (backups *.bak)
- src/Info.plist (backup src/Info.plist.orig): replaced Xcode placeholders — EXECUTABLE_NAME=gamessq, PRODUCT_BUNDLE_IDENTIFIER=edu.iastate.msg.gamessq, PRODUCT_NAME=GamessQ, PACKAGE_TYPE=APPL, DEVELOPMENT_LANGUAGE=en, MACOSX_DEPLOYMENT_TARGET=11.0; set NSSupportsAutomaticTermination/SuddenTermination to false

## Problems hit
- `fatal error: 'iosfwd' file not found` on first make: fixes are `export SDKROOT="$(xcrun --show-sdk-path)"`, reinstall Command Line Tools, or use Apple's /usr/bin/clang++
- "executable is missing" when opening the app: unexpanded Info.plist placeholders (fixed above)

## Caveats
- config.guess/config.sub date from 2013; if configure can't guess the system, pass `--build=aarch64-apple-darwin`
- bundle.sh copies only libwx* dylibs into the app; other Homebrew deps stay linked to /opt/homebrew, so the app only runs on a Mac with Homebrew
- gamessqd does not daemonize itself; socket is /tmp/gamessq
- Runtime: GAMESS Path setting must point to the directory with the `gms` script; rungms must write .dat/.trj into the current directory (see GamessQ.html). A source-built GAMESS needs a `gms` script and rungms adjustments