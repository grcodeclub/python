# pip install captcha
from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

def generate_captcha_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_captcha_image(captcha_text, img_width=300):
    image = ImageCaptcha(width=img_width)
    image_file = f"{captcha_text}.png"
    image.write(captcha_text, image_file)
    return image_file

text = generate_captcha_text()
image_file = generate_captcha_image(text)
Image.open(image_file).show()
