from languages import choose_language, set_language, get_text


def game_start(language):
    marks = ['X', 'x', 'O', 'o']

    player1 = input(language['player1'])

    while player1 not in marks:
        player1 = input(language['invalid_input'])

    if player1 in marks[0:2]:
        player2 = 'O'
    else:
        player2 = 'X'

    chosen_mark = get_text("chosen_mark", player1.upper())
    print(chosen_mark)

    start_and_rules_input = ['S', 's', 'R', 'r']
    if player1 in marks:
        start_rules = input(language['start_rules'])

        while start_rules not in start_and_rules_input:
            start_rules = input(language['invalid_start_rules'])

    if start_rules in start_and_rules_input[0:2]:
        pass
    elif start_rules in start_and_rules_input[2:4]:
        rules = get_text('rules', player1.upper(), player2)
        start_rules = input(rules)

    return player1.upper()


lang = choose_language()
set_language(lang)


test = game_start(lang)
