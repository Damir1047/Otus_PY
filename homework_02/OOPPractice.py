
class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s//60
        s = s%60
        return Time(m, s)

    def info(self):
        return f'{self.minutes} : {self.seconds}'

t1 = Time(5, 50)
print(t1.info())

t2 = Time(3, 10)
print(t2.info())

t3 = t1+t2+t1
print(t3.info())

print(id(t1))