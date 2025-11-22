import cv2
import os
import numpy as np

N=50 #progrowanie wielkosci konturu

FOLDER = "bird_miniatures/"

def count_birds(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # poprawa kontrastu 
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)

    # rozmycie
    blur = cv2.medianBlur(gray, 5)

    # automatyczne progowanie Otsu
    _, thresh = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # operacje morfologiczne w celu oczyszczenia obrazu
    kernel = np.ones((3,3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    #kontury
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    birds = [c for c in contours if cv2.contourArea(c) > N]

    return len(birds), img, thresh



results = []

for filename in os.listdir(FOLDER):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(FOLDER, filename)
        count, img, thr = count_birds(path)
        results.append((filename, count))
        print(f"{filename}: {count} birds")

# zapis wynikow
with open("bird_counts.txt", "w") as f:
    for name, count in results:
        f.write(f"{name}: {count}\n")
