import argparse
import os
import sys
import threading
from openai import OpenAI
from pydub import AudioSegment
import simpleaudio as sa
import time

# Constants
LOADING_THREAD_NAME = "Loading"
PLAYING_THREAD_NAME = "Playing"
FILE_NAME = "Vce.mp3"
TEMP_FILE_NAME = "temp.wav"
FILE_FORMAT = "wav"
ENTER_TEXT_MSG = "\nEnter Text (Then Press Return Twice): "
STORED_AUDIO_MSG = f"\n\nStored audio in '{FILE_NAME}'. Move a copy of this file elsewhere if you want to keep it."

# Thread status
thread_status = {LOADING_THREAD_NAME: False, PLAYING_THREAD_NAME: False}

# Thread lock
thread_lock = threading.Lock()


def spinner(thread_name):
    i = 0
    while threading.main_thread().is_alive():  # Keep running only while main thread is running
        with thread_lock:
            if thread_status.get(thread_name) or thread_status.get(thread_name) is None:
                break
        sys.stdout.write(f'\r{thread_name}' + '.' * (i % 3 + 1))
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1


def generate_audio(file_name, text_input, api_key=None):
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text_input,
    )
    response.stream_to_file(file_name)
    audio = AudioSegment.from_mp3(file_name)
    audio.export(TEMP_FILE_NAME, format=FILE_FORMAT)


def play_audio(file_name):
    wave_obj = sa.WaveObject.from_wave_file(file_name)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    os.remove(file_name)


def stream_to_file(file_name, text_input, api_key=None):
    success = False
    try:
        generate_audio(file_name, text_input, api_key)
        success = True

        with thread_lock:
            thread_status[LOADING_THREAD_NAME] = True

        playing_thread = threading.Thread(target=spinner, args=(PLAYING_THREAD_NAME,), daemon=True)
        playing_thread.start()
        play_audio(TEMP_FILE_NAME)

        with thread_lock:
            thread_status[PLAYING_THREAD_NAME] = True

        playing_thread.join()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        with thread_lock:
            if not success:
                thread_status[LOADING_THREAD_NAME] = None
                thread_status[PLAYING_THREAD_NAME] = None


def main(api_key=None, text_input=None):
    if text_input is None:
        print(ENTER_TEXT_MSG)
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        text_input = ' '.join(lines)

    loading_thread = threading.Thread(target=spinner, args=(LOADING_THREAD_NAME,), daemon=True)
    loading_thread.start()
    streaming_thread = threading.Thread(target=stream_to_file, args=(FILE_NAME, text_input, api_key,), daemon=True)
    streaming_thread.start()
    streaming_thread.join()
    loading_thread.join()

    with thread_lock:
        if thread_status[LOADING_THREAD_NAME] and thread_status[PLAYING_THREAD_NAME]:
            print(STORED_AUDIO_MSG)


parser = argparse.ArgumentParser(description='Generate text to speech with OpenAI')
parser.add_argument('--api-key', dest='api_key', action='store', default=None, help='API key for OpenAI')
parser.add_argument('--text', dest='text', action='store', default=None, help='Text to convert into speech')


def main(args=None):
    try:
        parser = argparse.ArgumentParser(description='Generate text to speech with OpenAI')
        parser.add_argument('--api-key', dest='api_key', action='store', default=None, help='API key for OpenAI')
        parser.add_argument('--text', dest='text', action='store', default=None, help='Text to convert into speech')
        args = parser.parse_args(args)

        api_key = args.api_key
        text_input = args.text

        if text_input is None:
            print(ENTER_TEXT_MSG)
            lines = []
            while True:
                line = input()
                if line:
                    lines.append(line)
                else:
                    break
            text_input = ' '.join(lines)

        loading_thread = threading.Thread(target=spinner, args=(LOADING_THREAD_NAME,), daemon=True)
        loading_thread.start()
        streaming_thread = threading.Thread(target=stream_to_file, args=(FILE_NAME, text_input, api_key,), daemon=True)
        streaming_thread.start()
        streaming_thread.join()
        loading_thread.join()

        with thread_lock:
            if thread_status[LOADING_THREAD_NAME] and thread_status[PLAYING_THREAD_NAME]:
                print(STORED_AUDIO_MSG)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Cleaning up...")
        if os.path.exists(TEMP_FILE_NAME):
            os.remove(TEMP_FILE_NAME)

    sys.exit(1)
