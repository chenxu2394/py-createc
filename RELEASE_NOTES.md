# py-createc 0.1.0

This release stabilizes the package metadata and distribution process while
preserving the controller and file-reading behavior.

The release captures controller and file-reading code that was previously used
successfully with the live Createc Windows vendor system. Release preparation
corrects version and dependency metadata, adds a defined PEP 517 setuptools
build, and makes the offline regression tests portable to case-sensitive
filesystems. The Windows dependency is updated from `pywin32` build 228 to build
306 so the release does not retain a vulnerability fixed in build 301.

## Highlights

- Createc Windows COM wrapper with direct delegation to vendor operations.
- DAT and VERT file readers, plus spectroscopy-grid support.
- Offline oscilloscope and mapping modes alongside optional hardware-backed
  modes.
- STM utility behavior previously verified with the live Windows vendor system.
- Wheel and source-distribution packaging with explicit runtime dependencies.

## Verification

The release wheel and source distribution were tested on Windows 11 amd64 with
Python 3.9. The wheel installed with its Windows dependencies, the two bundled
offline parsing tests passed, the oscilloscope ran in random and CPU modes, and
the map displayed Createc data files offline. The applet scripts and sample data
were taken from the matching source distribution. Examples are included in the
source distribution but are not installed by the wheel.

## Verification limitation

The microscope controller and vendor software were no longer available during
release preparation, so live integration was not re-tested. Windows packaging,
clean installation, offline parsing, and offline example behavior were verified
without claiming a current hardware test.

This release is intended for GitHub and is not intended for publication to
PyPI.
