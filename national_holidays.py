class NationalHolidays:

    def __init__(self, data_file_name):
        with open(data_file_name) as reader:
            dates_first_year = [[] for _i in range(12)]
            dates_second_year = [[] for _i in range(12)]
            first_year = 0
            second_year = 0
            for line in reader.readlines():
                parts = line.strip().split("-")
                year = int(parts[2])
                month = int(parts[1])
                day = int(parts[0])
                if first_year == 0:
                    first_year = year
                if year == first_year:
                    dates_first_year[month - 1].append(day)
                else:
                    second_year = year
                    dates_second_year[month - 1].append(day)
            self._dates = {
                first_year: dates_first_year,
                second_year: dates_second_year
            }


    def get_dates(self):
        return self._dates

