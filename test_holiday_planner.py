import unittest
from holiday_planner import HolidayPlanner
from national_holidays import NationalHolidays
from datetime import date, timedelta
from data_for_testing_finland_2020_2021 import get_data_around_christmas, get_data_around_new_year, get_data_around_easter, get_data_around_may



def perform_tests(self, test_data):
    start_date = test_data[0][0]
    for data_pair in test_data:
        end_date = data_pair[0]
        correct_days = data_pair[1]
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, end_date)
        self.assertTrue(calculated_days == correct_days)


class TestHolidayPlanner(unittest.TestCase):

    def setUp(self):
        country = "Finland"
        national_holidays = NationalHolidays("national_holidays_data.txt").get_dates()
        holiday_season = [date(year=2020, month=4, day=1), date(year=2021, month=3, day=31)]
        self.planner = HolidayPlanner(country, national_holidays, holiday_season, 50)

    def test_sunday_only_consumes_no_days(self):
        start_date = date(year=2020, month=5, day=3)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date)
        self.assertTrue(calculated_days == 0)

    def test_national_holiday_only_consumes_no_days(self):
        start_date = date(year=2020, month=5, day=1)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date)
        self.assertTrue(calculated_days == 0)

    def test_under_four_weekdays_consume_no_saturday_extra(self):
        start_date = date(year=2020, month=5, day=4)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date)
        self.assertTrue(calculated_days == 1)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date + timedelta(days=1))
        self.assertTrue(calculated_days == 2)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date + timedelta(days=2))
        self.assertTrue(calculated_days == 3)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date + timedelta(days=3))
        self.assertTrue(calculated_days == 4)

    def test_five_weekdays_consume_saturday_extra(self):
        start_date = date(year=2020, month=5, day=4)
        calculated_days = self.planner.calculate_consumed_holiday_days(start_date, start_date + timedelta(days=4))
        self.assertTrue(calculated_days == 6)

    def test_holiday_planner_returns_correct_number_of_consumed_days_around_christmas(self):
        test_data = get_data_around_christmas()
        perform_tests(self, test_data)

    def test_holiday_planner_returns_correct_number_of_consumed_days_around_new_year(self):
        test_data = get_data_around_new_year()
        perform_tests(self, test_data)

    def test_holiday_planner_returns_correct_number_of_consumed_days_around_easter(self):
        test_data = get_data_around_easter()
        perform_tests(self, test_data)

    def test_holiday_planner_returns_correct_number_of_consumed_days_around_may(self):
        test_data = get_data_around_may()
        perform_tests(self, test_data)


if __name__ == '__main__':
    unittest.main()
