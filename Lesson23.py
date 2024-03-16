"""创建语音识别客户端"""
from aip import AipSpeech
APP_ID = "10252021"
API_KEY = "ZHe7788sh11GEjIAdEKeY"
SECRET_KEY = "JMMzHe7788BUSH1ZhEnM1YUEhh" 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

"""语音识别接口调用函数"""
def audio2text(wav):
    rejson = client.asr(wav,"wav",16000,{"dev_pid": 1537})
    if rejson["err_no"] == 0:
        msg = rejson["result"][0]
    else:
        msg = "语音识别错误！"
    return msg

"""音频文件参数设置"""
from pydub import AudioSegment
sound=AudioSegment.from_wav("/Users/yequ/音频.wav")
sound=sound.set_frame_rate(16000)
sound=sound.set_channels(1)

"""导出参数设置后音频"""
path = "/Users/yequ/参数设置后音频.wav"
sound.export(path,format="wav")

"""读取参数设置后音频"""
with open(path, 'rb') as fp:
    wav = fp.read()

"""调用语音识别接口函数并输出结果"""
text = audio2text(wav)

def text2audio(wordText):
    result = client.synthesis(wordText, "zh", "1",{"vol": 12,"spd": 6,"pit": 7,"per": 4})
    if type(result) == dict:
        output = "语音合成错误"
    else:
        output = result
    return output

print(text2audio(text))
