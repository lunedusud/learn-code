# 학교 class 만들기

#School variables
# name1 = Aacademy
# date1 = 1991
# address1 = Gwangju
#
# name2 = Bacademy
# date2 = 1992
# address2 = Gwangju
#
# name3 = Cacademy
# date3 = 1993
# address3 = Gwangju


class School:
        address = "Gwangju"
        def __init__(self, name, date):
            self.name = name
            self.date = date

School1 = School("Aacademy",1991)
School2 = School("Bacademy",1992)
School3 = School("Cacademy",1993)

print(School1.date)
print(School2.name)
print(School3.address)
