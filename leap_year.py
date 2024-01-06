#1 cheak leap year
year=int(input("please enter an year:"))
def chekLeap(year):
    if year%4==0  or year%400==0 and not year%100:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')

chekLeap(year)
