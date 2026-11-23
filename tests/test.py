import tkinter as tk
from tkinter import messagebox
import webbrowser


def link_box():
  root = tk.Tk()
  root.title("Внимание!")
  root.geometry("280x110")
  root.resizable(False, False)
  root.attributes("-topmost", True)
  tk.Label(root, text="Приложение не найдено!", pady=10).pack()
  link = tk.Label(
      root, text="Скачать OBS Studio", fg="blue", cursor="hand2"
  )
  link.pack()
  link.bind(
      "<Button-1>",
      lambda e: (webbrowser.open("https://obsproject.com"), root.destroy()),
  )
  tk.Button(root, text="ОК", width=10, command=root.destroy).pack(pady=10)
  root.mainloop()
