from datetime import timedelta


class ConsumedDaysCalculator:

    def __init__(self, national_holidays):
        self._national_holidays = national_holidays

    def calculate_days(self, first_day, last_day):
        raise Exception(f"Not implemented for this country yet!")



class ConsumedDaysCalculatorFinland(ConsumedDaysCalculator):

    def calculate_days(self, first_day, last_day):
        days_count = 0
        weekdays_count = 0
        day = first_day
        while day <= last_day:
            year = day.year
            month = day.month
            nationals_this_month = self._national_holidays[year][month - 1]

            if day.day in nationals_this_month or day.weekday() == 6:
                pass
            elif day.weekday() == 5:
                if weekdays_count == 5:
                    days_count += 1
                    weekdays_count = 0
            else:
                days_count += 1
                weekdays_count += 1
                if weekdays_count == 5:
                    days_count += 1
                    weekdays_count = 0
            day = day + timedelta(days=1)
        return days_count

