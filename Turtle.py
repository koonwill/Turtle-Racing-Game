import random
import turtle
import time
from database import Database
from Player_Account import Player_Account

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'purple', 'pink', 'black']


class Game:
    def __init__(self, name_list):
        "Initialize"
        self.screen = turtle.Screen()
        self.database = Database()
        self.turtle_list = []
        self.color = COLORS[:self.get_number_of_racers()]
        self.player_list = [Player_Account(name) for name in name_list]
        self.painter = turtle.Turtle()
        self.painter.hideturtle()
        self.screen_turtle()

    def get_number_of_racers(self):
        '''Get number of racer'''
        while True:
            racer = input('Enter the number of racers (2-5): ')
            if racer.isdigit():
                racer = int(racer)
            else:
                print('Input is not numeric... Please Try Again!')
                continue

            if 2 <= racer <= 5:
                print()
                return racer
            else:
                print('Number not in range 2-5... Please Try Again!')

    def screen_turtle(self):
        '''Setup the screen'''
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title('Turtle Racing!!')

    def race(self, colors):
        '''Let the race begin then return the winner'''
        self.create_turtle(colors)
        for player in self.player_list:
            player.select_turtle(self.color)

        # after select the turtle the race will start
        while True:
            cup_amount = self.special_round()
            for racer in self.turtle_list:
                distance = random.randrange(1, 20)
                racer.forward(distance)
                if racer.ycor() >= HEIGHT // 2 - 10:  # check the winner
                    winner = colors[self.turtle_list.index(racer)]

                    for player in self.player_list:
                        if player.selected == winner:
                            print(f'{player.name} win the bet {player.selected}')
                            self.database.update_score(player.name, 1)

                        else:
                            print(f"{player.name} lost the bet, {player.selected} didn't win")
                            if cup_amount != 1:
                                print('*** SPECIAL ROUND!! ***')
                            print(f'{player.name} NEED TO DRINK {cup_amount} CUP')
                        print()

                    return

    def create_turtle(self, colors):
        '''Line a turtle at the start with spacing then append list of racer'''
        spacing_x_axis = WIDTH // (len(colors) + 1)

        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.speed(20)
            racer.left(90)
            racer.penup()
            racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x_axis, -HEIGHT // 2 + 20)
            racer.pendown()
            self.turtle_list.append(racer)

    def special_round(self):
        """This is special round that will randomly come
        which random multiply the amount of cup we need to drinks"""
        chance = random.randint(1, 1000)
        num_list = [1, 11, 111, 3, 33, 333, 5, 55, 555, 7, 77, 777, 9, 99, 999]
        return random.randint(2, 5) if chance in num_list else 1

    @staticmethod
    def show_rule():
        """Show rule of this game"""
        print('**************************** TURTLE RACING GAME *****************************')
        print('*** This game create to play within the party which need to drink if lose ***')
        print('*** So we highly recommend player to get the drinks ready.                ***')
        print('*****************************************************************************')
        print('Firstly, this game need player to select how many racer(turtle) player want.')
        print('After that the game will need player to select the racer by their color to make a bet')
        print('then the race will start and the player who lose the bet need to drink one cup.')
        print('But we thinks one cup is too easy so if player is very lucky the special round will appear')
        print('after the race end and the amount of cup that player need to drink will increase')
        print('')
        print('Have fun ;)')
        print('')

    def play_one_game(self):
        "Run one game"
        self.screen_turtle()
        random.shuffle(self.color)
        self.race(self.color)
        time.sleep(5)


def main():
    '''Main part'''
    print('*************************************')
    print('***Welcome to Turtle Racing Game!!***')
    print('*************************************')
    print('')
    while True:
        print('1.Play!!')
        print('2.Rule')
        print('3.Leaderboard')
        print('4.Quit')
        select_choice = input('Please enter the choice(1-4): ')
        print()
        if select_choice == '1':  # play the game
            name_list = []
            while True:
                print(f'now all player are: {name_list}')
                name = input('Enter name and press enter to start: ').capitalize()
                if name.lower() == '':
                    if name_list:
                        break
                    print('name cant be empty')
                    continue
                name_list.append(name)
            start = Game(name_list)  # insert namelist
            start.play_one_game()  # let race
            start.screen.clear()

        elif select_choice == '2':  # showrule
            Game.show_rule()

        elif select_choice == '3':  # show leader board
            data = Database()
            print('*** Leaderboard ***')
            print('name       score')
            for name, win in data.record():
                print(f'{name:<5} {win:>9}')
            print()

        elif select_choice == '4':  # exit with countdown
            print('Start Exit...')
            for countdown in range(3, 0, -1):
                print(f'Exit in {countdown}')
                time.sleep(1)
            print()
            break

        else:
            print('Invalid input please try again!!')
