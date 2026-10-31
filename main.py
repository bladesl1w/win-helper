import tkinter as tk
from func import (open_browser, tg, code, cmd, powershell,
                  calc, discord, taskmgr, obs, capcut,
                  explorer, regedit, appdata, windhawk, settings, random_lett, random_letters)


root = tk.Tk()
# root.title(random_lett(random_letters))
root.title("by bladesl1w")
root.config(bg="lightblue")
root.geometry("387x485")
root.resizable(False, False)
root.attributes("-topmost", True)


def unpin():
  root.attributes("-topmost", False)

def pin():
  root.attributes("-topmost", True)

def close_window():
  import getpass
  import ctypes
  import sys
  import os
  import psutil
  root.attributes("-topmost", False)
  if ctypes.windll.user32.MessageBoxW(0, "Введенные данные могут не сохраниться!\nСохраните все файлы перед продолжением.\n\nВсе равно закрыть программы?", "Внимание!", 4 + 48) == 6:
      root.attributes("-topmost", True) 
      user, pid = getpass.getuser(), os.getpid()
      current_exe_name = os.path.basename(sys.executable)
      skip = ["explorer.exe", "taskhostw.exe", 
              "svchost.exe", "sihost.exe", 
              "winws.exe", "everything.exe", 
              "windhawk.exe", "MpDefenderCoreService.exe",
              current_exe_name].lower()
      
      
      for p in psutil.process_iter(['pid', 'name', 'username']):
          try:
            if p.info['username'] and user in p.info['username']:
              if p.info['pid'] != pid and p.info['name'] not in skip:
                p.terminate()
                root.attributes("-topmost", True)
          except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def close_all_window():
  import ctypes
  LK_WIN = 0x5B
  B_R = 0x44
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 0, 0)
  ctypes.windll.user32.keybd_event(B_R, 0, 0, 0) 
  ctypes.windll.user32.keybd_event(B_R, 0, 2, 0)
  ctypes.windll.user32.keybd_event(LK_WIN, 0, 2, 0)
  
def close_program():
  
  import time
  import ctypes
  import win32process
  import psutil
  import os
  import pygetwindow as gw
  
  root.withdraw()
  root.update()
  time.sleep(0.2)
  
  try:
    all_windows = gw.getAllWindows()
    active_window = None
    
    for win in all_windows:
      if win and win.visible and getattr(win, 'title', ''):
        try:
          _, pid = win32process.GetWindowThreadProcessId(win._hWnd)
          proc = psutil.Process(pid)
          p_name = str(proc.name()).lower()
          if p_name.lower() in ["helper.exe", "python.exe", "explorer.exe", "code.exe"]:
            continue
          # нашли окно 
          active_window = win
          break
        except:
          continue
        
    if not active_window:
      ctypes.windll.user32.MessageBoxW(0, "Программа не найдена.", "Внимание!", 0 + 48)
      root.deiconify()
      return
    
    hwnd = active_window._hWnd
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
        
    proc = psutil.Process(pid)
    process_name = proc.name()
    # Окно обнаружено
    proc.kill()
  except Exception as e:
    print(f"error {e}")
    ctypes.windll.user32.MessageBoxW(0, "Не удалось закрыть окно", "Внимание!", 0 + 48)
    
  root.deiconify()  

# Закрывает окно
def close():
  root.destroy()
  
# Свернуть программу
def resize_program():
  root.iconify()


# Сверуть окно
def resize_program2():
    import time, ctypes, win32process, psutil
    import pygetwindow as gw
    from ctypes import wintypes

    root.withdraw()
    root.update()
    time.sleep(0.2)

    def cloaked(hwnd):
      v = wintypes.DWORD()
      ctypes.windll.dwmapi.DwmGetWindowAttribute(hwnd, 14, ctypes.byref(v), 4)
      return v.value != 0

    skip = {"helper.exe", "textinputhost.exe"}
    target = None

    for win in gw.getAllWindows():
      try:
        if not win.title or not win.visible or win.isMinimized:
          continue
        if win.width < 100 or win.height < 100 or cloaked(win._hWnd):
          continue
        pid = win32process.GetWindowThreadProcessId(win._hWnd)[1]
        name = psutil.Process(pid).name().lower()
        if name in skip:
          continue
        target = win
        break
      except Exception:
       continue

    if target:
      target.minimize()
    else:
      ctypes.windll.user32.MessageBoxW(0, "Программа не найдена.", "Внимание!", 0x30)

    root.deiconify()
  

# 1 ряд
# Открыть браузер
btn_brow = tk.Button(root, text="Открыть браузер", command=open_browser, width=15, height=2, bg="lightgreen", fg="black")
btn_brow.grid(row=0, column=0, padx=5, pady=5)

# Открыть тг
btn_tg = tk.Button(root, text="Открыть Telegram",command=tg, width=15, height=2, bg="lightgreen", fg="black")
btn_tg.grid(row=0, column=1, padx=5, pady=5)

# Открыть дискорд
btn_ds = tk.Button(root, text="Discord", command=discord, width=15, height=2, bg="lightgreen", fg="black")
btn_ds.grid(row=0, column=2, padx=5, pady=5)


# 2 ряд
# Диспетчер задач
btn_task = tk.Button(root, text="Диспетчер задач", command=taskmgr, width=15, height=2)
btn_task.grid(row=1, column=0, padx=5, pady=5)

# Открыть калькулятор
btn_calc = tk.Button(root, text="Калькулятор", command=calc, width=15, height=2)
btn_calc.grid(row=1, column=1, padx=5, pady=5)

# Открыть проводник
btn_exp = tk.Button(root, text="Проводник", command=explorer, width=15, height=2)
btn_exp.grid(row=1, column=2, padx=5, pady=5)


# 3 ряд
# RegEdit
btn_regedit = tk.Button(root, text="Редактор реестра", command=regedit, width=15, height=2)
btn_regedit.grid(row=2, column=0, padx=5, pady=(0, 7))

# Открыть cmd
btn_cmd = tk.Button(root, text="Открыть cmd", command=cmd, width=15, height=2)
btn_cmd.grid(row=2, column=1, padx=5, pady=(0, 7))

# Открыть PowerShell
btn_ps1 = tk.Button(root, text="Открыть PowerShsell", command=powershell, width=15, height=2)
btn_ps1.grid(row=2, column=2, padx=5, pady=(0, 7))


# 4 ряд
# Редактор кода
btn_code = tk.Button(root, text="Редактор кода", command=code, width=15, height=2)
btn_code.grid(row=3, column=0, padx=5, pady=(0, 24))

# AppData
btn_appdata = tk.Button(root, text="AppData", command=appdata, width=15, height=2)
btn_appdata.grid(row=3, column=1, padx=5, pady=(0, 24))

# Настройки
btn_windhawk= tk.Button(root, text="Параметры", command=settings, width=15, height=2)
btn_windhawk.grid(row=3, column=2, padx=5, pady=(0, 24))


# 5 ряд
# Открыть OBS
btn_obs = tk.Button(root, text="OBS", command=obs, width=15, height=2, bg="green", fg="black")
btn_obs.grid(row=4, column=0, padx=5, pady=(0, 7))  

# Открыть CapCut
btn_cc = tk.Button(root, text="CapCut", command=capcut, width=15, height=2, bg="green", fg="black")
btn_cc.grid(row=4, column=1, padx=5, pady=(0, 7))

# Windhawk
btn_windhawk= tk.Button(root, text="WindHawk", command=windhawk, width=15, height=2, bg="green", fg="black")
btn_windhawk.grid(row=4, column=2, padx=5, pady=(0, 7))
# btn_cc = tk.Button(root, text="   ", width=15, height=2)#, bg="green", fg="black")
# btn_cc.grid(row=4, column=2, padx=5, pady=(0, 7))


# Сворачивает свсе окна (win + d)
btn_close_win2 = tk.Button(root, text="Свернуть\nвсе окна", command=close_all_window, width=15, height=2, font=("Arial", 9),  bg="plum", fg="black")
btn_close_win2.grid(row=5, column=0, padx=7, pady=(40, 0))

# pass
btn_close_pass = tk.Button(root, text="   ", width=15, height=2)#, bg="plum", fg="black")
btn_close_pass.grid(row=5, column=1, padx=7, pady=(40, 0))

# Сворачивает текущее окно
btn_close__rhythm = tk.Button(root, text="Свернуть\nоткрытое окно", command=resize_program2, width=15, height=2, font=("Arial", 9), bg="plum", fg="black")
btn_close__rhythm.grid(row=5, column=2, padx=7, pady=(40, 0))


""" Управление окном """
# Закрыть все открыте окна
btn_close_win = tk.Button(root, text="Закрыть все\nокна", command=close_window, width=15, height=3, font=("Arial", 9), bg="tan", fg="black")
btn_close_win.grid(row=7, column=0, padx=5, pady=5)

# Закрыть программу
btn_close = tk.Button(root, text="Закрыть программу", command=close, width=15, height=3, bg="black", fg="white")
btn_close.grid(row=7, column=1, padx=5, pady=5)

# Закрывает процесс
btn_taskkill = tk.Button(root, text="Завершить\nпроцесс", command=close_program, width=15, height=3, bg="tan", fg="black")
btn_taskkill.grid(row=7, column=2, padx=5, pady=5)

# Сворачивает прогу
btn_resize = tk.Button(root, text="Свернуть\nпрограмму", command=resize_program, width=15, height=3, bg="black", fg="white")
btn_resize.grid(row=8, column=1, padx=5, pady=5)

# Открепляет окно
btn_unpin = tk.Button(root, text="Открепить", command=unpin, width=15, height=3, bg="cadetblue", fg="black")
btn_unpin.grid(row=8, column=0, padx=5, pady=5)

# Закрепляет окно
btn_unpin = tk.Button(root, text="Поверх\nдругих окон", command=pin, width=15, height=3, bg="cadetblue", fg="black")
btn_unpin.grid(row=8, column=2, padx=5, pady=5)

if __name__ == "__main__":
  root.mainloop()
  
  



