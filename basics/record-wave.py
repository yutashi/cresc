#-*-coding:utf-8-*-
#!/usr/bin/python
import pyaudio
import wave
import sys
import time


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2**11
RECORD_SECONDS = 3
try:
    WAVE_FILE = sys.argv[1]
except:
    print('File name is required as an argument.')
    sys.exit(1)


audio = pyaudio.PyAudio()
stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index=0,
            frames_per_buffer=CHUNK,
            start=False
        )


if __name__ == '__main__':
    print('Starting in 3 seconds')
    for i in range(3):
        print(str(i) + '...')
        time.sleep(1)

    print('Recording...')
    frames = []
    stream.start_stream()
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print('Finished recording')
    stream.stop_stream()
    stream.close()
    audio.terminate()

    print('Saving as a wave file...')
    wf = wave.open(WAVE_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
