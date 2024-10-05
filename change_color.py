import cv2
import numpy as np


def replace_color(image_path, target_color, replacement_color, tolerance=40):
    image = cv2.imread(image_path)
    target_color = np.array(target_color, dtype=np.uint8)
    replacement_color = np.array(replacement_color, dtype=np.uint8)
    lower_bound = target_color - tolerance
    upper_bound = target_color + tolerance
    mask = cv2.inRange(image, lower_bound, upper_bound)
    image[mask != 0] = replacement_color
    result_path = 'result.png'
    cv2.imwrite(result_path, image)
    cv2.imshow('Result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return result_path


image_path = 'image1.png'
target_color = [86, 211, 247]  # Цвет, который нужно заменить (синий в BGR)
replacement_color = [255, 255, 255]  # Новый цвет (зеленый в BGR)

replace_color(image_path, target_color, replacement_color)
