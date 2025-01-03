from PIL import Image
import requests
from transformers import ChineseCLIPProcessor, ChineseCLIPModel
model_path='/Users/zhangyulong/Documents/vscodeWorkspace/Notes/clip_Project/model/chinese-clip-vit-base-patch16'

class Cliper:
    def __init__(self):
        self.model=ChineseCLIPModel.from_pretrained(model_path)
        self.processor=ChineseCLIPProcessor.from_pretrained(model_path)
    def encodeImage(self,url):
    # compute image feature
        image = Image.open(requests.get(url, stream=True).raw)
        inputs = self.processor(images=image, return_tensors="pt")
        image_features = self.model.get_image_features(**inputs)
        image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)  # normalize
        return image_features
    def encodeText(self,texts):
        inputs = self.processor(text=texts, padding=True, return_tensors="pt")
        text_features = self.model.get_text_features(**inputs)
        text_features = text_features / text_features.norm(p=2, dim=-1, keepdim=True)
        return text_features
    def image_text_simility(self,texts,url):

        # compute image-text similarity scores
        image = Image.open(requests.get(url, stream=True).raw)
        inputs = self.processor(text=texts, images=image, return_tensors="pt", padding=True)
        outputs = self.model(**inputs)
        logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1) 
        return probs

cliper=Cliper()
print("##########image_features#######")
url = "https://clip-cn-beijing.oss-cn-beijing.aliyuncs.com/pokemon.jpeg"
image_features=cliper.encodeImage(url)
print(image_features)
print("#########texts_feature########")
# Squirtle, Bulbasaur, Charmander, Pikachu in English
texts = ["杰尼龟", "妙蛙种子", "小火龙", "皮卡丘"]
texts_feature=cliper.encodeText(texts)
print(texts_feature)
print("#########simility###########")
simility=cliper.image_text_simility(texts,url)
print(simility)