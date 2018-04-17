import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    """
    init dictionary
    """
    DIC_CITY = {'a': 'chicago',
                'b': 'new york city',
                'c': 'washington'
                }

    DIC_MONTH = {'all': 'all',
                 '1': 'January',
                 '2': 'February',
                 '3': 'March',
                 '4': 'April',
                 '5': 'May',
                 '6': 'June',
                 '7': 'July',
                 '8': 'August',
                 '9': 'September',
                 '10': 'October',
                 '11': 'November',
                 '12': 'December'
                 }

    DIC_DAY = {'all': 'all',
               '1': 'Monday',
               '2': 'Tuesday',
               '3': 'Wednesday',
               '4': 'Thursday',
               '5': 'Friday',
               '6': 'Saturday',
               '7': 'Sunday'
               }

    '''
    init return values
    '''
    city = ''
    month = ''
    day = ''

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input_is_correct = False
    month_input_is_correct = False
    city_input = input(
        '''
Please input the city which you like 
    a : chicago
    b : new york city
    c : washington
'''
    )
    city_input_is_correct = (city_input == 'a') or (
        city_input == 'b') or (city_input == 'c')
    while city_input_is_correct == False:
        city_input = input(
            '''
Sorry!! You entered an wrong input !! Please input again!!
    a : chicago
    b : new york city
    c : washington
'''
        )
        city_input_is_correct = (city_input == 'a') or (
            city_input == 'b') or (city_input == 'c')

    city = DIC_CITY[city_input]
    print('You selected city: {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = input(
        '''
Please input the month which you like 
    all : all month
    1 : January
    2 : February
    3 : March
    4 : April
    5 : May
    6 : June
'''
    )

    month_input_is_correct = (month_input == 'all') or (
        month_input.isdigit() and int(month_input) >= 1 and int(month_input) <= 6)

    while month_input_is_correct == False:
        month_input = input(
            '''
Sorry!! You entered an wrong input !! Please input again!!
    all : all month
    1 : January
    2 : February
    3 : March
    4 : April
    5 : May
    6 : June
'''
        )
        month_input_is_correct = (month_input == 'all') or (
            month_input.isdigit() and int(month_input) >= 1 and int(month_input) <= 6)
    if(month_input == 'all'):
        month = 'all'
    else:
        month = DIC_MONTH[month_input]
    print('You selected month: {}'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
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

    day_input_is_correct = (month_input == 'all') or (
        month_input.isdigit() and int(month_input) >= 1 and int(month_input) <= 6)

    while month_input_is_correct == False:
        month_input = input(
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
        month_input_is_correct = (month_input == 'all') or (
            month_input.isdigit() and int(month_input) >= 1 and int(month_input) <= 6)
    if(month_input == 'all'):
        month = 'all'
    else:
        month = DIC_MONTH[month_input]
    print('You selected month: {}'.format(month))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    print('*'*32)
    print(df['month'].min())
    print('*'*32)
    print(df['day_of_week'].min())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[(df.month==month)]
        # print('*'*32)
        # print(df)

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day)
        df = df[(df.day_of_week==day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # TO DO: display the most common day of week

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used end station

    # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # TO DO: Display counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
