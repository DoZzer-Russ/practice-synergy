from functions import (
    get_birthday,
    get_day_of_week,
    is_leap_year,
    calculate_age,
    print_digits
)

print(
    f'Введите дату вашего рождения и вы узнаете:\n'
    f'- К какому дню недели соответствует ваш день рождения.\n'
    f'- Високосный был год, или нет.\n'
    f'- Сколько сейчас вам лет.\n'
    f'- Так же появится электронное табло с датой вашего рождения.'
)
print('-'*65)

day = get_birthday('Введите день от (1 - 31): ', 1, 31)
month = get_birthday('Введите месяц от (1 - 12): ', 1, 12)
year = get_birthday('Введите год (пример: 1999): ', 1000, 9999)

day_of_week = get_day_of_week(day, month, year)
leap_result = is_leap_year(year)
age = calculate_age(day, month, year)


print('-'*65)
print(f'День недели: {day_of_week}.')
print(f'{leap_result}')
print(f'Ваш возраст: {age}')
print('-'*65)
print_digits(f'{day:02d}.{month:02d}.{year}')
print('-'*65)
