#Udacity-Misk second project in nd of "Programming for data science with python"
#version 2: changes made based on udacity feedback

import time
import pandas as pd
import numpy as np

# Here we make a dataframe of all three files 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def display_raw_data(df):
    """ Ask user wether to display 5 rows of the dataframe or not 
        Function returns: df
    """
    i = 0
    raw = str(input("Would you like to see raw data? Type Yes or No:\n").strip().lower())
    
    while True:
        if raw not in ("yes", "no"):
            raw = str(input("Your input is invalid!, please Type Yes or No:\n").strip().lower())
        else:
            break
    
    pd.set_option('display.max_columns',None) # show all columns
    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i : i + 5])# TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = str(input("Would you like to see 5 MORE rows of raw data? Type Yes or No:\n").strip().lower())
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").strip().lower()
    return df


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
    city = str(input("Which city do you want to analyse? chicago, new york city or washington\n")).strip().lower()
    
    while True:
        if city not in ("chicago", "new york city","washington"):
            city = str(input("Your input is invalid, please choose: chicago, new york city or washington\n")).strip().lower()
        else:
            break
            

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("Which month? all, january, febryuary, march, april, may or june?\n")).strip().lower()
    
    while True:
        if month not in ("all", "january", "febryuary", "march", "april", "may", "june"):
            month = str(input("Your input is invalid, please choose: all, january, febryuary, march, april, may or june?\n")).strip().lower()
        else:
            break

        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Which day? all, monday, tuesday, wednsday, thursday, friday, saturday or sunday\n")).strip().lower()
    
    while True:
        if day not in ("all", "monday", "tuesday", "wednsday", "thursday", "friday", "saturday","sunday"):
             day = str(input("Your input is invalid, please choose: all, monday, tuesday, wednsday, thursday, friday, saturday or sunday\n")).strip().lower()
        else:
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
  # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour # we need this later
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # TO DO: display the most common month
    mostCommonMonth = df['month'].mode()[0]
    print("\nMost common month:\n{}".format(mostCommonMonth))
    
    # TO DO: display the most common day of week
    mostCommonDay = df['day_of_week'].mode()[0]
    print("\nMost common day_of_week:\n{}".format(mostCommonDay))
    
    # TO DO: display the most common start hour
    mostCommonHour = df['hour'].mode()[0]
    print("\nMost common start hour:\n{}".format(mostCommonHour))
    
    print("\nThis took %s seconds." % "{:.7f}".format(time.time() - start_time))
    print('-'*40)
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostPopularstartStation = df['Start Station'].mode()[0]
    print("\nMost commonly used Start station:\n{}".format(mostPopularstartStation))
    
    # TO DO: display most commonly used end station
    mostPopularENDStation = df['End Station'].mode()[0]
    print("\nMost commonly used end station:\n{}".format(mostPopularENDStation))

    # TO DO: display most frequent combination of start station and end station trip
    mostPopularTrip = df.groupby(['Start Station','End Station']).size().idxmax() # we can also use mode()[0] here
    #mostPopularTrip = ("Station: " + df['Start Station'] + ', and station: ' + df['End Station']).mode()[0] ---another way to do this
    print("\nMost frequent combination of start station and end station trip:\n{}".format(mostPopularTrip))
    
    print("\nThis took %s seconds." % "{:.7f}".format(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time in days, hours, minues and seconds
    totalTravelTime = df['Trip Duration'].sum()
    # print("\nTotal travel time:\n %s seconds" % (totalTravelTime).round()) --- all in seconds
    print("%s Days" % int(totalTravelTime/86400) +", "+ "%s Hours" % int((totalTravelTime%86400)/3600)+", "+"%s Minutes" % int(((totalTravelTime%86400)%3600)/60) +" and "+"%s Seconds" % int(((totalTravelTime%86400)%3600)%60))

    # TO DO: display mean travel time in seonds
    meanTravelTime = df['Trip Duration'].mean()
    print("\nMean travel time:\n %s seconds" % (meanTravelTime).round())



    print("\nThis took %s seconds." % "{:.7f}".format(time.time() - start_time))
    print('-'*40)


def user_stats(df,city): #added city as argument because the columns differ in the three cities' dataframes 
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userCounts = df['User Type'].value_counts()
    print("\nCounts of user types:\n{}".format(userCounts))
    
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
        genderCounts = df['Gender'].value_counts()
        print("\nCounts of gender:\n{}".format(genderCounts))
        
        earliestYear = int(df['Birth Year'].min())
        print("\nEarliest year of birth:\n{}".format(earliestYear))
        
        recentYear = int(df['Birth Year'].max())
        print("\nRecent year of birth:\n{}".format(recentYear))
        
        mostFrequentYear = int(df['Birth Year'].value_counts().idxmax())
        print("\nMost frequent year of birth:\n{}".format(mostFrequentYear))
    


    print("\nThis took %s seconds." % "{:.7f}".format(time.time() - start_time))
    print('-'*40)


def main(): # main function where we call all other functions
    while True:
                  
                  
        city, month, day = get_filters() # what did the user select
        df = load_data(city, month, day)
        df = display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while True:
            if restart not in ("yes", "no"):
                restart = str(input("Your input is invalid!, please Type Yes or No:\n").strip().lower())
            else:
                break
        if restart.lower() != 'yes':
            break
            


            
if __name__ == "__main__":
	main()
