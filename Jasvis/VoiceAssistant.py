import pyttsx3
import speech_recognition

from User import User


class VoiceAssistant:
    name = "Friday"
    sex = "female"
    speech_language = "en"
    recognition_language = "en"

class Translation(User, VoiceAssistant):
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных пользователя
    person = User()
    person.name = "Maksim"
    person.home_city = "Minsk"
    person.native_language = "ru"
    person.target_language = "en"

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Friday"
    assistant.sex = "female"
    assistant.speech_language = "en"



def setup_assistant_voice():
    voices = Translation.ttsEngine.getProperty("voices")

    if Translation.assistant.speech_language == "en":
        Translation.assistant.recognition_language = "en-US"
        if Translation.assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
           Translation.ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            Translation.ttsEngine.setProperty("voice", voices[2].id)
    else:
        Translation.assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        Translation.ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    Translation.ttsEngine.say(str(text_to_speech))
    Translation.ttsEngine.runAndWait()
