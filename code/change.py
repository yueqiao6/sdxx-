import os

def delete_xml_files(folder_path):
    """删除指定文件夹中的所有XML文件"""
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(folder_path, filename)
            os.remove(xml_file_path)
            print(f"已删除: {xml_file_path}")

# 指定包含XML文件的文件夹路径
folder_path = '/datas/labels/valid'  # 替换为你的文件夹路径
delete_xml_files(folder_path)
