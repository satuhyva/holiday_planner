from holiday_planner import HolidayPlanner
from datetime import date


# As a default, the HolidayPlanner uses 1.4.2020-31.4.2021 as the holiday season,
# Finland as the country, and 50 days as the maximum time span
planner = HolidayPlanner()


# Holiday days consumed are calculated by giving the start and end date of the holiday
start_day = date(year=2020, month=12, day=31)
end_day = date(year=2021, month=1, day=19)
print(planner.calculate_consumed_holiday_days(start_day, end_day))





