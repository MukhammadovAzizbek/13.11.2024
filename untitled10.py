# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H6pGec2vaOCYuY8-cZ1cb42zTAHfIQWu
"""

from google.colab.patches import cv2_imshow
import cv2

def Dunyo_shaharlar(belgi):
    if belgi == "Uzbekiston":
        rasm1 = cv2.imread("to.jpg")
        if rasm1 is not None:
            cv2_imshow(rasm1)
            return "Poytaxti Toshkent"
    elif belgi == "Russia":
        rasm2 = cv2.imread("m.jpg")
        if rasm2 is not None:
            cv2_imshow(rasm2)
        return "Poytaxt Moskva"
    elif belgi == "Germaniya":
        rasm3 = cv2.imread("be.jpg")
        if rasm3 is not None:
            cv2_imshow(rasm3)
        return "Poytaxti Berlin"
    elif belgi == "Fransiya":
        rasm4 = cv2.imread("p.jpg")
        if rasm4 is not None:
            cv2_imshow(rasm4)
        return "Parij"
    elif belgi == "Xitoy":
        rasm5 = cv2.imread("bej.jpg")
        if rasm5 is not None:
            cv2_imshow(rasm5)
        return "Beijing"
    elif belgi == "Yaponiya":
        rasm6 = cv2.imread("pek.jpg")
        if rasm6 is not None:
            cv2_imshow(rasm6)
        return "Tokio"
    elif belgi == "Italiya":
        rasm7 = cv2.imread("rim.jpg")
        if rasm7 is not None:
            cv2_imshow(rasm7)
        return "Rim"
    elif belgi == "BBA":
        rasm8 = cv2.imread("abu.jpg")
        if rasm8 is not None:
            cv2_imshow(rasm8)
        return "Abu-Dabi"
    else:
        return "Borini qidiring iltimos"

belgi = input("Shaharni kiriting")
natija = Dunyo_shaharlar(belgi)
print(natija)