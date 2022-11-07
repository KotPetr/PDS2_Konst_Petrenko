import sys

def month_name(month_num):
    months = {1: 'January',2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    try:
        return months[month_num]
    except KeyError:
        print('Invalid month_name(num) argument. Int number in range from 1 to 12 expected.', file=sys.stderr)
        return 'Some month'


print(month_name(4))
print(month_name(15))
print(month_name('gg'))
