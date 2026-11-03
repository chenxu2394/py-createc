# Releasing py-createc

This maintainer guide assumes Windows 11, Python 3.9, a full repository
checkout, and PowerShell opened at the repository root. Release `0.1.0` is a
GitHub release and is not intended for PyPI.

## 1. Prepare the release commit

Confirm that `createc.__version__`, `CHANGELOG.md`, and the proposed tag agree.
Set the changelog date, commit the release preparation, and start only from a
clean worktree:

```powershell
git status --short
git log -1 --oneline
```

## 2. Build the artifacts once

Use a unique temporary workspace so old files cannot contaminate the build or
source extraction:

```powershell
$Repository = (Resolve-Path ".").Path
$Version = "0.1.0"
$Run = [guid]::NewGuid().ToString("N")
$Work = Join-Path $env:TEMP "py-createc-release-$Run"
$Dist = Join-Path $Work "dist"
$ExtractRoot = Join-Path $Work "extracted"
$BuildVenv = Join-Path $Work ".venv-build"
$BuildPython = Join-Path $BuildVenv "Scripts\python.exe"

New-Item -ItemType Directory -Path $Work | Out-Null
New-Item -ItemType Directory -Path $Dist | Out-Null
New-Item -ItemType Directory -Path $ExtractRoot | Out-Null

py -3.9 -m venv $BuildVenv
& $BuildPython -m pip install --upgrade pip
& $BuildPython -m pip install "build==1.2.2.post1" "twine==5.1.1"
& $BuildPython -m build $Repository --outdir $Dist

$Wheel = Join-Path $Dist "createc-$Version-py3-none-any.whl"
$Sdist = Join-Path $Dist "createc-$Version.tar.gz"

& $BuildPython -m twine check $Wheel $Sdist
Get-FileHash -Algorithm SHA256 $Wheel
Get-FileHash -Algorithm SHA256 $Sdist
```

Do not rebuild after testing. The files in `$Wheel` and `$Sdist` are the files
to attach to the GitHub Release.

## 3. Test the exact artifacts

Create a clean environment, install the wheel, and check the Windows import:

```powershell
$TestVenv = Join-Path $Work ".venv-test"
$TestPython = Join-Path $TestVenv "Scripts\python.exe"

py -3.9 -m venv $TestVenv
& $TestPython -m pip install --upgrade pip
& $TestPython -m pip install $Wheel
& $TestPython -m pip check
& $TestPython -c "import createc, win32com.client; print(createc.__version__)"
```

Extract the source archive into the empty extraction directory and run its
tests:

```powershell
tar -xf $Sdist -C $ExtractRoot
$Source = Join-Path $ExtractRoot "createc-$Version"
$Examples = Join-Path $Source "examples"

& $TestPython -m pip install pytest
& $TestPython -m pytest -q (Join-Path $Source "tests")
```

Install the optional dependencies and run the examples one at a time, stopping
each with Ctrl+C:

```powershell
& $TestPython -m pip install "${Wheel}[example_maps,osc,utility]"
& $TestPython (Join-Path $Examples "osc\oscilloscope.py")
& $TestPython (Join-Path $Examples "osc\oscilloscope.py") --cpu
& $TestPython (Join-Path $Examples "map\map.py")
```

Use a file from `$Examples\sample_data` in the map. The STM utility and
hardware-backed modes require the running vendor software. Their live behavior
was verified with the vendor system; exercise them again when that system is
available.

Record the Windows version, Python version, architecture, checksums, and test
results. Do not describe an unavailable hardware retest as completed.

## 4. Tag and create the GitHub Release

After all checks pass, tag the exact commit used for the build and push the tag:

```powershell
git tag -a "v$Version" -m "Release $Version"
git push origin "v$Version"
```

Create a draft release and attach the same tested artifacts:

```powershell
gh release create "v$Version" $Wheel $Sdist `
    --draft `
    --verify-tag `
    --notes-file RELEASE_NOTES.md
```

Review the commit, tag, notes, artifacts, and checksums before publishing. Never
move a published tag; use a new patch version for a correction.
