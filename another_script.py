from PIL import Image
import numpy as np


def replace_color(image_path, target_color, replacement_color, tolerance=40):
    # Откройте изображение
    image = Image.open(image_path)
    image = image.convert('RGBA')

    # Преобразуйте изображение в массив
    data = np.array(image)

    # Определите целевой цвет и замену
    target_color = np.array(target_color)
    replacement_color = np.array(replacement_color)

    # Найдите пиксели, которые находятся в пределах допустимого диапазона
    mask = np.all(np.abs(data[:, :, :3] - target_color) <= tolerance, axis=-1)

    # Замените цвет
    data[mask] = replacement_color

    # Создайте новое изображение
    new_image = Image.fromarray(data)

    # Сохраните и покажите результат
    result_path = 'result.png'
    new_image.save(result_path)
    new_image.show()

    return result_path

# Пример использования
image_path = 'image1.png'
target_color = [86, 211, 247, 255]  # Цвет, который нужно заменить (синий в RGBA)
replacement_color = [0, 255, 0, 255]  # Новый цвет (зеленый в RGBA)

replace_color(image_path, target_color, replacement_color)
