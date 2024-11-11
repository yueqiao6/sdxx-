from ultralytics import YOLO
import os

# 加载训练好的模型
model = YOLO("./best_pro.pt")

# 文件夹路径
image_folder = "F:/v11/test"


# 遍历文件夹中的每个图像文件并进行推理
for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  # 检查是否为图像文件
        image_path = os.path.join(image_folder, image_file)
        results = model(image_path,save=True)  # 对图像进行推理
