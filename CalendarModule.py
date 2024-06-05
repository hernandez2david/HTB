#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
#You are given a date. Your task is to find what the day is on that date.

import calendar

in_date = input()
#Input format is: 08 05 2015

in_date = in_date.split()
#Remove leading zeroes
in_date = [ele.lstrip('0') for ele in in_date]

#Converts str to int
in_date = [eval(i) for i in in_date]

#Use the calendar function to return the index of day of the week
index_day = calendar.weekday(in_date[2], in_date[0], in_date[1])

#create a list with the all days and their indexes 
list_days = calendar.day_name

#prints the day of the week
print(list_days[index_day].upper())
