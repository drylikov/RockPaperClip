# -*- coding: utf-8 -*-
#
#  rock_paper_clip.py
#
#  Created by LulzLoL231 on 2/23/20.
#
from random import choice

def Init():
    global game_player_scope, game_pc_scope, game_draws, game_items, game_rules, game_help, game_welcome
    game_player_scope, game_pc_scope, game_draws = 0, 0, 0
    game_items = ['rock', 'paper', 'clip']
    game_rules = 'The rock breaks the clip, the clip cut the paper, the paper is placed on the rock. Sounds simple, right?'
    game_help = 'Use "rock", "paper" or "clip" for try win. Use "rules" for Rules & "exit" for... exit.'
    game_welcome = 'Welcome to "rock, paper & clip" game!'

def WhoWin(player_item, pc_item):
    if player_item == pc_item:
        return 'draw'
    elif player_item == 'rock':
        if pc_item == 'paper':
            return 'pc'
        else:
            return 'player'
    elif player_item == 'paper':
        if pc_item == 'rock':
            return 'pc'
        else:
            return 'player'
    elif player_item == 'clip':
        if pc_item == 'rock':
            return 'pc'
        else:
            return 'player'
    else:
        raise Exception('player_item or pc_item not in game_items!')

def Game():
    global game_player_scope, game_pc_scope, game_draws
    try:
        play = True
        print(game_welcome)
        print(game_help)
        while play is True:
            print()
            print(f'Current scope: {str(game_player_scope)}:{str(game_pc_scope)}:{str(game_draws)}')
            player_item = input('[?] Rock, paper or clip: ').lower()
            print()
            pc_item = choice(game_items)
            if player_item in game_items:
                win = WhoWin(player_item, pc_item)
                if win == 'draw':
                    print('It\'s a DRAW!')
                    game_draws += 1
                    continue
                elif win == 'pc':
                    print('PC win!')
                    game_pc_scope += 1
                    continue
                elif win == 'player':
                    print('You win!')
                    game_player_scope += 1
                    continue
                else:
                    print('HOW YOU DID IT!?')
                    raise Exception('Out from loop.')
            else:
                if player_item == 'exit':
                    if game_player_scope > game_pc_scope:
                        print(f'You did it! You won PC with scope: {str(game_player_scope)}:{str(game_pc_scope)}. Draws: {str(game_draws)}')
                    elif game_player_scope < game_pc_scope:
                        print(f'So sad! You lose to PC with scope: {str(game_pc_scope)}:{str(game_player_scope)}. Draws: {str(game_draws)}')
                    elif game_draws > 0:
                        print(f'It\'s a draw... Scope: {str(game_player_scope)}:{str(game_pc_scope)}:{str(game_draws)}')
                    else:
                        print('You don\'t play!')
                    play = False
                elif player_item == 'rules':
                    print(game_rules)
                    continue
                elif player_item == 'help':
                    print(game_help)
                    continue
                else:
                    print('ONLY "rock", "paper" & "clip"!')
                    continue
    except KeyboardInterrupt as e:
        pass
    except NameError as e:
        print('[!] Do "Init" please!')
        raise e
    except Exception as e:
        print('Houston we have a problem!')
        raise e
    print('It was be a nice game, bye & have a nice day! ^^')
    if __name__ == '__main__':
        exit()

if __name__ == '__main__':
    Init()
    Game()
