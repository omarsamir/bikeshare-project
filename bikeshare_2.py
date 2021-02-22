import time
import pandas as pd
import numpy as np
from pathlib import Path

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city','washington']
months = ['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
days = ['sat','sun','mon','tues','wed','thurs']
city, month, day = '','',''
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('Enter the name of the city to analyze (chicago, washington and new york city) \n')
       if city in cities:
           break
    print(CITY_DATA[city])
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the name of the month to filter by (jan, feb, mar, apr, may or june), or "all" to apply no month filter \n')
        if month in months or month == 'all':
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the name of the day of week to filter by (sat, sun, mon, tues, wed or thurs), or "all" to apply no day filter \n')
        if day in days or day == 'all':
            break

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
    # load needed city data
    script_location = Path(__file__).absolute().parent
    file_location = script_location / CITY_DATA[city]
    df = pd.read_csv(file_location)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month]

    if day != 'all':
        df = df[ df['day_name'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # display the most common month
  
    if len(df['month'].value_counts()) > 0:
        most_common_month = df['month'].mode().loc[0]
        print("The most common month is: " + months[most_common_month - 1])
    else:
        print("No data for the most common month")

    # display the most common day of week
    if len(df['day_name'].value_counts()) > 0:
        most_common_day_name = df['day_name'].mode().loc[0]
        print("The most common day is: " + most_common_day_name)
    else:
         print("No data for the most common day")

    # display the most common start hour
    if len(df['hour'].value_counts()) > 0:
        most_common_start_hour = df['hour'].mode().loc[0]
        print("The most common day is: " + str(most_common_start_hour))
    else:
         print("No data for the most common hour")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if  len(df['Start Station'].value_counts()) > 0:
        most_commonly_used_start_station = df['Start Station'].mode().loc[0]
        print("The most commonly used start station: " + most_commonly_used_start_station)
    else:
        print("No data for the most commonly used start station")

    # display most commonly used end station
    if len(df['End Station'].value_counts()) > 0:
        most_commonly_used_end_station = df['End Station'].mode().loc[0]
        print("The most commonly used end station: " + most_commonly_used_end_station)
    else:
        print("No data for the most commonly used end station")


    # display most frequent combination of start station and end station trip
    if len(df[['Start Station','End Station']].value_counts()) > 0:
        most_commonly_used_start_and_end_station = df[['Start Station', 'End Station']].mode().loc[0]
        print("\nResult of the most frequent combination of start station and end station trip: ")
        print(most_commonly_used_start_and_end_station)
    else:
        print("No data for the most commonly used end station")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: ", str(len(df['User Type'].dropna().unique())))

    # Display counts of gender
    if 'Gender' in df.columns and len(df['Gender'].value_counts()) > 0:
        print("Counts of gender: ", str(len(df['Gender'].dropna().unique())))
    else:
        print('No data for gender to display')

    # Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns and len(df['Birth Year'].value_counts()) > 0:

        # Earliest
        print("The most earliest birth year: ", str(int(df['Birth Year'].min())))

        # most recent
        print("The most recent birth year: ", str(int(df['Birth Year'].max())))

        # most common
        if len(df['Birth Year'].value_counts()) > 0:
            most_recent_year_of_birthday = df['Birth Year'].mode().loc[0]
            print("The most common birth year: ", str(int(most_recent_year_of_birthday)))
        else:
            print("No data for the most common birth year")
    else:
         print("No data for birth year to display")

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
