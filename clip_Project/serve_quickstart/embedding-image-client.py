import json
import requests

# 服务的URL
service_url = 'http://127.0.0.1:8000/' 

# 要发送的图像URL
image_url = 'https://clip-cn-beijing.oss-cn-beijing.aliyuncs.com/pokemon.jpeg'

# 构建请求体
data = {'image_url': image_url}

# 发送POST请求
response = requests.post(service_url, json=data)

# 检查响应状态码
if response.status_code == 200:
    # 解析并打印响应内容
    response_data = response.json()
    print("Service response:")
    print(response_data)
else:
    # 打印错误信息
    print(f"Failed to get response from service. Status code: {response.status_code}")
    print(response.text)