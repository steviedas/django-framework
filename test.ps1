if ($env:VIRTUAL_ENV) {
    Write-Host "Virtual environment is active: $($env:VIRTUAL_ENV)"
} else {
    Write-Host "No virtual environment is active."
}
