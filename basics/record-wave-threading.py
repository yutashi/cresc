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


frames = []
def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return(None, pyaudio.paContinue)

stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index=0,
            frames_per_buffer=CHUNK,
            start=False,
            stream_callback=callback
        )


if __name__ == '__main__':
    print('Starting in 3 seconds')
    for i in range(3):
        print(str(i) + '...')
        time.sleep(1)

    print('Recording...')
    stream.start_stream()
    time.sleep(RECORD_SECONDS)

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
