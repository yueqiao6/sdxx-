import cv2
import numpy as np
from openvino.inference_engine import IECore

# 加载模型
model_xml = "path/to/your/model.xml"
model_bin = "path/to/your/model.bin"

ie = IECore()
net = ie.read_network(model=model_xml, weights=model_bin)
input_blob = next(iter(net.input_info))
output_blob = next(iter(net.outputs))

# 创建推理请求
exec_net = ie.load_network(network=net, device_name='CPU')

# 读取并预处理输入图像
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    n, c, h, w = net.input_info[input_blob].input_data.shape
    image_resized = cv2.resize(image, (w, h))
    image_resized = image_resized.transpose((2, 0, 1))  # HWC to CHW
    image_resized = image_resized.reshape((n, c, h, w))
    return image_resized, image

# 进行推理
def inference(image_path):
    image_data, original_image = preprocess_image(image_path)
    result = exec_net.infer(inputs={input_blob: image_data})

    return result, original_image

# 可视化结果
def draw_results(original_image, result):
    # 假设输出的结构为 [class_id, confidence, x_min, y_min, x_max, y_max]
    boxes = result[output_blob]
    for box in boxes[0][0]:  # 遍历所有检测框
        class_id, confidence, x_min, y_min, x_max, y_max = box
        if confidence > 0.5:  # 设置阈值
            cv2.rectangle(original_image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
            cv2.putText(original_image, f'Class: {int(class_id)} Conf: {confidence:.2f}',
                        (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# 主程序
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # 输入图像路径
    result, original_image = inference(image_path)
    draw_results(original_image, result)

    # 显示结果
    cv2.imshow("Detection Result", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
