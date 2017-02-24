# coding: UTF-8
# author: huisong.li
# Date  : 02/10/2017

from datetime import datetime
import os

def fill(number):
    return str(number).zfill(2)

def count(off_time):
    clock = datetime.now()
    delta = off_time - clock
    while delta.total_seconds() > 0:
        clock = datetime.now()
        delta = off_time - clock
        print (delta, end = '\r')

def set_time():
    print ('INPUT OFF TIME')
    off_time = input().split(':')
    length = len(off_time)
    
    hour   = int(off_time[0]) if off_time[0] else 20
    minute = int(off_time[1]) if length > 1  else 0
    second = int(off_time[2]) if length > 2  else 0
    
    today = datetime.now()
    
    return datetime(today.year, today.month, today.day,
                    hour      , minute     , second)

def main():
    os.system('cls')
    try:
        count(set_time())
    except KeyboardInterrupt:
        print('\nOFF DUTY EARLY\n')

if __name__ == '__main__':
    main()
