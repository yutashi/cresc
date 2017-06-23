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


audio = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    return(in_data, pyaudio.paContinue)

stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            input_device_index=0,
            output_device_index=1,
            frames_per_buffer=CHUNK,
            start=False,
            stream_callback=callback
        )


if __name__ == '__main__':
    print('Recording...')
    stream.start_stream()
    time.sleep(10)

    print('Finished recording')
    stream.stop_stream()
    stream.close()
    audio.terminate()
