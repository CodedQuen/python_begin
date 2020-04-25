class Bird(object):
    def __int__(self):
        self.hungry = 1
    def eat(self):
        if self.hungry:
            print ('Aaah...')
            self.hungry = 0
        else:
            print('No, Thanks!')


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
