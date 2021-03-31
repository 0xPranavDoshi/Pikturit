import winreg
import os

appdata_dir = r'C:\Users\prana\AppData\Local\Programs\Python\Python39\python.exe" "D:\prana\Programming\My Projects\Pikturit Project\Pikturit\pikturit.py'
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                 R'SystemFileAssociations\image\shell\Pikturit')
winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                 R'SystemFileAssociations\image\shell\Pikturit\command')

key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,
                     R'SystemFileAssociations\image\shell\Pikturit', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Pikturit')
key.Close()


command_key = winreg.OpenKey(
    winreg.HKEY_CLASSES_ROOT, R'SystemFileAssociations\image\shell\Pikturit\command', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, Rf'"{appdata_dir}" "%1"')
command_key.Close()

# python.exe C:\Users\prana\AppData\Local\Programs\Python\Python39\python.exe
