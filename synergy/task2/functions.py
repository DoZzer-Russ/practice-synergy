import calendar
from datetime import datetime


def get_birthday(number, min_num, max_num):
    while True:
        try:
            value = int(input(number))
            if min_num <= value <= max_num:
                return value
            else:
                print(
                    f'Вы ввели недопустимое значение. Введите число от {min_num} до {max_num}.')
        except ValueError:
            print('Вы ввели не число. Попрбуйте еще раз.')


def get_day_of_week(day, month, year):
    user_date = datetime(year, month, day)
    week_day = user_date.weekday()

    days = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    ]
    return days[week_day]


def is_leap_year(year):
    if calendar.isleap(year):
        years = 'Это был високосный год.'
    else:
        years = 'Это был не високосный год.'
    return years


def calculate_age(day, month, year):
    user_date = datetime(year, month, day)
    today = datetime.now()

    age = today.year - user_date.year
    if today.month < user_date.month:
        age -= 1
    elif today.month == user_date.month and today.day < user_date.day:
        age -= 1

    year_1 = [1]
    year_2_4 = [2, 3, 4]
    year_0_5_9 = [0, 5, 6, 7, 8, 9]
    year_11_14 = [11, 12, 13, 14]

    last_one = age % 10
    last_two = age % 100

    if last_two in year_11_14:
        return f'{age} лет.'
    elif last_one in year_1:
        return f'{age} год.'
    elif last_one in year_2_4:
        return f'{age} года.'
    elif last_one in year_0_5_9:
        return f'{age} лет.'


digits = {
    '0': [
        ' *** ',
        '*   *',
        '*  **',
        '* * *',
        '**  *',
        '*   *',
        ' *** '
    ],

    '1': [
        '  ** ',
        ' * * ',
        '*  * ',
        '   * ',
        '   * ',
        '   * ',
        '*****'
    ],

    '2': [
        ' *** ',
        '*   *',
        '    *',
        '   * ',
        '  *  ',
        ' *   ',
        '*****'
    ],

    '3': [
        ' *** ',
        '*   *',
        '    *',
        ' *** ',
        '    *',
        '*   *',
        ' *** '
    ],

    '4': [
        '   **',
        '  * *',
        ' *  *',
        '*   *',
        '*****',
        '    *',
        '    *'
    ],

    '5': [
        '*****',
        '*    ',
        '*    ',
        '**** ',
        '    *',
        '    *',
        '**** '
    ],

    '6': [
        ' *** ',
        '*   *',
        '*    ',
        '**** ',
        '*   *',
        '*   *',
        ' *** '
    ],

    '7': [
        '*****',
        '    *',
        '    *',
        '   * ',
        '  *  ',
        '  *  ',
        '  *  '
    ],

    '8': [
        ' *** ',
        '*   *',
        '*   *',
        ' *** ',
        '*   *',
        '*   *',
        ' *** '
    ],

    '9': [
        ' *** ',
        '*   *',
        '*   *',
        ' ****',
        '    *',
        '*   *',
        ' *** '
    ],

    '.': [
        '   ',
        '   ',
        '   ',
        '   ',
        '   ',
        '   ',
        ' * '
    ]
}


def print_digits(number):
    number_str = str(number)

    digits_patterns = []
    for patterns in number_str:
        digits_patterns.append(digits[patterns])

    for row in range(7):
        line = ''
        for pattern in digits_patterns:
            line += pattern[row] + '  '
        print(line)
