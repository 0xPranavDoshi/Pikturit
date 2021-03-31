import winreg

winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'SystemFileAssociations\image\shell\Pikturit\command')
winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'SystemFileAssociations\image\shell\Pikturit')