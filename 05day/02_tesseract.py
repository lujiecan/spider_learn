import pytesseract
from PIL import Image


def main():
    image = Image.open("tesseract.png")
    print("正在识别tesseract.png, 请稍后...")
    text = pytesseract.image_to_string(image, lang="chi_sim")
    print("结果如下：")
    print("="*50)
    print(text)
    print("="*50)


if __name__ == "__main__":
    main()

