from moviepy.editor import VideoFileClip
videoPath = "路径.mp4"
aduioPath = "路径.wav"
video = VideoFileClip(videoPath)
audio = video.audio
audio.write_audiofile(audioPath)
from pydub import AudioSegment
sound = AudioSegment.from_wav(audioPath)
sound = sound.set_frame_rate(16000)
sound = sound.set_channels(1)
path = “调参后的音频.wav"
sound.export(path.format = "wav")
from aip imoprt AipSpeech
APP_ID = "10252021"
API_KEY = "ZHe7788sh11GEjIAdEKeY"
SECRET_KEY = "JMMzHe7788BUSH1ZhEnM1YUEhh"
client = AipFace(APP_ID,API_KEY,SECRET_KEY)
def audio2text(wav):
    rejson = client.asr(wav,"wav",16000,{dev_pid":1537}
    if rejson["err_no"] == 0:
        msg= rejson["result"][0]
    else:
        msg = "语音识别错误“
    return msg
with open(path, "rb") as fp:
    wav=fp.read()
text = audio2text(wav)
def text2audio(wordText):
    result = client.synthesis(text, "zh", "1",{"vol":12,"spd"6,"pit":7,"per":4})
    if type(result) == dict:
        output = "语音合成错误“
    else：
        output = result
    return output
audio2 = text2audio(text)
with open("音频变音版.wav", "wb") as fp:
    fp.write(audio2)
print("变音文件生成完毕！")
    
