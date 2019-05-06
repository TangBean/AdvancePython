class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))  # 如果我们改了类名为 NewDate，这里也要改 Date

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))  # 如果我们改了类名为 NewDate，这啥都不用变

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == '__main__':
    new_day = Date(2019, 4, 18)
    new_day.tomorrow()
    print(new_day)

    date_str0 = "2019-4-18"
    new_day = Date.parse_from_string(date_str0)
    Date.tomorrow(new_day)  # 也可以通过 Date 调用对象方法，不过要传入对象，不能自己传入调用对象了
    new_day.tomorrow()
    print(new_day)

    date_str1 = "2019-4-20"
    new_day = Date.from_string(date_str1)
    print(new_day)
