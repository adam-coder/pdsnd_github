import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to see data for Chicago, New York City, or Washington? -> ').lower()
        if city in CITY_DATA.keys():    
            # uses city_data to find matching keys in dictionary
            break
        else:
            print('That\'s not a vaild city, please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like explore?\n january, february, march, april, may, june, or all -> ').lower()
        if month in months:
            # uses the index of the months list to get matching index
            break
        else:
            print('That\'s not a vaild month, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to explore?\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all -> ').lower()
        if day in days:
            # uses the index of the days list to get matching index
            break
        else:
            print('That\'s not a vaild day of week, Try again')

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
    # loading data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1 
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)
    
    # Display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    weekday_name = df['weekday_name'].mode()[0]
    print('Most common day of week: ', weekday_name)

    # Display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', start_station)
    
    # Display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', end_station)

    # Display most frequent combination of start station and end station trip
    df['frequent_starstop'] = df['Start Station'] + 'from' + df['End Station']
    print('Most frequent start and stop station: ', df.frequent_starstop.mode().iloc[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_time)
    
    # Display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Types:', user_types)
    
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('Count of Gender Type:', gender_types)
    else:
        print('Sorry, no data to show')
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('Oldest Year of birth date:', earliest_year)
    
        recent_year = df['Birth Year'].max()
        print('Youngest Year of birth date:', recent_year)

        common_year = df['Birth Year'].mode()
        print('Most common Year of birth:', common_year) 
    else:
        print('Sorry, no data to show')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def more_data(df):
    """"Ask the user if they would like to see 5 rows of raw data. """
    # Asks user if they would like to veiw five rows of data
    more_data = input('Would you like to see 5 rows of data? (yes or no)\n').lower()
    if more_data == 'yes':
        # checks user input for string value 
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            five_more = input('Would you like to see more!!? (yes or no)\n').lower()
            if five_more != 'yes':
                # checks user input for sting value
                break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()