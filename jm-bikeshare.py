import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    """
    while loops are being used in combination with if conditions in order to handle the         cases where the user input is invalid
    """

    cities = ('chicago', 'new york city', 'washington')
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\n Which city would you like to draw the data from:\n chicago, new york city or washington? ').lower()
        if city in cities:
            print('\n You chose the following city: ', city)
            break
        else:
            print('\n Oops, looks like you have not chosen one of the aforementioned cities!')

# get user input for month (all, january, february, ... , june)

    while True:
        month = input('\n Please choose a month from january to june that you would like to filter by\n alternatively you can choose all: ').lower()
        if month in months:
            print('\n You chose: ', month)
            break
        else:
            print('\n Oops, looks like the month you chose is not within the abovementioned range!')

# get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\n Which weekday would you like to filter by?\n alternativeley you can choose all: ').lower()
        if day in days:
            print('\n You chose: ', day)
            break
        else:
            print('\n Oops, looks like you have not chosen one of the available options!')

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    mc_month = df ['month'].mode()[0]# TO DO: display the most common month

    mc_day_of_week = df['day_of_week'].mode()[0] # TO DO: display the most common day of         week

    df['Start Hour'] = df['Start Time'].dt.hour
    mc_hour = df['Start Hour'].mode()[0]# TO DO: display the most common start hour
    print("Most common month (as an int.): {}\nMost common day of week: {}\nMost common start hour: {}\n".format(mc_month, mc_day_of_week, mc_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    mc_start_station = df['Start Station'].mode()[0] # TO DO: display most commonly used         start station

    mc_end_station = df['End Station'].mode()[0] # TO DO: display most commonly used end         station

    com_strt_end = df['Start Station'] + ' - ' + df['End Station'] # TO DO: display most         frequent combination of start station and end station trip
    frq_com_strt_end = com_strt_end.mode()[0]
    print("The most commonly used start station was: {}\nThe most commonly used end station was: {}\nThe most frequent combination of start and end stations was: {}\n".format(mc_start_station, mc_end_station, frq_com_strt_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    tot_travel_time = df['Trip Duration'].sum()# TO DO: display total travel time
    print('The total travel time was: ', tot_travel_time)

    avg_travel_time = df['Trip Duration'].mean() # TO DO: display mean travel time
    print('The average travel time was: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    A try statement is used to take account of the fact that there are no data on gender         and birth year available for washington.

    The birth year stats are converted into integers.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        cnt_user_type = df['User Type'].value_counts() # Display counts of user types
        print('Those are the counts of the different user types:\n ', cnt_user_type)
        cnt_gender = df['Gender'].value_counts()# Display counts of gender
        print('Those are the counts of the different gender:\n ', cnt_gender)
# Display earliest, most recent, and most common year of birth
        earl_year = df['Birth Year'].min()
        int_earl_year = int(earl_year)
        print('The earliest birth year is:', int_earl_year)
        mst_recent = df['Birth Year'].max()
        int_mst_recent = int(mst_recent)
        print('The most recent birth year is: ', int_mst_recent)
        mst_common = df['Birth Year'].mode()[0]
        int_mst_common = int(mst_common)
        print('The most common birth year is: ', int_mst_common)

    except KeyError:
        print('There are no data available on gender and birth year in washington')

    while True:
        ind_data = input('Would you like to see some individual raw Data? ')
        if ind_data == 'yes':
            rand_sam = df.sample(n=5)
            print(rand_sam)
        elif ind_data == 'no':
            break

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
