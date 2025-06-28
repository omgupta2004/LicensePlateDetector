# 🚘 Real-Time Indian License Plate Detection System
## 🎯 Features

- 📷 Live webcam-based detection
- 🇮🇳 Detects and validates Indian vehicle numbers
- 📝 Logs each plate with timestamp & snapshot
- 🧾 Exports logs to `CSV` and saves plate images
- 🖥️ Simple GUI using Tkinter

## 🛠️ Tech Stack

| Technology     | Role                  |
|----------------|------------------------|
| Python 3.12    | Core programming       |
| OpenCV         | Camera & image handling|
| pytesseract    | OCR engine             |
| Tkinter        | GUI application        |
| Regex          | Plate pattern matching |

## 🔧 Installation

### 1. 📦 Install Python dependencies:

```bash
pip install numpy==1.26.4
pip install pandas==2.2.2
pip install opencv-python
pip install pytesseract
