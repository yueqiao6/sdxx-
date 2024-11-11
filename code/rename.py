import os


def rename_files_in_directory(directory):
    # 获取文件夹中所有文件
    files = os.listdir(directory)

    # 过滤出文件（可选：根据需要过滤出特定文件类型）
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    # 对文件按自然顺序排序
    files.sort()

    for index, file in enumerate(files):
        # 生成新文件名
        new_name = f"valid_{index + 1:04d}"  # 使用04d格式化成4位数字
        # 获取原文件的扩展名
        ext = os.path.splitext(file)[1]
        # 完成新文件名
        new_file_name = f"{new_name}{ext}"

        # 获取完整的原始和新文件路径
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_file_name)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: "{old_file_path}" to "{new_file_path}"')



target_directory = 'F:/v11/ultralytics-main/datas/labels/valid'
rename_files_in_directory(target_directory)
