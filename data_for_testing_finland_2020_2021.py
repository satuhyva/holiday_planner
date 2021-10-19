from datetime import date, timedelta


def get_data_around_christmas():
    start_date = date(year=2020, month=12, day=21)
    counts = [1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 8, 8, 8, 9, 10, 10, 12, 13, 13, 13, 14]
    correct_date_count_pairs = []
    for i in range(0, len(counts)):
        day = start_date + timedelta(days=i)
        correct_date_count_pairs.append([day, counts[i]])
    return correct_date_count_pairs


def get_data_around_new_year():
    start_date = date(year=2020, month=12, day=29)
    counts = [1, 2, 3, 3, 3, 3, 4, 6, 6, 7, 8, 8, 8, 9, 10, 12, 13, 14, 14, 14, 15, 16]
    correct_date_count_pairs = []
    for i in range(0, len(counts)):
        day = start_date + timedelta(days=i)
        correct_date_count_pairs.append([day, counts[i]])
    return correct_date_count_pairs


def get_data_around_easter():
    start_date = date(year=2020, month=4, day=7)
    counts = [1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 8, 8, 9, 10, 12, 13, 14]
    correct_date_count_pairs = []
    for i in range(0, len(counts)):
        day = start_date + timedelta(days=i)
        correct_date_count_pairs.append([day, counts[i]])
    return correct_date_count_pairs


def get_data_around_may():
    start_date = date(year=2020, month=5, day=1)
    counts = [0, 0, 0, 1, 2, 3, 4, 6, 6, 6, 7, 8, 9, 10, 12, 12, 12, 13, 14, 15, 15, 16]
    correct_date_count_pairs = []
    for i in range(0, len(counts)):
        day = start_date + timedelta(days=i)
        correct_date_count_pairs.append([day, counts[i]])
    return correct_date_count_pairs


