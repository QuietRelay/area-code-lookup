# areacode

A tiny, dependency-free command-line tool for looking up the general geographic
region tied to a North American (NANP) telephone area code — the US, Canada,
and shared NANP territories. Useful for a quick gut-check on unfamiliar
incoming calls.

## Requirements

- Python 3 (no third-party packages needed)

## Usage

One-off lookup:

```bash
python area_code.py 415
python area_code.py 415 212 90210        # multiple lookups at once
python area_code.py "+1 (313) 555-0100"  # full numbers work too
```

Interactive mode (no arguments):

```bash
python area_code.py
```

## Installing it as a plain `areacode` command

Clone the repo, then put this folder on your `PATH`.

**macOS / Linux:**

```bash
git clone https://github.com/QuietRelay/area-code-lookup.git
chmod +x area-code-lookup/areacode
echo 'export PATH="$PATH:'"$(pwd)"'/area-code-lookup"' >> ~/.zshrc   # or ~/.bashrc
```

Open a new terminal, then run:

```bash
areacode 415
```

**Windows (PowerShell or cmd):**

```powershell
git clone https://github.com/QuietRelay/area-code-lookup.git
[Environment]::SetEnvironmentVariable('PATH', "$env:PATH;$(Resolve-Path .\area-code-lookup)", 'User')
```

Open a new terminal, then run:

```powershell
areacode 415
```

> Avoid `setx` for editing `PATH` on Windows — it silently truncates the
> value at 1024 characters, which will corrupt the rest of your PATH if it's
> already long. `[Environment]::SetEnvironmentVariable` has no such limit.

## Notes

- Area code data reflects publicly available NANPA (North American Numbering
  Plan Administration) assignments and may drift out of date as new overlay
  codes are introduced.
- Cell phone numbers are portable, so an area code only tells you where a
  number was originally registered — not necessarily where the caller
  actually is.
- Unknown area codes print a "not found" message rather than failing.

## License

No license file yet — all rights reserved by default. Add a `LICENSE` file
if you want to permit reuse.
