class InputChecker:


    def __init__(self, holiday_season, max_time_span):
        self._holiday_season = holiday_season
        self._max_time_span = max_time_span


    def check_input(self, first_day, last_day):
        if last_day < first_day:
            raise Exception("Start date and end date must be in chronological order")
        if first_day < self._holiday_season[0]:
            raise Exception(f"Start date must not be earlier than season starts ({self._holiday_season['start']})")
        if last_day > self._holiday_season[1]:
            raise Exception(f"End date must not be later than season ends ({self._holiday_season['end']})")
        if (last_day - first_day).days + 1 > self._max_time_span:
            raise Exception(f"Maximum time span is {self._max_time_span} days")



