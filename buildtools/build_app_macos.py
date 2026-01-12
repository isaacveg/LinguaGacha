import os

import PyInstaller.__main__

cmd = [
    "./app.py",
    "--icon=./resource/icon.icns",
    "--clean",
    "--windowed",
    "--noconfirm",
    "--name=LinguaGacha",
    "--distpath=./dist",
]

if os.path.exists("./requirements.txt"):
    with open("./requirements.txt", "r", encoding="utf-8") as reader:
        for line in reader:
            if "#" not in line:
                cmd.append("--hidden-import=" + line.strip())

    PyInstaller.__main__.run(cmd)
