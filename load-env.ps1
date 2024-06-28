Get-Content key.env | ForEach-Object {
  $name, $value = $_.split('=')
  Set-Content env:\$name $value
}