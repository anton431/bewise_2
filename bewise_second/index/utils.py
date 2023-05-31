import os
from pydub import AudioSegment

from bewise_second.settings import BASE_DIR


def convert_to_mp3(audio_file):
    "Конвектирует wav -> mp3"
    print(audio_file)
    audio_file = str(audio_file)
    audio_name = '.'.join(audio_file.split('.')[:-1])
    print(audio_name)

    src = os.path.join(BASE_DIR, rf"media\{audio_name}.wav") # src to dst
    dst = os.path.join(BASE_DIR, rf"media\{audio_name}.mp3") # wav to mp3

    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    os.remove(src) # удаляем из media wav файл

    return f'{audio_name}.mp3'