import os
from PIL import Image
import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


def upWindowsh(hint):
    messBox = QMessageBox()
    messBox.setWindowTitle(u'提示')
    messBox.setText(hint)
    messBox.exec_()


def list_images_in_directory(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))
    return image_files


# 修改照片大小
def Change_image_Size(image_path):
    # 打开原图像
    original_image = Image.open(image_path)
    # 获取原始照片大小
    original_width, original_height = original_image.size
    
    # 计算调整后的尺寸
    width, height = original_width, original_height
    ratio = 1300 / width
    width = 1300
    height *= ratio
    if height > 850:
        ratio = 850 / height
        height = 850
        width *= ratio
    
    # 调整图像
    reduced_image = original_image.resize((int(width), int(height)))
    reduced_image.save((image_path))
    
    # 返回调整后的图像路径、调整后尺寸和原始尺寸
    return image_path, int(width), int(height), (original_width, original_height)


def convert_coordinates_to_original(x, y, w, h, original_size, resized_size):
    """
    将调整后图像上的坐标转换回原始图像坐标
    
    Args:
        x, y, w, h: 调整后图像上的坐标和尺寸
        original_size: 原始图像尺寸 (width, height)
        resized_size: 调整后图像尺寸 (width, height)
    
    Returns:
        原始图像上的坐标和尺寸
    """
    orig_w, orig_h = original_size
    resize_w, resize_h = resized_size
    
    # 计算缩放比例
    scale_x = orig_w / resize_w
    scale_y = orig_h / resize_h
    
    # 转换坐标
    orig_x = int(x * scale_x)
    orig_y = int(y * scale_y)
    orig_w = int(w * scale_x)
    orig_h = int(h * scale_y)
    
    return orig_x, orig_y, orig_w, orig_h


def list_label(label_path):
    with open(label_path, 'r') as file:
        content = file.read()
    root = ET.fromstring(content)

    objects = root.findall('object')

    list_labels = []
    list_box = []
    for obj in objects:
        name = obj.find('name').text
        # 修复坐标计算错误：应该直接使用xmax和ymax，而不是相加
        xmin = int(obj.find('bndbox/xmin').text)
        ymin = int(obj.find('bndbox/ymin').text)
        xmax = int(obj.find('bndbox/xmax').text)
        ymax = int(obj.find('bndbox/ymax').text)
        box = [xmin, ymin, xmax, ymax]
        list_labels.append(name)
        list_box.append(box)
    return list_labels,list_box


def get_labels(label_path):
    with open(label_path, 'r') as file:
        content = file.read()
    root = ET.fromstring(content)

    get_list_label = []

    for obj in root.findall('object'):
        item = {
            'name': obj.find('name').text,
            'pose': obj.find('pose').text,
            'truncated': int(obj.find('truncated').text),
            'difficult': int(obj.find('difficult').text),
            'bndbox': [int(obj.find('bndbox/xmin').text), int(obj.find('bndbox/ymin').text),
                       int(obj.find('bndbox/xmax').text), int(obj.find('bndbox/ymax').text)]
        }
        get_list_label.append(item)

    return get_list_label


