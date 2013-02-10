'''
Scripts for session 4
'''

import requests, getpass, datetime, sys
from collections import Counter
from dateutil import parser
from pandas import Series, DataFrame

'''Provides a prompt for writing a password'''
def getPassword():
    try:
        password = getpass.getpass()
        return password
    finally:
        del password
 
''' Retrieves repositories from Github'''
def getRepos(username, password):
    try:
        users = requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(username, password))
        users_data = users.json()
        return users_data
    finally:
        del password
    
''' Retrieves commit data from Github'''
def getCommits(username, password):  
    try:
        commit_data = []
        repos = getRepos(username, password)
        for i in range(len(repos)):
            name = repos[i][u'full_name']
            data = requests.get("https://api.github.com/repos/" + name + "/commits", auth=(username, password))
            commit_data.append(data.json())
        return commit_data
    finally:
        del password
        
''' Returns commit information in a DataFrame'''        
def commitsToDataFrame(username):
    try:
        password = getPassword()
        commits = getCommits(username, password)
        repos = getRepos(username, password)
    finally:
        del password
    d = dict()
    for i in range(len(commits) - 1):
        dates = []
        messages = []
        for j in range(len(commits[i])):
            raw_time = commits[i][j][u'commit'][u'committer'][u'date']
            datetime = parser.parse(raw_time)
            dates.append(datetime)
            message = commits[i][j][u'commit'][u'message']
            messages.append(message)
        s = Series(messages, index=dates, name=repos[i][u'full_name'])
        d.update({s.name : s})
    df = DataFrame(d)
    return df

''' Computes most common weekday and hour for commits. Input is a DataFrame'''
def commonTimes(df):
    weekdays = Counter()
    hours = Counter()
    for i in range(len(df.index)):
        date = df.index[i]
        weekdays.update([date.weekday()])
        hours.update([date.hour])
    most_common_day = weekdays.most_common()
    most_common_day = most_common_day[0][0]
    most_common_hour = hours.most_common()
    most_common_hour = most_common_hour[0][0]
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
    print "The most common weekday is " + str(day_names[most_common_day]) + " and the most common hour is " + str(most_common_hour) + "."
    return [most_common_day, most_common_hour]

    
            