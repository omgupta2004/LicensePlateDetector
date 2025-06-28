import cv2
import pytesseract
import csv
from datetime import datetime
import os
import re
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def detect_license_plates():
    cap = cv2.VideoCapture(0)

    os.makedirs("static/snapshots", exist_ok=True)
    os.makedirs("database", exist_ok=True)

    log_path = "database/plate_log.csv"
    new_log = not os.path.exists(log_path)

    with open(log_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if new_log:
            writer.writerow(["Plate Number", "Timestamp", "Image Path"])

        frame_count = 0
        while frame_count < 150:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            text = text.upper().replace(" ", "").replace("-", "")
            matches = re.findall(r"[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}", text)

            for plate in matches:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"{plate}_{timestamp}.jpg"
                filepath = os.path.join("static/snapshots", filename)
                cv2.imwrite(filepath, frame)
                writer.writerow([plate, timestamp, filepath])
                print(f"[LOGGED] {plate} at {timestamp}")
                time.sleep(1)

            frame_count += 1
            time.sleep(0.1)

    cap.release()
