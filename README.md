# TTS using edge-tts

## Install
```
pip install edge-tts
```

## Notice
The tool calls the Microsoft online service.
So make sure **NOT to use private or sensitive data**.

## Quick start
Simply run:
```
python text2speech.py
```

Modify the text in `text/src1.txt` to decide the content you want to convert.
Modify the voice type in line 27 of `text2speech.py` to use a voice you like.

To try different voices, run:
```
python text2speech.py 1
```
```
python text2speech.py 2
```
where 1 is for Chinese voices, and 2 is for English voices.

## More info about edge-tts
Refer [here](https://github.com/rany2/edge-tts#installation) to learn more.
