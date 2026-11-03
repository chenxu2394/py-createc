# Changelog

This project follows semantic versioning from the published PyPI releases.
Entries describe released behavior and release-preparation corrections.

## [0.1.0] - 2026-11-03

Release 0.1.0 stabilizes package metadata and distribution while preserving the
controller and scientific behavior.

### Added since 0.0.3

- `GRID_SPEC` support for Createc spectroscopy-grid files.
- Direct delegation from `CreatecWin32` to the underlying vendor COM object.
- Offline data examples, documentation, and regression fixtures.

### Release preparation

- Corrected the package version from the unsupported internal value `1.0` to
  `0.1.0`, following the published `0.0.3` release.
- Declared PyYAML as a direct dependency and updated the Windows-only
  `pywin32` dependency from build 228 to build 306. Build 306 retains Python
  3.7–3.9 wheels and includes the security fix published in build 301.
- Added optional dependency groups for the map, oscilloscope, and STM utility
  examples.
- Included the example applications and sample data in the source distribution.
- Added a minimal PEP 517 setuptools build configuration.
- Corrected `.VERT` fixture capitalization so the offline tests also pass on
  case-sensitive filesystems.
- Documented the distinction between cross-platform offline functionality and
  Windows/vendor controller functionality.

### Verification scope

- The controller implementation was used successfully with the live Createc
  vendor system on Windows.
- Live controller integration was not re-tested for this release because the
  microscope controller and vendor software were unavailable.
- Windows packaging, clean installation, offline parsing, and offline examples
  are the current release gates.
