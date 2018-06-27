# -*- coding:utf-8 -*-
from PIL import Image
import subprocess

def cleanFile(filePath):
    image =Image.open(filePath)

    # subprocess.call(["tesseract", "-1", "chi_sim", filePath, "paixu"])
    # subprocess.call(["tesseract", "-1", "chi_sim", filePath, "paixu"], shell=True)
    subprocess.call("tesseract -1 chi_sim C:\Users\joker\Pictures\paixu.png paixu", shell=True)

    with open("paixu.txt", "r") as f:
        print(f.read().encode('utf-8'))

if __name__ == "__main__":
    cleanFile("paixu2.png")