#-*-coding:utf-8-*-
#!/usr/bin/python
import pyaudio
import wave
import sys
import time


try:
    WAVE_FILE = sys.argv[1]
except:
    print('File name is required as an argument.')
    sys.exit(1)

audio = pyaudio.PyAudio()
wf = wave.open(WAVE_FILE, 'rb')

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

stream = audio.open(
            format=audio.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            output_device_index=1,
            stream_callback=callback
        )


if __name__ == '__main__':
    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    audio.terminate()
