from PIL import Image, ImageEnhance, ImageFilter
import os
path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    
    img = Image.open(f"{path}/{filename}")
    
    # Convert the image to 'RGB' mode if it's in 'RGBA' mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    edit = img.filter(ImageFilter.SHARPEN)
    
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')