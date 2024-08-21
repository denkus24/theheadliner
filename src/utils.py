from datetime import datetime


def convert_to_timestamp(time_str: str):
    """Function for converting date to timestamp"""
    time_str_cleaned = ' '.join(time_str.split()[:-1])
    dt = datetime.strptime(time_str_cleaned, "%a, %d %b %Y %H:%M:%S")
    timestamp = int(dt.timestamp())

    return timestamp

def max_date(entries: list):
    """Function to find the highest date from a list of entries"""
    max_timestamp = 0
    for entry in entries:
        if convert_to_timestamp(entry.published) > max_timestamp:
            max_timestamp = convert_to_timestamp(entry.published)
    return max_timestamp
