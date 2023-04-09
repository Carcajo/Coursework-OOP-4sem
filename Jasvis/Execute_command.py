import Commands


def execute_command_with_name(command_name: str, *args: list):
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")


# перечень команд для использования (качестве ключей словаря используется hashable-тип tuple)
# в качестве альтернативы можно использовать JSON-объект с намерениями и сценариямив)
commands = {
    ("hello", "hi", "morning", "привет"): Commands.play_greetings,
    ("name", "представься", "имя"): Commands.play_name_of_assistant,
    ("say", "повтори", "скажи"): Commands.say_words,
    ("jarvis", "джарвис", "жарвис", "ты"): Commands.jarvis,
    ("bye", "goodbye", "quit", "exit", "stop", "пока", "стоп"): Commands.play_farewell_and_quit,
    ("search", "google", "find", "найди"): Commands.search_for_term_on_google,
    ("video", "youtube", "видео", "ютуб"): Commands.search_for_video_on_youtube,
    ("film", "cinema", "смотреть", "фильм"): Commands.film_kinogo,
    ("task", "solve", "задача", "узнай", "узнать"): Commands.using_GPT,
    ("mute", "звук", "без", "тишина", "тихо"): Commands.mute,
    # ("open","открой"):file_open,
    # ("full","весь","полный","экран","уменьши","меньше"):screen,
    ("seasonvar", "сериал"): Commands.seasonvar,
    ("music", "song", "spotify", "музыка", "песня"): Commands.music,
    # ("exit","pause","выход","пауза"): stop_programm,
    ("song", "чёрный"): Commands.song,
    ("how", "всё", "как"): Commands.dela,
    ("wallpaper", "обои", "смени", "поменяй"):Commands.wallpaper,
    ("thanks", "спасибо", "благодарю", "хорош", "красава"): Commands.thanks,
    ("play", "pause", "пауза", "плэй", "включи", "продолжить"): Commands.play_pause,
    ("end", "finish", "выключай", "выключи", "вырубай", "авада", "авадакедавра", "авадакедабра"): Commands.finish_work,
    ("call", "phone", "позвони", "звони", "звонок"):Commands. phone_management,
    ("new", "update", "обновить", "обнови"): Commands.new,
    ("wikipedia", "definition", "about", "определение", "википедия"):Commands.search_for_definition_on_wikipedia,
    #("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
    ("language", "translate", "язык"): Commands.change_language,
    ("weather", "forecast", "погода", "прогноз"): Commands.get_weather_forecast,
    ("facebook", "person", "run", "пробей", "контакт"): Commands.run_person_through_social_nets_databases,
    ("story", "joke", "шутка", "анекдот"):Commands. play_joke,
    ("aim", "plans", "цель", "планы"): Commands.play_plans,
    ("toss", "coin", "монета", "подбрось"): Commands.toss_coin
}