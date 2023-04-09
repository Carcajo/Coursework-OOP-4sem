import os
import speech_recognition
import pyttsx3
import User
import VoiceAssistant
import Translation
import Recognize_audio
import Execute_command

from termcolor import colored
if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных пользователя
    person = User.User()
    person.name = "Maksim"
    person.home_city = "Minsk"
    person.native_language = "ru"
    person.target_language = "en"

    # настройка данных голосового помощника
    assistant = VoiceAssistant.VoiceAssistant()
    assistant.name = "Friday"
    assistant.sex = "female"
    assistant.speech_language = "en"

    # установка голоса по умолчанию
    VoiceAssistant.setup_assistant_voice()

    # добавление возможностей перевода фраз (из заготовленного файла)
    translator = Translation.Translation()

    # загрузка информации из .env-файла (там лежит API-ключ для OpenWeatherMap)
    # load_dotenv()

    while True:
        # старт записи речи с последующим выводом распознанной речи и удалением записанного в микрофон аудио
        voice_input = Recognize_audio.record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(colored(voice_input, "blue"))

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        Execute_command.execute_command_with_name(command, command_options)


