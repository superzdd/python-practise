DIC_DAY = {'all': 'all',
               '1': 'Monday',
               '2': 'Tuesday',
               '3': 'Wednesday',
               '4': 'Thursday',
               '5': 'Friday',
               '6': 'Saturday',
               '7': 'Sunday'
               }
day_input = input(
        '''
Please input the day which you like 
    all: all day
    1: Monday,
    2: Tuesday,
    3: Wednesday,
    4: Thursday,
    5: Friday,
    6: Saturday,
    7: Sunday
'''
    )

day_input_is_correct = (day_input == 'all') or (
    day_input.isdigit() and int(day_input) >= 1 and int(day_input) <= 6)

while day_input_is_correct == False:
    day_input = input(
        '''
Sorry!! You entered an wrong input !! Please input again!!
all: all day
1: Monday,
2: Tuesday,
3: Wednesday,
4: Thursday,
5: Friday,
6: Saturday,
7: Sunday
'''
    )
    day_input_is_correct = (day_input == 'all') or (
        day_input.isdigit() and int(day_input) >= 1 and int(day_input) <= 7)
if(day_input == 'all'):
    day = 'all'
else:
    day = DIC_DAY[day_input]
print('You selected day: {}'.format(day))