from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests


def generate_caption(image_url):
    """
    生成图像描述
    :param image_url: 图像的URL
    :return: 图像描述
    """
    # 下载预训练模型
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # 读图并处理
    image = Image.open(requests.get(image_url, stream=True).raw).convert('RGB')
    #another way to read image
    # image = Image.open(image_path).convert('RGB')
    inputs = processor(images=image, return_tensors="pt")

    # 推理生成文本
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    return caption

if __name__ == "__main__":
    # 示例图像URL
    image_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
    # image_path = "/content/Doraemon.jpg"
    
    # 生成描述
    # caption = generate_caption(image_path)
	caption = generate_caption(image_url)
    
    # 打印结果
    print("Generated Caption:", caption)