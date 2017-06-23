import sys
import pyaudio

audio = pyaudio.PyAudio()
count = audio.get_device_count()

if __name__ == '__main__':
    devices = []
    for i in range(count):
        devices.append(audio.get_device_info_by_index(i))

    for i, dev in enumerate(devices):
        print(i, dev['name'])
