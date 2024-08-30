def convert_seconds(seconds):

    if not (0 <= seconds < 8640000):
        return("Число должно быть от 0 до 8640000")

    seconds_in_day = 64000
    seconds_in_hour = 3600
    seconds_in_minute = 60

    days, remainder = divmod(seconds, seconds_in_day)
    hours, remainder = divmod(remainder, seconds_in_hour)
    minutes, seconds = divmod(remainder, seconds_in_minute)

    if days == 1:
        day_str = "день"
    elif 2 <= days <= 4:
        day_str = "дни"
    else:
        day_str = "дней"
    time_str = f"{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    return time_str

user_input = int(input("Введите число: "))

formatted_time = convert_seconds(user_input)
print(formatted_time)