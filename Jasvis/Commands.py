import speech_recognition
#import googletrans
import pyttsx3
import wikipediaapi
import random
import webbrowser
import traceback
import json
import wave
import pyautogui as pg
import keyboard
import os
import pygame
import openai
import uuid
import ctypes
import pytime
import VoiceAssistant
import Translation
import User

from VoiceAssistant import Translation
from googlesearch import search
from pyowm import OWM
from termcolor import colored
from playsound import playsound

def play_greetings(*args: tuple):
    playsound("morning.wav")


def play_joke(*args: tuple):
    greetings = [
        Translation.get(
            "Ad on the sex shop window: New! Inflatable Voodoo doll! Now you can stick more than just a needle into your enemy").format(
            Translation.person.name),
        Translation.get("Dad, did you pass the DNA test? Call me Uncle Vitya!").format(Translation.person.name),
        Translation.get("Do not be afraid to be *banished — everything is fine, everyone is their own here!").format(
            Translation.person.name),
    ]
    VoiceAssistant.play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])


def play_name_of_assistant(*args: tuple):
    greetings = [
        Translation.get("Hello, {}! My name is Friday. I am your assistant").format(Translation.person.name)
    ]
    VoiceAssistant.play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])


def phone_management(*args: tuple):
    playsound("yes.wav")
    pg.moveTo(1730, 1070, 0.2)
    pg.click()
    pg.moveTo(1350, 330, 0.5)
    pg.click()
    if not args[0]: return
    search_term = " ".join(args[0])
    keyboard.write(search_term)
    pg.moveTo(1400, 390, 0.7)
    pg.click()
    pg.moveTo(1500, 915)
    pg.click()


def jarvis(*args: tuple):
    tracks = ['yes.wav', 'work.wav', 'connect.wav']
    random_track = random.choice(tracks)
    playsound(random_track)


def play_pause(*args: tuple):
    pg.moveTo(500, 500)
    pg.click()


def mute(*args: tuple):
    keyboard.send("win+d")

def play_plans(*args: tuple):
    tracks = ['yes.wav', 'vs.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    # greetings = [
    #     translator.get("If everything goes according to plan nah * y, nah *y such a plan!").format(person.name)
    # ]
    # play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])


def dela(*args: tuple):
    playsound("dela.wav")


def thanks(*args: tuple):
    playsound("thanks.wav")


def wallpaper(*args: tuple):
    SPI_SETDESKWALLPAPER = 20
    wallpaper_dir = "C:\puhau\PS4\SHARE\Screenshots\Miles_Morales"
    wallpapers = os.listdir(wallpaper_dir)
    random_wallpaper = os.path.join(wallpaper_dir, random.choice(wallpapers))
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, os.path.abspath(random_wallpaper), 0)


#def play_greetings(*args: tuple):
    """
    Проигрывание случайной приветственной речи
    """
    """
    greetings = [
        translator.get("Hello, {}! How can I help you today?").format(person.name),
        translator.get("Good day to you {}! How can I help you today?").format(person.name)
    ]
    play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])
    """


def finish_work(*args: tuple):
    tracks = ['virub.wav', 'virub1.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    # greetings = [
    #     translator.get("Perform!").format(person.name)
    # ]
    # play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])
    os.system("shutdown/p")


def play_farewell_and_quit(*args: tuple):
    """
    Проигрывание прощательной речи и выход
    """
    tracks = ['virub.wav', 'virub1.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    # farewells = [
    #     translator.get("Goodbye, {}! Have a nice day!").format(person.name),
    #     translator.get("See you soon, {}!").format(person.name)
    # ]
    # play_voice_assistant_speech(farewells[random.randint(0, len(farewells) - 1)])
    # ttsEngine.stop()
    quit()


def search_for_term_on_google(*args: tuple):
    playsound("zapros.mp3")
    block = False
    if not args[0]: return
    search_term = " ".join(args[0])

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)

    # альтернативный поиск с автоматическим открытием ссылок на результаты (в некоторых случаях может быть небезопасно)
    search_results = []
    try:
        for _ in search(search_term,  # что искать
                        tld="com",  # верхнеуровневый домен
                        lang=Translation.assistant.speech_language,  # используется язык, на котором говорит ассистент
                        num=1,  # количество результатов на странице
                        start=0,  # индекс первого извлекаемого результата
                        stop=1,  # индекс последнего извлекаемого результата (я хочу, чтобы открывался первый результат)
                        pause=1.0,  # задержка между HTTP-запросами
                        ):
            search_results.append(_)
            webbrowser.get().open(_)

    # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
    except:
        # play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
        # traceback.print_exc()
        return

    #print(search_results)
    #play_voice_assistant_speech(translator.get("Here is what I found for {} on google").format(search_term))


def music(*args: tuple):
    tracks = ['yes.wav', 'zagrus.wav', 'zapros.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    if not args[0]: return
    url = "https://open.spotify.com/search"
    webbrowser.get().open(url)
    if not args[0]: return
    search_term = " ".join(args[0])
    pg.moveTo(1000, 1000)
    pg.moveTo(1000, 1000, 0.9)
    pg.moveTo(800, 800, 0.9)
    pg.moveTo(1000, 1000, 0.9)
    pg.moveTo(600, 120, 0.9)
    pg.click()
    keyboard.write(search_term)
    keyboard.send("enter")
    pg.moveTo(600, 500, 0.9)
    pg.click()
    pg.moveTo(360, 600, 0.9)
    pg.click()


def film_kinogo(*args: tuple):
    tracks = ['yes.wav', 'zagrus.wav', 'zapros.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    if not args[0]: return
    url = "https://kinogo.biz"
    webbrowser.get().open(url)
    if not args[0]: return
    search_term = " ".join(args[0])
    pg.moveTo(1000, 500)
    pg.moveTo(1300, 100, 0.5)
    pg.click()
    keyboard.write(search_term)
    keyboard.send("enter")


def using_GPT(*args:tuple):
    playsound("yes.wav")
    my_file = open("GPT.py", "w+")
    if not args[0]: return
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    search_term = " ".join(args[0])
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=search_term,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    my_file.write(response+"\n\n")
    my_file.close()


def search_for_video_on_youtube(*args: tuple):
    tracks = ['yes.wav', 'zagrus.wav', 'zapros.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    # play_voice_assistant_speech(translator.get("Here is what I found for {} on youtube").format(search_term))


def new(*args: tuple):
    keyboard.send("control + f5")


def song(*args: tuple):
    # if not args[0]: return
    url = "https://www.youtube.com/watch?v=CTmKrwFu7wg"
    webbrowser.get().open(url)
    VoiceAssistant.play_voice_assistant_speech(Translation.get("Here is what I found for {} on youtube"))


def say_words(*args: tuple):
    if not args[0]: return
    search_term = " ".join(args[0])
    VoiceAssistant.play_voice_assistant_speech(Translation.get("{}").format(search_term))


def seasonvar(*args: tuple):
    tracks = ['yes.wav', 'zagrus.wav', 'zapros.wav']
    random_track = random.choice(tracks)
    playsound(random_track)
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "http://seasonvar.ru/search?q=" + search_term
    webbrowser.get().open(url)


def search_for_definition_on_wikipedia(*args: tuple):
    if not args[0]: return

    search_term = " ".join(args[0])

    # установка языка (в данном случае используется язык, на котором говорит ассистент)
    wiki = wikipediaapi.Wikipedia(Translation.assistant.speech_language)

    # поиск страницы по запросу, чтение summary, открытие ссылки на страницу для получения подробной информации
    wiki_page = wiki.page(search_term)
    try:
        if wiki_page.exists():
            VoiceAssistant.play_voice_assistant_speech(Translation.get("Here is what I found for {} on Wikipedia").format(search_term))
            webbrowser.get().open(wiki_page.fullurl)

            # чтение ассистентом первых двух предложений summary со страницы Wikipedia
            # (могут быть проблемы с мультиязычностью)
            VoiceAssistant.play_voice_assistant_speech(wiki_page.summary.split(".")[:2])
        else:
            # открытие ссылки на поисковик в браузере в случае, если на Wikipedia не удалось найти ничего по запросу
            VoiceAssistant.play_voice_assistant_speech(Translation.get(
                "Can't find {} on Wikipedia. But here is what I found on google").format(search_term))
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)

    # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
    except:
        VoiceAssistant.play_voice_assistant_speech(Translation.get("Seems like we have a trouble. See logs for more information"))
        traceback.print_exc()
        return


# def get_translation(*args: tuple):
#     if not args[0]: return
#
#     search_term = " ".join(args[0])
#     google_translator = googletrans.Translator()
#     translation_result = ""
#
#     old_assistant_language = assistant.speech_language
#     try:
#         # если язык речи ассистента и родной язык пользователя различаются, то перевод выполяется на родной язык
#         if assistant.speech_language != person.native_language:
#             translation_result = google_translator.translate(search_term,  # что перевести
#                                                              src=person.target_language,  # с какого языка
#                                                              dest=person.native_language)  # на какой язык
#
#             play_voice_assistant_speech("The translation for {} in Russian is".format(search_term))
#
#             # смена голоса ассистента на родной язык пользователя (чтобы можно было произнести перевод)
#             assistant.speech_language = person.native_language
#             setup_assistant_voice()
#
#         # если язык речи ассистента и родной язык пользователя одинаковы, то перевод выполяется на изучаемый язык
#         else:
#             translation_result = google_translator.translate(search_term,  # что перевести
#                                                              src=person.native_language,  # с какого языка
#                                                              dest=person.target_language)  # на какой язык
#             play_voice_assistant_speech("По-английски {} будет как".format(search_term))
#
#             # смена голоса ассистента на изучаемый язык пользователя (чтобы можно было произнести перевод)
#             assistant.speech_language = person.target_language
#             setup_assistant_voice()
#
#         # произнесение перевода
#         play_voice_assistant_speech(translation_result.text)
#
#     # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
#     except:
#         play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
#         traceback.print_exc()
#
#     finally:
#         # возвращение преждних настроек голоса помощника
#         assistant.speech_language = old_assistant_language
#         setup_assistant_voice()


def get_weather_forecast(*args: tuple):

    # в случае наличия дополнительного аргумента - запрос погоды происходит по нему,
    # иначе - используется город, заданный в настройках
    if args[0]:
        city_name = args[0][0]
    else:
        city_name = Translation.person.home_city

    try:
        # использование API-ключа, помещённого в .env-файл по примеру WEATHER_API_KEY = "01234abcd....."
        weather_api_key = os.getenv("83822e545cc51d591e09d2601825f9e7")
        open_weather_map = OWM(weather_api_key)

        # запрос данных о текущем состоянии погоды
        weather_manager = open_weather_map.weather_manager()
        observation = weather_manager.weather_at_place(city_name)
        weather = observation.weather

    # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
    except:
        VoiceAssistant.play_voice_assistant_speech(Translation.get("Seems like we have a trouble. See logs for more information"))
        traceback.print_exc()
        return

    # разбивание данных на части для удобства работы с ними
    status = weather.detailed_status
    temperature = weather.temperature('celsius')["temp"]
    wind_speed = weather.wind()["speed"]
    pressure = int(weather.pressure["press"] / 1.333)  # переведено из гПА в мм рт.ст.

    # вывод логов
    print(colored("Weather in " + city_name +
                  ":\n * Status: " + status +
                  "\n * Wind speed (m/sec): " + str(wind_speed) +
                  "\n * Temperature (Celsius): " + str(temperature) +
                  "\n * Pressure (mm Hg): " + str(pressure), "yellow"))

    # озвучивание текущего состояния погоды ассистентом (здесь для мультиязычности требуется дополнительная работа)
    VoiceAssistant.play_voice_assistant_speech(Translation.get("It is {0} in {1}").format(status, city_name))
    VoiceAssistant.play_voice_assistant_speech(Translation.get("The temperature is {} degrees Celsius").format(str(temperature)))
    VoiceAssistant.play_voice_assistant_speech(Translation.get("The wind speed is {} meters per second").format(str(wind_speed)))
    VoiceAssistant.play_voice_assistant_speech(Translation.get("The pressure is {} mm Hg").format(str(pressure)))



def change_language(*args: tuple):
    """
    Изменение языка голосового ассистента (языка распознавания речи)
    """
    Translation.assistant.speech_language = "ru" if Translation.assistant.speech_language == "en" else "en"
    VoiceAssistant.setup_assistant_voice()
    print(colored("Language switched to " + Translation.assistant.speech_language, "cyan"))


def run_person_through_social_nets_databases(*args: tuple):
    """
    Поиск человека по базе данных социальных сетей ВКонтакте и Facebook
    :param args: имя, фамилия TODO город
    """
    tracks = ['yes.wav', 'zagrus.wav', 'zapros.wav']
    random_track = random.choice(tracks)
    playsound(random_track)

    if not args[0]: return

    google_search_term = " ".join(args[0])
    vk_search_term = "_".join(args[0])
    fb_search_term = "-".join(args[0])

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + google_search_term + " site: vk.com"
    webbrowser.get().open(url)

    url = "https://google.com/search?q=" + google_search_term + " site: facebook.com"
    webbrowser.get().open(url)

    # открытие ссылкок на поисковики социальных сетей в браузере
    vk_url = "https://vk.com/people/" + vk_search_term
    webbrowser.get().open(vk_url)

    fb_url = "https://www.facebook.com/public/" + fb_search_term
    webbrowser.get().open(fb_url)

    #play_voice_assistant_speech(translator.get("Here is what I found for {} on social nets").format(google_search_term))
    pygame.time.wait(700)
    playsound('info.wav')

def toss_coin(*args: tuple):
    """
    "Подбрасывание" монетки для выбора из 2 опций
    """
    flips_count, heads, tails = 3, 0, 0

    for flip in range(flips_count):
        if random.randint(0, 1) == 0:
            heads += 1

    tails = flips_count - heads
    winner = "Tails" if tails > heads else "Heads"
    VoiceAssistant.play_voice_assistant_speech(Translation.get(winner) + " " + Translation.get("won"))
