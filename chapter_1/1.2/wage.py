#!/usr/bin/env python
'''Determine a weekly paycheck given rate,
hours worked, and overtime hours worked.
Assumes overtime rate = normal rate * 1.5
'''


class Wage:
    '''Wage class to calculate paycheck.'''
    def __init__(self, rate, hours, over_hours):
        self.rate = rate
        self.hours = hours
        self.over_rate = (rate * 1.5)
        self.over_hours = over_hours

    def calc(self):
        '''Method to calculate wage.'''
        return (self.rate * self.hours) + (self.over_rate * self.over_hours)


def main():
    '''Gets input and puts results on the screen.'''
    try:
        rate = float(input("Hourly Rate: "))
        hours = float(input("Hours Worked: "))
        over_hours = float(input("Overtime Hours Worked: "))
        this_wage = Wage(rate, hours, over_hours)
        print('%.2f' % this_wage.calc())
    except ValueError:
        print("That doesn't look like a number. Try again.")
        main()


if __name__ == '__main__':
    main()
