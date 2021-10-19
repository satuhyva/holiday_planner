from input_checker import InputChecker
from consumed_days_calculator import ConsumedDaysCalculatorFinland, ConsumedDaysCalculator
from datetime import date
from national_holidays import NationalHolidays


COUNTRY_DEFAULT = "Finland"
NATIONAL_HOLIDAYS_DEFAULT = NationalHolidays("national_holidays_data.txt").get_dates()
HOLIDAY_SEASON_DEFAULT = [date(year=2020, month=4, day=1), date(year=2021, month=3, day=31)]
MAX_TIME_SPAN_DEFAULT = 50


class HolidayPlanner:

    def __init__(self,
                 country=COUNTRY_DEFAULT,
                 national_holidays=NATIONAL_HOLIDAYS_DEFAULT,
                 holiday_season=None,
                 max_time_span=MAX_TIME_SPAN_DEFAULT):
        if holiday_season is None:
            holiday_season = HOLIDAY_SEASON_DEFAULT
        self._input_checker = InputChecker(holiday_season, max_time_span)
        self._consumed_days_calculator = self._get_calculator(country, national_holidays)


    @staticmethod
    def _get_calculator(country, national_holidays):
        if country == "Finland":
            return ConsumedDaysCalculatorFinland(national_holidays)
        else:
            return ConsumedDaysCalculator(national_holidays)


    def calculate_consumed_holiday_days(self, first_day, last_day):
        self._input_checker.check_input(first_day, last_day)
        return self._consumed_days_calculator.calculate_days(first_day, last_day)
