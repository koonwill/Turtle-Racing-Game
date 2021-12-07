import turtle


class Player_Account:
    def __init__(self, name):
        self.name = name
        self.selected = None

    def __repr__(self):
        return f'Player("{self.name}")'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, (str)):
            raise TypeError('Name must be string')
        if name == "":
            raise ValueError("Name musn't empty")
        self.__name = name

    def select_turtle(self, all_color):

        while True:

            color = turtle.Screen().textinput(title="Make your bet!",
                                            prompt=f"{self.name}'s turn\nWhich turtle do you think will win? Enter a colour: ").lower()
            if color in all_color:
                break
            print('Invalid color')

        self.selected = color
