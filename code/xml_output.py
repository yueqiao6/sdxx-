from ultralytics import YOLO
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 加载训练好的模型
model = YOLO("./best.pt")

# 文件夹路径
image_folder = "F:/v11/test"
output_folder = "F:/v11/test_output_xml"  # 保存XML文件的文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的每个图像文件并进行推理
for image_file in os.listdir(image_folder):
    if image_file.endswith(('.jpg', '.jpeg', '.png')):  # 检查是否为图像文件
        image_path = os.path.join(image_folder, image_file)
        results = model(image_path)  # 对图像进行推理

        # 获取第一个结果
        result = results[0]  # 取第一个推理结果

        # 提取推理结果（包括边界框坐标、类别、置信度等）
        boxes = result.boxes.xyxy  # 获取边界框坐标（[xmin, ymin, xmax, ymax]）
        scores = result.boxes.conf  # 置信度
        class_ids = result.boxes.cls  # 类别 ID

        # 获取类别名称映射
        class_names = model.names  # 获取模型的类别名称列表

        # 获取原图尺寸（宽度和高度）
        img_width, img_height = result.orig_img.shape[1], result.orig_img.shape[0]

        # 创建 XML 树的根节点
        annotation = ET.Element('annotation')

        # 添加文件名
        filename = ET.SubElement(annotation, 'filename')
        filename.text = image_file

        # 添加文件尺寸（图像宽度和高度）
        size = ET.SubElement(annotation, 'size')
        width = ET.SubElement(size, 'width')
        height = ET.SubElement(size, 'height')
        depth = ET.SubElement(size, 'depth')
        width.text = str(img_width)  # 图像宽度
        height.text = str(img_height)  # 图像高度
        depth.text = str(3)  # 彩色图像通常为3（RGB）

        # 添加每个检测框的信息
        for i, box in enumerate(boxes):
            obj = ET.SubElement(annotation, 'object')

            # 类别名称（根据class_ids获取类别名称）
            name = ET.SubElement(obj, 'name')
            name.text = class_names[int(class_ids[i].item())]  # 使用类别 ID 获取类别名称

            # 坐标信息（xmin, ymin, xmax, ymax）
            bndbox = ET.SubElement(obj, 'bndbox')
            xmin = ET.SubElement(bndbox, 'xmin')
            ymin = ET.SubElement(bndbox, 'ymin')
            xmax = ET.SubElement(bndbox, 'xmax')
            ymax = ET.SubElement(bndbox, 'ymax')
            xmin.text = str(int(box[0]))  # xmin
            ymin.text = str(int(box[1]))  # ymin
            xmax.text = str(int(box[2]))  # xmax
            ymax.text = str(int(box[3]))  # ymax

            # 置信度
            confidence = ET.SubElement(obj, 'confidence')
            confidence.text = str(scores[i].item())  # 置信度

        # 创建XML文件的路径
        xml_filename = os.path.splitext(image_file)[0] + '.xml'
        xml_filepath = os.path.join(output_folder, xml_filename)

        # 将 XML 树保存到文件
        tree = ET.ElementTree(annotation)
        tree.write(xml_filepath)

        # 格式化 XML 文件（美化输出）
        xml_str = minidom.parse(xml_filepath).toprettyxml(indent="  ")
        with open(xml_filepath, 'w') as f:
            f.write(xml_str)

        print(f"XML file saved for {image_file} at {xml_filepath}")
