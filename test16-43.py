filePath = '二维码‘.png'
with open(filePath, 'rb') as f:
    image = f.read()
from aip import AipOcr
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
result = client.qrcode(image)
text = result["codes_result"][0]["text"][0]
print(text)
