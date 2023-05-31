import os
from pydub import AudioSegment

from bewise_second.settings import BASE_DIR


def convert_to_mp3(audio_file):
    print(audio_file)
    audio_file = str(audio_file)
    audio_name = '.'.join(audio_file.split('.')[:-1])
    print(audio_name)
    # Enter the filename you want to convert it should in the same folder as this python file
    src = os.path.join(BASE_DIR, rf"media\{audio_name}.wav")
    dst = os.path.join(BASE_DIR, rf"media\{audio_name}.mp3")

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    os.remove(src)

    return f'{audio_name}.mp3'