# cresc

## Installation

Please make sure to use Python3.5

### Mac

1. Install [portaudio](http://www.portaudio.com/) via brew
2. Create virtual environment `python -m venv <ENV NAME>`
3. Activate the env `source <ENV NAME>/bin/activate`
4. Install dependencies `pip install -r requirements.txt`


### Raspbian

Coming soon.


## Getting Started

You can check available sound devices.

```
python3 show-devices.py
```

Playing recorder saound.

```
python3 basics/play-wave-threading.py samples/c-full.wave
```

Recording sound from mic.

```
python3 basics/record-wave.py <WAVE FILE NAME>
```
