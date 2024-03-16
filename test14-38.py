from aip import AipFace
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipFace(APP_ID,API_KEY,SECRET_KEY)
import base64
img_path = "图片路径“
with open(img_path, "rb") as file:
    res = file.read()
    img = base64.b64encode(res)
    img = str(img, 'utf-8')
img_type = "BASE64"
options = {
    'max_face_num': 10,
    "face_field": "age"}
ret_data = client.detect(img, img_type, options)
from PIL import Image
image = Image.open(img_path)
image_cp = image.copy()
from PIl import ImageDraw
from PIL import ImageFont
draw_img = ImageDraw.Draw(image_cp)
if ret_data['error_msg'] == 'SUCCESS':
    for item in ret_data["result"]["face_list]:
    location = item["location]
    age = item["age"]
    x1 = location['left']
    y1 = location['top']
    x2 = x1 + location['width']
    y2 = y1 + location['height']
    font_path = "字体路径"
    color = "azure"
    font_size = location['height']//3
    font = ImageFont.truetype(font_path,font_size)
    text_positon = [x1,y1-1.5*font_size]
    text = f"age:{age}"
    draw_img.rectangle([x1,y1,x2,y2],outline = color,width = 3)
    draw_img.text(text_position,text,color,font)
    image_cp.save('存储路径‘)
else：
    print（“识别失败”）
    
