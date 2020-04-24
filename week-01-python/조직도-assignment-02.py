#사람 클래스
# name1 : "John"
# age1 : 25
# sex1 : "male"
# position1 : "대리"
#
# name2 : "Jany"
# age2 : 30
# sex2 : "male"
# position2 : "대리"
#
# name3 : "Carol"
# age3 : 35
# sex3 : "female"
# position3 : "대리""

class Collegue:
    position = "대리"
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

collegue1 = Collegue("John",25,"male")
collegue2 = Collegue("Jany",30,"male")
collegue3 = Collegue("Carol",35,"female")


print(collegue1.sex)
print(collegue3.position)
print(collegue2.name)

# Collegue class inheritance + 직급 변경
class CollegueNew(Collegue):
    def __init__(self, name, age, sex, position):
        super().__init__(name,age,sex)
        self.position = position

colleguenew1 = CollegueNew("John",25,"male","중위")
print(colleguenew1.position)
print(colleguenew1.name)
