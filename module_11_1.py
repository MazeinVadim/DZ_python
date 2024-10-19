import os
from PIL import Image, ImageFilter, ImageEnhance

# Путь к папке с изображениями .webp
input_folder = 'webp'
# Путь к папке для сохранения изображений .png
output_folder = 'png'

# Создание папки для сохранения изображений .png, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Перебор всех файлов в папке input_folder
for filename in os.listdir(input_folder):
    if filename.endswith('.webp'):
        # Полный путь к файлу .webp
        webp_path = os.path.join(input_folder, filename)
        # Полный путь к файлу .png
        png_path = os.path.join(output_folder, filename.replace('.webp', '.png'))

        # Открытие изображения .webp
        with Image.open(webp_path) as img:
            # Применение фильтра тиснения
            img = img.filter(ImageFilter.EMBOSS)
            # Перевод в черно-белый формат
            img = img.convert('L')
            # Повышение резкости изображения
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(2.0)  # Коэффициент повышения резкости (2.0 - удвоение резкости)
            # Сохранение изображения в формате .png
            img.save(png_path, 'PNG')

        print(f"Конвертировано: {webp_path} -> {png_path}")

print("Все изображения успешно конвертированы и обработаны!")

