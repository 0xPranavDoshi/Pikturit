import winreg

winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\Pikturit\command')
winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'Directory\shell\Pikturit')