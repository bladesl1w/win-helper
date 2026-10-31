# для тестов

import os
from pathlib import Path

program_files = os.environ.get("ProgramFiles", r"C:\Program Files")

base_obs_path = Path(program_files) / "obs-studio" / "bin" / "64bit"

exe_path = str(base_obs_path / "obs64.exe")
work_path = str(base_obs_path)

print(f"Путь к EXE: {exe_path}")
print(f"Рабочая директория: {work_path}")

