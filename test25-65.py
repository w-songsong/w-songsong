from moviepy.editor import VideoFileClip
videoPath = "路径A.mp4"
aduioPath = "路径A.wav"
video = VideoFileClip(videoPath)
audio = video.audio
audio.write_audiofile(audioPath)
from pydub import AudioSegment
sound = AudioSegment.from_wav(audioPath)
sound = sound.set_frame_rate(16000)
sound = sound.set_channels(1)
path = “调参后的音频.wav"
sound.export(path.format = "wav")
from pydub.slience import detect_nonsilent
min_silence_ = 500
silence_thresh = -50
timestamp_list = detect_nonsilent(sound,min_silence_len,silence_thresh)
B_sound = sound[:timestamp_list[-3][1]]
B_sound.export('路径B.wav',format = "wav)
A_sound = ound[:timestamp_list[-2][0]]
A_sound.export('路径B.wav',format = "wav)
from aip import AipSpeech
APP_ID = '10252021'
API_KEY = 'ZHe7788sh11GEjIAdEKeY'
SECRET_KEY = 'JMMzHe7788BUSH1ZhEnM1YUEhh'
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
def audio2text(wav):
    rejson = client.asr(wav, "wav", 16000,{"dev_pid":1537})
    if rejson["err_no"] == 0:
        msg = rejson["result"][0]
    else:
        msg = "语音识别错误“
    return msg
def read_file(filePath):
    with open(filePath,"rb") as fp:
        wavsapmle = fp.read()
        return wavsample
B_text = audio2text(read_file("路径B.wav"))
A_text = audio2text(read_file("路径A.wav"))
def text2audio(wordText, dict_):
    result = client.synthesis(wordText, "zh", "1", dict_)
    if type(result) == dict:
        output "语音合成错误“
    else:
        output = result
    return output
B_dict = {"vol":12, "spd":2, "pit":7, "per":3}
B_audio = text2audio(B_text,B_dict)
A_dict = {"vol":12, "spd":8, "pit":7, "per":4}
A_audio = text2audio(A_text,A_dict)
path = '变换后的语音.wav'
open(path,"wb").write(B_audio)
open(path,"wb").write(A_audio)
        
