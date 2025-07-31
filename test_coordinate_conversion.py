#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
坐标转换测试脚本
用于验证坐标转换功能是否正确
"""

from util.QtFunc import convert_coordinates_to_original

def test_coordinate_conversion():
    """测试坐标转换功能"""
    
    # 测试用例1：原始图像 1920x1080，调整后 1300x731
    print("测试用例1：原始图像 1920x1080，调整后 1300x731")
    original_size = (1920, 1080)
    resized_size = (1300, 731)
    
    # 在调整后图像上的坐标
    x, y, w, h = 100, 50, 200, 150
    
    # 转换到原始图像坐标
    orig_x, orig_y, orig_w, orig_h = convert_coordinates_to_original(
        x, y, w, h, original_size, resized_size
    )
    
    print(f"调整后坐标: x={x}, y={y}, w={w}, h={h}")
    print(f"原始坐标: x={orig_x}, y={orig_y}, w={orig_w}, h={orig_h}")
    
    # 验证转换是否正确
    scale_x = original_size[0] / resized_size[0]
    scale_y = original_size[1] / resized_size[1]
    
    expected_x = int(x * scale_x)
    expected_y = int(y * scale_y)
    expected_w = int(w * scale_x)
    expected_h = int(h * scale_y)
    
    print(f"期望坐标: x={expected_x}, y={expected_y}, w={expected_w}, h={expected_h}")
    print(f"转换正确: {orig_x == expected_x and orig_y == expected_y and orig_w == expected_w and orig_h == expected_h}")
    print()
    
    # 测试用例2：原始图像 800x600，调整后 800x600（无需调整）
    print("测试用例2：原始图像 800x600，调整后 800x600（无需调整）")
    original_size = (800, 600)
    resized_size = (800, 600)
    
    x, y, w, h = 100, 50, 200, 150
    
    orig_x, orig_y, orig_w, orig_h = convert_coordinates_to_original(
        x, y, w, h, original_size, resized_size
    )
    
    print(f"调整后坐标: x={x}, y={y}, w={w}, h={h}")
    print(f"原始坐标: x={orig_x}, y={orig_y}, w={orig_w}, h={orig_h}")
    print(f"转换正确: {orig_x == x and orig_y == y and orig_w == w and orig_h == h}")
    print()
    
    # 测试用例3：原始图像 4000x3000，调整后 1300x975
    print("测试用例3：原始图像 4000x3000，调整后 1300x975")
    original_size = (4000, 3000)
    resized_size = (1300, 975)
    
    x, y, w, h = 650, 487, 100, 75
    
    orig_x, orig_y, orig_w, orig_h = convert_coordinates_to_original(
        x, y, w, h, original_size, resized_size
    )
    
    print(f"调整后坐标: x={x}, y={y}, w={w}, h={h}")
    print(f"原始坐标: x={orig_x}, y={orig_y}, w={orig_w}, h={orig_h}")
    
    # 验证转换是否正确
    scale_x = original_size[0] / resized_size[0]
    scale_y = original_size[1] / resized_size[1]
    
    expected_x = int(x * scale_x)
    expected_y = int(y * scale_y)
    expected_w = int(w * scale_x)
    expected_h = int(h * scale_y)
    
    print(f"期望坐标: x={expected_x}, y={expected_y}, w={expected_w}, h={expected_h}")
    print(f"转换正确: {orig_x == expected_x and orig_y == expected_y and orig_w == expected_w and orig_h == expected_h}")

def test_custom_coordinates(original_size, resized_size, x, y, w, h):
    """
    自定义坐标转换测试
    
    Args:
        original_size: 原始图像尺寸 (width, height)
        resized_size: 调整后图像尺寸 (width, height)
        x, y, w, h: 调整后图像上的坐标和尺寸
    """
    print(f"自定义测试：原始图像 {original_size[0]}x{original_size[1]}，调整后 {resized_size[0]}x{resized_size[1]}")
    print(f"调整后坐标: x={x}, y={y}, w={w}, h={h}")
    
    # 转换到原始图像坐标
    orig_x, orig_y, orig_w, orig_h = convert_coordinates_to_original(
        x, y, w, h, original_size, resized_size
    )
    
    print(f"原始坐标: x={orig_x}, y={orig_y}, w={orig_w}, h={orig_h}")
    
    # 计算缩放比例
    scale_x = original_size[0] / resized_size[0]
    scale_y = original_size[1] / resized_size[1]
    print(f"缩放比例: 宽度 {scale_x:.2f}倍，高度 {scale_y:.2f}倍")
    
    # 验证转换是否正确
    expected_x = int(x * scale_x)
    expected_y = int(y * scale_y)
    expected_w = int(w * scale_x)
    expected_h = int(h * scale_y)
    
    print(f"期望坐标: x={expected_x}, y={expected_y}, w={expected_w}, h={expected_h}")
    print(f"转换正确: {orig_x == expected_x and orig_y == expected_y and orig_w == expected_w and orig_h == expected_h}")
    print()

if __name__ == "__main__":
    print("=" * 60)
    print("坐标转换功能测试")
    print("=" * 60)
    test_coordinate_conversion()
    
    print("=" * 60)
    print("自定义测试示例")
    print("=" * 60)
    
    # 示例：测试您自己的坐标
    # 您可以修改这些参数来测试不同的场景
    test_custom_coordinates(
        original_size=(1920, 1080),  # 原始图像尺寸
        resized_size=(1300, 731),    # 调整后图像尺寸
        x=500, y=300, w=100, h=80    # 调整后图像上的坐标
    )
    
    print("测试完成！")
    print("\n使用方法：")
    print("1. 修改 test_custom_coordinates 函数的参数来测试您的坐标")
    print("2. 或者直接调用 convert_coordinates_to_original 函数")
    print("3. 函数签名：convert_coordinates_to_original(x, y, w, h, original_size, resized_size)") 