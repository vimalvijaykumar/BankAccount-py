import sys
import random
from enum import Enum
def rps(name='playerone'):
    game_count=0
    player_wins=0
    python_wins=0
    
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
                    ROCK = 1
                    PAPER = 2
                    SCISSOR = 3

        playerchoice=int(input(f'\n{name}....\n1 for rock \n2for paper \n3 for scissor\n'))
        if playerchoice not in [1,2,3]:
                print(f'{name} must enter 1,2,3')
                return play_rps()
    
        print("")
        computerchoice=int(random.choice("123"))
        print('')
        print(f"{name} chose😍: {str(RPS(playerchoice)).replace('RPS.',' ')}.")
        print(f"python chose🐍: {str(RPS(computerchoice)).replace('RPS.'," ")}.") 
        print('')
        def decide_winners(playerchoice,computerchoice):
                nonlocal player_wins
                nonlocal python_wins
                if playerchoice ==1 and computerchoice ==3 :
                    player_wins+=1
                    return f'{name} win🍷'
                elif playerchoice==2 and computerchoice ==1 :
                    player_wins+=1
                    return f"{name} win🍷"
                elif playerchoice ==3 and computerchoice ==2 :
                    player_wins+=1
                    return f"{name} win🍷"         
                elif playerchoice== computerchoice :
                    return "tie"
                else:
                    python_wins+=1
                    return "🐍python wins"
                  
        result = decide_winners(playerchoice,computerchoice)
        print(result)
        print('')
        nonlocal game_count
        game_count+=1
        print(f"Game_count:{str(game_count)}")
        print(f"\nPlayer_count:{str(player_wins)}")
        print(f"\nPyhton wins:{str(python_wins)}")
        print("\nplay again"f"{name}")
        while True: 
              print('')
              playagain=input("\n Y for yes or Q for quit:")
              if playagain.lower() not in ['y','q']:
                    continue
              else:
                    break
              
        if playagain.lower() == "y":
              return play_rps()
        else:
              print("\n💥💥💥")
              print('Thankyou for playing!\n')
              sys.exit("bye👋!")
    return play_rps



if __name__=="__main__":
        import argparse
        parser= argparse.ArgumentParser(
            description="provides a personalized game experience"
        )
        parser.add_argument(
        "-user","--user",metavar="name",required=True,help="the name of provider"
        )
        args=parser.parse_args()

        rock_paper_scissor = rps(args.user)
        rock_paper_scissor()