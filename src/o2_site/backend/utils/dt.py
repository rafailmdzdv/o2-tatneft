import datetime
import re


def get_date_and_time(date_time: str) -> tuple:
    secs_str = re.search(r'\..+', date_time).group()
    date_time = date_time.replace('T', ' ').replace(secs_str, '')
    converted_datetime = datetime.datetime.strptime(date_time,
                                                    '%Y-%m-%d %H:%M:%S')
    return converted_datetime.date(), converted_datetime.time()
