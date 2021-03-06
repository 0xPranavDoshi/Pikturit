; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Pikturit"
#define MyAppVersion "1.2.2"
#define MyAppPublisher "Pranav Doshi"
#define MyAppURL "https://github.com/Cybernetic77/Pikturit"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{32A8006E-B6D9-4A33-91DE-5D2587C83624}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\Pikturit
DefaultGroupName=Pikturit
LicenseFile=D:\prana\Programming\My Projects\Pikturit\LICENSE.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputBaseFilename=pikturit_setup
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "D:\prana\Programming\My Projects\Pikturit\dist\pikturit\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKCR; Subkey: "SystemFileAssociations\image\shell\Pikturit"; ValueType: string; ValueData: "Pikturit"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\image\shell\Pikturit\command"; ValueType: string; ValueData: """{app}\pikturit.exe"" ""%1""";
Root: HKCR; Subkey: "Directory\shell\Pikturit"; ValueType: string; ValueData: "Pikturit"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\shell\shell\Pikturit\command"; ValueType: string; ValueData: """{app}\pikturit.exe"" ""%1""";