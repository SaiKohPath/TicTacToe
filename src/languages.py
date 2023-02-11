chosen_language = None


def get_language_dictionaries():
    # FIXME CHANGE TO DICT
    languages = [
        {'eng': {
            'choice': 'You have chosen English as your language.',
            'player1': 'Player 1: Do you want to be X or O?\n(X/O)\n',
            'invalid_input': 'Sorry, invalid input. Please chose X or O:\n(X/O)\n',
            'chosen_mark': 'Player 1 has chosen _.\nPlayer 1 will go first.',
            'start_rules': 'Are you ready to start or would you like to read the rules?\nStart or Rules\n(S/R)\n',
            'invalid_start_rules': "Sorry, I didn't understand. Please try again.\n\nAre you ready to start or would you like to read the rules?\nStart or Rules\n(S/R)\n",
            'rules': "Rules:\n1. The game is played on a grid that's 3 squares by 3 squares.\n2. Player 1 is _, player 2 (or the computer) is _.\n3. Players take turns putting their marks in empty squares.\n4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n\nIf all 9 squares are full and there is no winner. The game ends in a tie.\n(OK)\n"
        }},
        {'swe': {
            'choice': 'Du har valt Svenska som ditt språk.',
            'player1': 'Spelare 1: Vill du vara X eller O?\n(X/O)\n',
            'invalid_input': 'Felinmatning. Var snäll och välj X eller O:\n(X/O)\n',
            'chosen_mark': 'Spelare 1 har valt _.\nSpelare 1 kör först.',
            'start_rules': 'Är du redo att starta eller vill du läsa reglerna?\nStart eller Regler\n(S/R)\n',
            'invalid_start_rules': "Förlåt, jag förstod inte. Please vänligen försök igen.\n\nÄr du redo att starta eller vill du läsa reglerna?\nStart eller Regler\n(S/R)\n",
            'rules': "Regler:\n1. Spelet spelas på ett rutnät som är 3 rutor gånger 3 rutor.\n2. Spelare 1 är _, spelare 2 (eller datorn) är _.\n3. Spelare turas om att sätta sina poäng i tomma rutor.\n4. Den första spelaren som får 3 av sina marker i rad (upp, ner, tvärs över eller diagonalt) vinner.\n\nOm alla 9 rutor är fulla och det finns ingen vinnare avslutas spelet som oavgjort.\n(OK)\n"
        }}
    ]

    return languages


def get_default_language():
    languages = get_language_dictionaries()
    english_language = languages[0]
    return english_language["eng"]


def get_valid_languages(languages):
    valid_languages = []

    for language_dictionary in languages:
        keys = list(language_dictionary.keys())
        language_name = keys[0]
        valid_languages.append(language_name)

    return valid_languages


def choose_language():
    language_index = 0
    languages = get_language_dictionaries()
    valid_languages = get_valid_languages(languages)

    print('Welcome to Tic Tac Toe!')
    chosen_language = input('Chose language:\n(Eng/Swe)\n')

    while chosen_language not in valid_languages:
        x = input('Invalid answere, please try again:\n(Eng/Swe)\n')
        chosen_language = x.lower()

    while chosen_language != valid_languages[language_index]:
        language_index += 1
    else:
        checker = valid_languages[language_index]
        language_dictionary = languages[language_index][checker]
        print(languages[language_index][checker]['choice'])

    return language_dictionary


def get_text(text_key, *args):
    language = chosen_language

    if chosen_language is None:
        language = get_default_language()

    if text_key not in language:
        print(f"Could not find text for text_key: {text_key}")
        return "Null"

    text = language[text_key]

    for string_to_input in args:
        temp_str = text.replace("_", string_to_input, 1)
        text = temp_str

    return text


def set_language(language):
    global choose_language
    choose_language = language
