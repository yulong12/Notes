import json
import requests
from PIL import Image
from ray import serve
from starlette.requests import Request
from transformers import ChineseCLIPModel, ChineseCLIPProcessor

@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
class Cliper:
    def __init__(self):
        model_path = '/Users/zhangyulong/Documents/vscodeWorkspace/Notes/clip_Project/model/chinese-clip-vit-base-patch16'
        self.model = ChineseCLIPModel.from_pretrained(model_path)
        self.processor = ChineseCLIPProcessor.from_pretrained(model_path)

    async def encodeImage(self, url):
        # 下载并处理图像
        try:
            image = Image.open(requests.get(url, stream=True).raw)
            inputs = self.processor(images=image, return_tensors="pt")
            image_features = self.model.get_image_features(**inputs)
            image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)  # 标准化
            return image_features.tolist()  # 转换为列表以便JSON序列化
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

    async def __call__(self, http_request: Request):
        try:
            # 解析请求体中的JSON
            body = await http_request.json()
            image_url = body.get('image_url')
            if not image_url:
                raise ValueError("Missing 'image_url' in request body")

            # 编码图像
            img_vector = await self.encodeImage(image_url)
            if img_vector is None:
                return {"error": "Failed to encode image"}

            # 打印并返回结果
            print("=========img_vector=========")
            print(img_vector)
            return json.dumps({"image_vector": img_vector})
        except Exception as e:
            return {"error": str(e)}

# 部署服务
clip_app_embedding = Cliper.bind()