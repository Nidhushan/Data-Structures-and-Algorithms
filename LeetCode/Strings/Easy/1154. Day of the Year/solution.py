class Solution:
    def dayOfYear(self, date: str) -> int:
        daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))

        day_num = sum(daysPerMonth[:m-1]) + d

        if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)) and m>2:
            return day_num + 1
        else:
            return day_num

        """
        Question:
        date - String(gregorian calendar date - format - YYYY-MM-DD)
        return day of the year

        Solution:
        have a list of 12 with no of days per month
        return days + sum(list[:month])
        make sure to add 1 if its leap year and the month is after feb
        """