"""
Update windows wallpaper.

- ask the user for a wallpaper
- use the library ctypes to change the wallpaper
"""
import ctypes
import subprocess
import platform

def set_wallpaper():
    # Ask the user for the wallpaper file path
    wallpaper_path = input("Enter the file path for the wallpaper: ")

    # Set the wallpaper using ctypes on Windows, or PowerShell on other platforms
    if platform.system() == "Windows":
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0)
    else:
        ps_command = 'Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "Wallpaper" -Value "{}"'.format(wallpaper_path)
        subprocess.run(["powershell", "-Command", ps_command], capture_output=True)

def main():
    set_wallpaper()

if __name__ == "__main__":
    main()
