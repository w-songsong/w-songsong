from aip import AipNlp
content = "新闻内容"
title = "标题"
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
if len(content)>3000 or len(title)>200:
    print('字符串长度过长，请重新编辑。‘）
client = AipNlp(APP_ID,API_KEY,SECRET_KEY)
max_summary_len = 50
options = {}
options["title"] = title
result = client.newsSummary(content,max_summary_len,options)
print(result)
summary = result['summary']
print(summary)
