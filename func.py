import os
import time
import subprocess
import pyperclip
import psutil
import ctypes
import random
import pygetwindow as gw

program_files = os.environ.get("ProgramFiles")
program_files86 = os.environ.get("ProgramFiles(x86)")

random_letters = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", 
    "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", 
    "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", 
    "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", 
    "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", 
    "N", "M"
]

def random_lett(letters_list, length=15):
  return "".join([random.choice(letters_list) for _ in range(length)])


def get_windows_pid(hwnd):
  from ctypes import wintypes
  pid = wintypes.DWORD()
  ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
  return pid.value

import winreg
import re
def default_browser():
  try:
      with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice") as k:
          prog = winreg.QueryValueEx(k, "ProgId")[0]
      with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, prog + r"\shell\open\command") as k:
          cmd = winreg.QueryValueEx(k, None)[0]
      return re.match(r'"?([^"]+?\.exe)', cmd).group(1)
  except Exception:
      return None
      
def default_browser():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice") as k:
            prog = winreg.QueryValueEx(k, "ProgId")[0]
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, prog + r"\shell\open\command") as k:
            cmd = winreg.QueryValueEx(k, None)[0]
        return re.match(r'"?([^"]+?\.exe)', cmd).group(1)
    except Exception:
        return None

def open_browser():
  import webbrowser
  browsers = {"chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe", "browser.exe", "vivaldi.exe"}
  for win in gw.getAllWindows():
    try:
      if win.title and psutil.Process(get_windows_pid(win._hWnd)).name().lower() in browsers:
        if win.isMinimized:
          win.restore()
        try:
          win.activate()
        except Exception:
          pass
        return
    except Exception:
      continue

  exe = default_browser()
  if not exe:
    webbrowser.open("about:blank")
    return
  args = [exe] if "firefox" in exe.lower() else [exe, "--restore-last-session"]
  subprocess.Popen(args, cwd=os.path.dirname(exe))
  
# Открыть телеграм
def tg():
  try:
    subprocess.Popen("start tg://", shell=True)
  except Exception:
    ctypes.windll.user32.MessageBoxW(0, "Приложение не найдено!\nСкачайте с магазина приложений", "Ошибка!", 0 + 16)
    
def windhawk():
  windhawk_windows = gw.getWindowsWithTitle('Windhawk')
  if windhawk_windows:
    windhawk_win = windhawk_windows[0]
    if windhawk_win.isMinimized:
      windhawk_win.restore()
    windhawk_win.activate()
  else:
    path_to_exe = r"C:\Program Files\Windhawk\windhawk.exe"
    dir_path = r"C:\Program Files\Windhawk"
    try:
      subprocess.Popen(path_to_exe, cwd=dir_path)
    except FileNotFoundError:
      ctypes.windll.user32.MessageBoxW(0, "Приложение не найдено!\nСначало скачайте приложение с GitHub.", "Ошибка!", 0 + 48) 

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



# открыть cmd
def cmd():
  cmd_window = gw.getWindowsWithTitle('cmd')
  if cmd_window:
    cmd_win = cmd_window[0]
    if cmd_win.isMinimized:
      cmd_win.restore()
    cmd_win.activate()
  else:
    user_profile = os.path.expanduser("~")
    subprocess.Popen("start cmd", shell=True, cwd=user_profile)
    
# Открыть PowerShell
def powershell():
  ps1_window = gw.getWindowsWithTitle('powershell')
  if ps1_window:
    ps1_win = ps1_window[0]
    if ps1_win.isMinimized:
      ps1_win.restore()
    ps1_win.activate()
  else:
    subprocess.Popen(['powershell', '-NoExit'],
        cwd=r'C:\Windows\System32',
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    
# Открыть калькулятор
def calc():
  calc_window = gw.getWindowsWithTitle('calc')
  if calc_window:
    calc_win = calc_window[0]
    if calc_win.isMinimized:
      calc_win.restore()
    calc_win.activate()
  else:
    subprocess.Popen("calc", shell=True)
  
def explorer():
  exp_window = gw.getWindowsWithTitle('explorer')
  if exp_window:
    exp_win = exp_window[0]
    if exp_win.isMinimized:
      exp_win.restore()
    exp_win.activate()
  else:
    subprocess.Popen("explorer", shell=True)

def settings():
  subprocess.Popen("start ms-settings:", shell=True)

def regedit2():
  regedit_window = gw.getWindowsWithTitle("regedit") or gw.getWindowsWithTitle("Редактор реестра")
  if regedit_window:
    regedit_win = regedit_window[0]
    if regedit_win.isMinimized:
      regedit_win.restore()
      time.sleep(0.1)
    regedit_win.activate()
  else:
    import pyautogui
    LK_WIN = 0x5B
    B_R = 0x52
    pyperclip.copy("regedit")
    ctypes.windll.user32.keybd_event(LK_WIN, 0, 0, 0)  # 0 скан-код не нужен, 0 нажать, 0 без спец данных
    ctypes.windll.user32.keybd_event(B_R, 0, 0, 0) # 0 скан-код не нужен, 0 нажать, 0 без спец данных
    ctypes.windll.user32.keybd_event(B_R, 0, 2 , 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
    ctypes.windll.user32.keybd_event(LK_WIN, 0, 2, 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    
def regedit():
  regedit_window = gw.getWindowsWithTitle("regedit") or gw.getWindowsWithTitle("Редактор реестра")
  if regedit_window:
    regedit_win = regedit_window[0]
    if regedit_win.isMinimized:
      regedit_win.restore()
    regedit_win.activate()
  else:
    ps_command = f'Start-Process "regedit"'
    subprocess.Popen(["powershell", "-Command", ps_command])

def help_LK_WIN_and_codes(): # help down
  import pyautogui # код клавиши Win
  import pyperclip # код клавиши R
  LK_WIN = 0x5B # код клавиши Win
  VK_R = 0x52 # код клавиши R
  pyperclip.copy("%appdata%")
  # 0 - скан-код клавиши на аппаратном уровне клавиатуры не нужен, 0 (нажать), 2 (зажать) 0 (без спец. данных(драйвера, спец. программы и др.)).
  # логика win + r
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 0, 0)  # 0 скан-код не нужен, 0 нажать, 0 без спец данных
  ctypes.windll.user32.keybd_event(VK_R, 0, 0, 0) # 0 скан-код не нужен, 0 нажать, 0 без спец данных
  # отпускаем R | после Win, во избежания залипания
  ctypes.windll.user32.keybd_event(VK_R, 0, 2 , 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
  # отпускаем Win
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 2, 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
  time.sleep(0.3)
  pyautogui.hotkey("ctrl", "v")
  pyautogui.press("enter")

def appdata():
  import keyboard
  import pyperclip
  LK_WIN = 0x5B 
  VK_R = 0x52 
  pyperclip.copy("%appdata%")
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 0, 0)  # 0 скан-код не нужен, 0 нажать, 0 без спец данных
  ctypes.windll.user32.keybd_event(VK_R, 0, 0, 0) # 0 скан-код не нужен, 0 нажать, 0 без спец данных
  ctypes.windll.user32.keybd_event(VK_R, 0, 2 , 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 2, 0) # 0 скан-код не нужен, 2 зажать, 0 без спец данных
  time.sleep(0.3)
  keyboard.send("ctrl+v")
  keyboard.send("enter")
  
# Открывает Диспетчер задач
def taskmgr():
  task_window = gw.getWindowsWithTitle('taskmgr')
  if task_window:
    task_win = task_window[0]
    if task_win.isMinimized:
      task_win.restore()
    task_win.activate()
  else:
    subprocess.Popen("taskmgr", shell=True)
    
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
      ctypes.windll.user32.MessageBoxW(0, "Приложение Discord не найдено!\nУстанови приложение с оффициального сайта!", "Внимание!", 0 + 16) == 1


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
      ctypes.windll.user32.MessageBoxW(0, "Приложение CapCut не найдено!\nУстановите из магазина приложений.", "Внимание!", 0 + 48) == 1

    
def obs():
  obs_window = gw.getWindowsWithTitle('OBS')
  if obs_window:
    obs_win = obs_window[0]
    if obs_win.isMinimized:
      obs_win.restore()
    obs_win.activate()
  else:
    exe_path = f"{program_files}\\obs-studio\\bin\\64bit\\obs64.exe"
    work_path = f"{program_files}\\obs-studio\\bin\\64bit"
    try:
      subprocess.Popen(exe_path, cwd=work_path)
    except FileNotFoundError:
      ctypes.windll.user32.MessageBoxW(0, "Приложение не найдено!", "Внимание!", 0 + 48)
      