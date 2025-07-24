Set WshShell = CreateObject("WScript.Shell")
Set oShellLink = WshShell.CreateShortcut("TNC Gestão - Sistema.lnk")
oShellLink.TargetPath = WshShell.CurrentDirectory & "\executar_sistema.bat"
oShellLink.WorkingDirectory = WshShell.CurrentDirectory
oShellLink.IconLocation = WshShell.CurrentDirectory & "\logo_rnc.ico"
oShellLink.Description = "TNC Gestão - Sistema de Gestão de TNCs"
oShellLink.Save

WScript.Echo "✅ Atalho criado: TNC Gestão - Sistema.lnk"
