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
