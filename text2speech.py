#!/usr/bin/env python3

"""
Basic example of edge_tts usage.
INSTALL: pip install edge-tts
"""
import os
import sys
import asyncio
import edge_tts

os.makedirs('voice/', exist_ok=True)

def load_text(fn):
    with open(fn, 'r') as f:
        texts = f.readlines()
    text = ''.join(texts)
    return text


async def _main() -> None:
    # prepare text
    fn = 'text/src1.txt'
    TEXT = load_text(fn)

    # prepare voice type
    # VOICE = "zh-CN-YunxiNeural"
    VOICE = "zh-CN-YunyangNeural"

    # speak
    OUTPUT_FILE = "voice/test.mp3"
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


async def eval_voices(lang:str='zh') -> None:
    # prepare text
    if lang == 'zh':
        TEXT = '你好，同学！今天天气真不错，祝你走向成功！'
    elif lang == 'en':
        TEXT = 'Today is a good day for the Chinese economy and Chinese workers.'
    else:
        raise ValueError('only support zh and en.')
    # prepare voice type
    voices = await edge_tts.list_voices()
    cnt = 0
    for voice in voices:
        voice_sn:str = voice['ShortName']
        if voice_sn.startswith(lang):
            print(voice_sn)
            cnt += 1
            # speak
            out_fn = os.path.join('voice/', voice_sn + '.mp3')
            communicate = edge_tts.Communicate(TEXT, voice_sn)
            await communicate.save(out_fn)
    print(f'{cnt} voice types have been tested.')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        mode = "0"
    else:
        mode = sys.argv[1]
    loop = asyncio.get_event_loop()
    try:
        if mode == "0":
            loop.run_until_complete(_main())
        elif mode == "1":
            loop.run_until_complete(eval_voices('zh'))
        elif mode == "2":
            loop.run_until_complete(eval_voices('en'))
    finally:
        loop.close()
