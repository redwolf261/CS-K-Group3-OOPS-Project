$exe = Join-Path $PSScriptRoot 'aes_tool.exe'
if (-not (Test-Path $exe)) {
    Write-Error "Executable not found: $exe"
    exit 1
}

# Use simple args parsing to avoid param block parsing issues in some shells
$mode = 'encrypt'
$file = 'test.txt'
$password = 'mypassword'
if ($args.Count -ge 1) { $mode = $args[0] }
if ($args.Count -ge 2) { $file = $args[1] }
if ($args.Count -ge 3) { $password = $args[2] }

# Map mode to menu choice
$choice = if ($mode -eq 'encrypt') { '1' } else { '2' }

$inputText = "$choice`n$file`n$password`n"

$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = $exe
$startInfo.WorkingDirectory = $PSScriptRoot
$startInfo.RedirectStandardInput = $true
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true
$startInfo.UseShellExecute = $false
$startInfo.CreateNoWindow = $true

$proc = New-Object System.Diagnostics.Process
$proc.StartInfo = $startInfo
$proc.Start() | Out-Null

# Write input
$proc.StandardInput.Write($inputText)
$proc.StandardInput.Close()

# Read output
$out = $proc.StandardOutput.ReadToEnd()
$err = $proc.StandardError.ReadToEnd()
$proc.WaitForExit()

Write-Host "Exit code: $($proc.ExitCode)"
if ($out) { Write-Host "--- STDOUT ---"; Write-Host $out }
if ($err) { Write-Host "--- STDERR ---"; Write-Host $err }

if (Test-Path (Join-Path $PSScriptRoot 'test.txt.enc')) {
    Write-Host "Encrypted file created: test.txt.enc"
}

exit $proc.ExitCode
