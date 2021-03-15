class Time:
    def __init__(self,hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self, other):
        return self.hour + other.hour, self.minute + other.minute, self.second + other.second


t1 = Time(4, 5, 20)
t2 = Time(7, 30, 12)
t3 = t1 + t2
print(t3)

