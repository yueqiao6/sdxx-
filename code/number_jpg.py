import os

# 指定要重命名的文件夹路径
folder_path = 'F:/v11/ultralytics-main/datas/images/train'

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 过滤出图片文件（根据需要添加更多扩展名）
image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
images = [f for f in files if f.lower().endswith(image_extensions)]

# 按文件名排序
images.sort()

# 重命名文件
for index, image in enumerate(images, start=1):
    # 创建新的文件名
    new_name = f'images_{index:04d}{os.path.splitext(image)[1]}'
    # 完整路径
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, new_name)

    # 重命名
    os.rename(old_path, new_path)

print("重命名完成！")
