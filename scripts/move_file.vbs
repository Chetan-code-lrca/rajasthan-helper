Dim fso, shell, folder, file
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

' Change to the target directory
shell.CurrentDirectory = "C:\Users\cheta\rajasthan-helper"

' Create .github directory if it doesn't exist
If Not fso.FolderExists(".github") Then
    fso.CreateFolder ".github"
    WScript.Echo "✓ Created .github directory"
Else
    WScript.Echo "✓ .github directory already exists"
End If

' Move the file
If fso.FileExists("copilot-instructions.md") Then
    fso.MoveFile "copilot-instructions.md", ".github\copilot-instructions.md"
    WScript.Echo "✓ File moved successfully"
Else
    WScript.Echo "✗ Source file not found"
End If

' Verify the file is in the correct location
If fso.FileExists(".github\copilot-instructions.md") Then
    Set file = fso.GetFile(".github\copilot-instructions.md")
    WScript.Echo "✓ File successfully located at: C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md"
    WScript.Echo "  File size: " & file.Size & " bytes"
Else
    WScript.Echo "✗ File not found at destination"
End If
