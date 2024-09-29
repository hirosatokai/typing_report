import cv2
import pytesseract # 画像から文字を読み取るモジュール
import pyautogui
import numpy as np  # NumPyをインポート
import time

# Tesseractのパスが必要な場合は指定する
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen(region):
    # region = (left, top, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def recognize_text(image):
    # 画像から文字を認識
    text = pytesseract.image_to_string(image, lang='eng')
    return text.strip()

def type_text(text):
    # 認識した文字を自動でタイピング
    pyautogui.write(text, interval=0.001)

def main():
    # キャプチャする画面の領域を指定
    region = (930, 470, 460, 40)  # 左上のx, y, 幅, 高さ
    while True:
        print("!!!!!!!!!!!!!!!!!!")
        # 画面をキャプチャして文字を認識
        image = capture_screen(region)
        recognized_text = recognize_text(image)
        
        if recognized_text:
            print(f"Recognized: {recognized_text}")
            type_text(recognized_text)
        
        # 処理の間隔を調整
        time.sleep(0.7)

if __name__ == "__main__":
    main()