import os
import subprocess
import ctypes
import pygetwindow as gw
import webbrowser

program_files = os.environ.get("ProgramFiles")
program_files86 = os.environ.get("ProgramFiles(x86)")

# Открыть телеграм
def tg():
  try:
    subprocess.Popen("start tg://", shell=True)
  except Exception:
   if ( ctypes.windll.user32.MessageBoxW(0,
            "Приложение не найдено!\n\nНажмите «Да», если хотите скачать приложение",
            "Ошибка!", 4 + 16) == 6):
     webbrowser.open("https://desktop.telegram.org/")
   
   
# Открывает VsCode
def code():
  code_windows = gw.getWindowsWithTitle('Visual Studio Code')
  if code_windows:
    code_win = code_windows[0]
    if code_win.isMinimized:
      code_win.restore()
    code_win.activate()
  else:
    user_profile = os.environ.get("USERPROFILE")
    path_to_exe = os.path.join(user_profile, r"AppData\Local\Programs\Microsoft VS Code\Code.exe")
    try:
      subprocess.Popen([path_to_exe]) # subprocess.Popen("code", shell=True) 
    except Exception:
      ctypes.windll.user32.MessageBoxW(0, "Приложение не найдено!\n\nВозможно у тебя не скачан Visual Studio Code.", "Ошибка!", 0 + 16)


# Открыть Windhawk
def windhawk():
  windhawk_windows = gw.getWindowsWithTitle('Windhawk')
  if windhawk_windows:
    windhawk_win = windhawk_windows[0]
    if windhawk_win.isMinimized:
      windhawk_win.restore()
    windhawk_win.activate()
  else:
    path_to_exe = f'{program_files}\\Windhawk\\windhawk.exe'
    dir_path = f'{program_files}\\Windhawk'
    try:
      subprocess.Popen(path_to_exe, cwd=dir_path)
    except FileNotFoundError:
      if ( ctypes.windll.user32.MessageBoxW(0,
              "Приложение не найдено!\n\nНажмите «Да», если хотите скачать приложение",
              "Внимание!", 4 + 16) == 6):
        webbrowser.open("https://windhawk.net/") 


# Открыть дискорд
def discord():
  ds_window = gw.getWindowsWithTitle('Discord')
  if ds_window:
    ds_win = ds_window[0]
    if ds_win.isMinimized:
      ds_win.restore()
    ds_win.activate()
  else:
    user_profile = os.environ.get("USERPROFILE")
    exe_path = os.path.join(user_profile, r"AppData\Local\Discord\Discord.exe")
    try:
      subprocess.Popen(exe_path, cwd=os.path.dirname(user_profile))
    except FileNotFoundError:
      if (ctypes.windll.user32.MessageBoxW(0,
              "Приложение Discord не найдено!\n\nНажмите «Да», если хотите скачать приложение.",
              "Внимание!", 4 + 16) == 6 ):
        webbrowser.open('https://discord.com/download')
        

# Открыть CapCut
def capcut():
  cc_window = gw.getWindowsWithTitle('capcut')
  if cc_window:
    cc_win = cc_window[0]
    if cc_win.isMinimized:
      cc_win.restore()
    cc_win.activate()
  else:
    user_profile = os.environ.get("USERPROFILE")
    path_to_exe = os.path.join(user_profile, r"AppData\Local\CapCut\Apps\CapCut.exe")
    try:
      subprocess.Popen(path_to_exe, cwd=os.path.dirname(path_to_exe))
    except FileNotFoundError:
      if ( ctypes.windll.user32.MessageBoxW(0,
              'Приложение CapCut не найдено!\n\nНажмите «Да», если хотите скачать приложение.',
              'Внимание!', 4 + 16) == 6 ):
        webbrowser.open('https://apps.microsoft.com/detail/xp9kn75rrb9nhs?hl=ru-RU&gl=RU')

# Открыть OBS
def obs():
  obs_window = gw.getWindowsWithTitle('OBS')
  if obs_window:
    obs_win = obs_window[0]
    if obs_win.isMinimized:
      obs_win.restore()
    obs_win.activate()
  else:
    try:
      exe_path = f'{program_files}\\obs-studio\\bin\\64bit\\obs64.exe'
      work_path = f'{program_files}\\obs-studio\\bin\\64bit'
      subprocess.Popen(exe_path, cwd=work_path)
    except FileNotFoundError:
      if ( ctypes.windll.user32.MessageBoxW(0, 
              'Приложение не найдено!\n\nНажмите «Да», если хотите скачать OBS Studio.',
              'Внимание!', 4 + 16 ) == 6 ):
        webbrowser.open('https://obsproject.com/')


# Открыть Happ
def happ():
  happ_window = gw.getWindowsWithTitle("Happ")
  if happ_window:
    happ_win = happ_window[0]
    if happ_win.isMinimized:
      happ_win.restore()
    happ_win.activate()
  else:
    exe_path = f'{program_files}\\FlyFrogLLC\\Happ\\Happ.exe'
    work_path = f'{program_files}\\FlyFrogLLC\\Happ'
    try:
      subprocess.Popen(exe_path, cwd=work_path)
    except FileNotFoundError:
      if ( ctypes.windll.user32.MessageBoxW(0,
                "Приложение не найдено!\n\nНажмите «Да», если хотите скачать Happ",
                "Внимание!", 4 + 16) == 6):
          webbrowser.open("https://github.com/Happ-proxy/happ-desktop/releases")