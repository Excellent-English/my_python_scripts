import cv2
import pytesseract

# Wczytaj obraz
image = cv2.imread('unnamed.jpg')

# Skalowanie obrazu
height, width = image.shape[:2]
scale_factor = 500 / height
resized_image = cv2.resize(image, (int(width * scale_factor), 500))

# Konwersja na skalę szarości i usuwanie szumów
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Progowanie
_, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

# Prostowanie obrazu
coords = cv2.findNonZero(thresh)
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle

(h, w) = thresh.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(thresh, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# Rozpoznawanie tekstu
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(rotated, lang='pol')

print(text)