from moviepy.editor import VideoFileClip
videoPath = ""
from pydub import AudioSegment
sound = AudioSegment.from_wav(audioPath)
sound = sound.set_frame_rate(16000)
sound = sound.set_channels(1)
path = “调参后的音频.wav"
