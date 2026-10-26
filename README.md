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
$dir = (Resolve-Path .\area-code-lookup).Path
$sub = 'Environment'
$key = [Microsoft.Win32.Registry]::CurrentUser.OpenSubKey($sub, $true)
try {
    $raw  = [string]$key.GetValue('Path', '', [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames)
    $kind = if ($key.GetValueNames() -contains 'Path') { $key.GetValueKind('Path') } else { 'ExpandString' }
    $have = @($raw -split ';' | Where-Object { $_ } | ForEach-Object { [Environment]::ExpandEnvironmentVariables($_.Trim().Trim('"')).TrimEnd('\','/') })
    if ($have -notcontains $dir.TrimEnd('\','/')) {
        $new = (@($raw.TrimEnd(';'), $dir) | Where-Object { $_ }) -join ';'
        $key.SetValue('Path', $new, $kind)
    }
} finally {
    if ($key) { $key.Close() }
}
```

Open a new terminal, then run:

```powershell
areacode 415
```

> Avoid `setx` for editing `PATH` on Windows — it silently truncates the
> value at 1024 characters, which will corrupt the rest of your PATH if it's
> already long. Writing the registry value directly has no such limit.

> The Windows snippet reads only your **User** `PATH`, exactly as stored, adds
> the folder at the end if it isn't already there (ignoring case, quotes, a
> trailing `\` and `%VARIABLE%` forms), and writes nothing otherwise, so it is
> safe to run twice. Existing entries, their order, any `%VARIABLE%` text and
> the value's registry type are left as they were, and it needs no
> administrator rights. Don't build the new value from `$env:PATH`: that is the
> combined machine + user + session `PATH`, and saving it as the User value
> copies every machine entry into it. The `GetEnvironmentVariable` /
> `SetEnvironmentVariable` pair isn't safe for this either: it expands
> `%VARIABLE%` entries on read and saves the result as plain text. The change
> applies to programs started afterwards, so open a new terminal; the current
> one and anything already running keep the old `PATH`. The snippet doesn't
> notify Windows of the change, so a program started from the Start menu or
> Explorer may need you to sign out and back in first.

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
