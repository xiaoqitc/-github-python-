import os
import requests

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.realpath(__file__))

# 提示用户输入GitHub文件的URL
file_url = input("请输入GitHub文件的URL：")

# 定义下载文件的函数
def download_file(url, directory):
    try:
        # 发送HTTP GET请求
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 构造文件的完整路径
        file_name = os.path.basename(url)
        file_path = os.path.join(directory, file_name)

        # 写入文件
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"文件已下载到：{file_path}")
    except requests.RequestException as e:
        print(f"请求错误：{e}")
    except IOError as e:
        print(f"文件写入错误：{e}")

# 调用函数下载文件
download_file(file_url, script_dir)
