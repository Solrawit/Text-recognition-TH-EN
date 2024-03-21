import os

# ตั้งค่า TESSDATA_PREFIX
os.environ['TESSDATA_PREFIX'] = 'C:\\Program Files\\Tesseract-OCR\\tessdata'

# ต่อมาเรียกใช้โมดูล pytesseract และทำ OCR ตามปกติ
import pytesseract
from PIL import Image

# ฟังก์ชันอ่านข้อความจากภาพ
def read_text_from_image(image_path):
    try:
        # อ่านข้อมูลจากภาพโดยใช้ Tesseract OCR
        text = pytesseract.image_to_string(Image.open(image_path), lang='tha')
        return text
    except Exception as e:
        print("Error:", e)
        return None

# ทดสอบการใช้งาน
if __name__ == "__main__":
    image_path = "C:/xampp/htdocs/Python - text-recognition/test.jpg"  # แทนที่ด้วยที่อยู่ของภาพที่ต้องการจะทำ OCR
    text = read_text_from_image(image_path)
    if text:
        print("Text from image:")
        print(text)
    else:
        print("Unable to read text from image.")
