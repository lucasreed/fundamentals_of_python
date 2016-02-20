#! /usr/bin/env python
'''Determine the distance traveled by a bouncing ball
given the user input of initial height and how many bounces.
"bounciness index" assumed to be .6'''


class Ball:
    '''Create an instance of a ball at a certain height'''
    def __init__(self, height):
        '''Be the ball. Initialize the ball.'''
        self.init_height = height
        self.current_height = float(height)
        self.distance = 0.0
        self.bindex = 0.6

    def bounce(self, bounces):
        '''Calculate the distance after all the bounces'''
        while bounces > 0.0:
            next_bounce = self.current_height * self.bindex
            self.distance += self.current_height + next_bounce
            self.current_height = next_bounce
            bounces -= 1.0
        return self.distance


def main():
    '''Gets input and puts results on the screen.'''
    try:
        height = float(input("How high is the ball (in feet)? "))
        num_bounces = float(input("How many bounces should it take? "))
        new_ball = Ball(height)
        distance = new_ball.bounce(num_bounces)
        print("The distance traveled is: %.2f feet!" % distance)
    except ValueError:
        "You input something that isn't a number. Try again."
        main()


if __name__ == '__main__':
    main()
