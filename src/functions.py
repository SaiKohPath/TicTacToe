def choose_language():
    valid_languages = ['eng','swe']
    language_index = 0
    languages = [
        {'eng':{
            'choice':'You have chosen English as your language.', 
            'player1':'Player 1: Do you want to be X or O?\n(X/O)\n', 
            'invalid_input':'Sorry, invalid input. Please chose X or O:\n(X/O)\n', 
            'chosen_mark':'Player 1 has chosen _.\nPlayer 1 will go first.', 
            'start_rules':'Are you ready to start or would you like to read the rules?\nStart or Rules\n(S/R)\n', 
            'invalid_start_rules':"Sorry, I didn't understand. Please try again.\n\nAre you ready to start or would you like to read the rules?\nStart or Rules\n(S/R)\n", 
            'rules':"Rules:\n1. The game is played on a grid that's 3 squares by 3 squares.\n2. Player 1 is _, player 2 (or the computer) is ^.\n3. Players take turns putting their marks in empty squares.\n4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n\nIf all 9 squares are full and there is no winner. The game ends in a tie.\n(OK)\n"
            }}, 
        {'swe':{
            'choice':'Du har valt Svenska som ditt språk.',
            'player1': 'Spelare 1: Vill du vara X eller O?\n(X/O)\n', 
            'invalid_input':'Felinmatning. Var snäll och välj X eller O:\n(X/O)\n', 
            'chosen_mark':'Spelare 1 har valt _.\nSpelare 1 kör först.', 
            'start_rules':'Är du redo att starta eller vill du läsa reglerna?\nStart eller Regler\n(S/R)\n', 
            'invalid_start_rules':"Förlåt, jag förstod inte. Please vänligen försök igen.\n\nÄr du redo att starta eller vill du läsa reglerna?\nStart eller Regler\n(S/R)\n", 
            'rules':"Regler:\n1. Spelet spelas på ett rutnät som är 3 rutor gånger 3 rutor.\n2. Spelare 1 är _, spelare 2 (eller datorn) är ^.\n3. Spelare turas om att sätta sina poäng i tomma rutor.\n4. Den första spelaren som får 3 av sina poäng i rad (upp, ner, tvärs över eller diagonalt) vinner.\n\nOm alla 9 rutor är fulla och det finns ingen vinnare avslutas spelet som oavgjort.\n(OK)\n"
            }}
        ]
    
    print('Welcome to Tic Tac Toe!')
    chosen_language = input('Chose language:\n(Eng/Swe)\n')
    
    while chosen_language not in valid_languages:
        x = input('Invalid answere, please try again:\n(Eng/Swe)\n')
        chosen_language = x.lower()
    
    #clear_output()
    while chosen_language != valid_languages[language_index]:
        language_index += 1
    else:
        checker = valid_languages[language_index]
        choice = languages[language_index][checker]
        print(languages[language_index][checker]['choice'])
        
        
    return choice



def game_start(language):
    xo = ['X','x','O','o']
    sr = ['S', 's', 'R', 'r']
    
    
    player1 = input(language['player1'])
    

    while player1 not in xo:
        player1 = input(language['invalid_input'])


    if player1 in xo[0:2]:
        player2 = 'O'
    else:
        player2 = 'X'
        
    
    _ = language['chosen_mark']
    chosen_mark = _.replace('_', player1.upper())
    print(chosen_mark)

    if player1 in xo:
        start_rules = input(language['start_rules'])

        while start_rules not in sr:
            start_rules = input(language['invalid_start_rules'])

    if start_rules in sr[0:2]:
        pass
    elif start_rules in sr[2:4]:
        _ = language['rules']
        __ = _.replace('_', player1.upper())
        rules = __.replace('^', player2.upper())
        start_rules = input(rules)

    return player1.upper()


lang = choose_language()

test = game_start(lang)