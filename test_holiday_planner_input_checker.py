import unittest
from holiday_planner import HolidayPlanner
from national_holidays import NationalHolidays
from datetime import date, timedelta



class TestHolidayPlannerInputChecker(unittest.TestCase):

    def setUp(self):
        country = "Finland"
        national_holidays = NationalHolidays("national_holidays_data.txt").get_dates()
        holiday_season = [date(year=2020, month=4, day=1), date(year=2021, month=3, day=31)]
        self.planner = HolidayPlanner(country, national_holidays, holiday_season, 50)

    def test_dates_not_in_chronological_order_raises_exception(self):
        with self.assertRaises(Exception):
            time_later = date(year=2020, month=7, day=1)
            time_earlier = time_later - timedelta(days=1)
            self.planner.calculate_consumed_holiday_days(time_later, time_earlier)

    def test_start_date_not_within_holiday_season_raises_exception(self):
        with self.assertRaises(Exception):
            start_time = date(year=2020, month=3, day=31)
            end_time = date(year=2020, month=4, day=1)
            self.planner.calculate_consumed_holiday_days(start_time, end_time)

    def test_end_date_not_within_holiday_season_raises_exception(self):
        with self.assertRaises(Exception):
            start_time = date(year=2021, month=3, day=31)
            end_time = date(year=2021, month=4, day=1)
            self.planner.calculate_consumed_holiday_days(start_time, end_time)

    def test_time_span_not_within_allowed_limits_raises_exception(self):
        with self.assertRaises(Exception):
            time_earlier = date(year=2020, month=7, day=1)
            time_later = time_earlier + timedelta(days=50)
            self.planner.calculate_consumed_holiday_days(time_earlier, time_later)


if __name__ == '__main__':
    unittest.main()
