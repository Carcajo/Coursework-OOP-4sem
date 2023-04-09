import json
import os
import pyttsx3
import wave
import traceback
import User
import VoiceAssistant
import speech_recognition
import Translation

from VoiceAssistant import Translation
from termcolor import colored
from vosk import Model, KaldiRecognizer

def record_and_recognize_audio(*args: tuple):
    with Translation.microphone:
        recognized_data = ""

        # запоминание шумов окружения для последующей очистки звука от них
        Translation.recognizer.adjust_for_ambient_noise(Translation.microphone, duration=2)

        try:
            print("Listening...")
            audio = Translation.recognizer.listen(Translation.microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            VoiceAssistant.play_voice_assistant_speech(Translation.get("Can you check if your microphone is on, please?"))
            traceback.print_exc()
            return

        # использование online-распознавания через Google (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = Translation.recognizer.recognize_google(audio, language=Translation.assistant.recognition_language).lower()

        except speech_recognition.UnknownValueError:
            pass  # play_voice_assistant_speech("What did you say again?")

        # в случае проблем с доступом в Интернет происходит попытка использовать offline-распознавание через Vosk
        except speech_recognition.RequestError:
            print(colored("Trying to use offline recognition...", "cyan"))
            recognized_data = use_offline_recognition()

        return recognized_data


def use_offline_recognition():
    recognized_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        if not os.path.exists("models/vosk-model-small-" + Translation.assistant.speech_language + "-0.4"):
            print(colored("Please download the model from:\n"
                          "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.",
                          "red"))
            exit(1)

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("models/vosk-model-small-" + Translation.assistant.speech_language + "-0.4")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    except:
        traceback.print_exc()
        print(colored("Sorry, speech service is unavailable. Try again later", "red"))

    return recognized_data
