#Video: Starting Out With Python with ML 02

##############################3
#What is a function?
# f(x) = x**2
# 4 -> 16
# -4 -> 16

def myFunc(x : int) -> int:
    y = x**2
    return y

def stringIsTooLong(aWord : str) -> bool:
    if len(aWord) > 16:
        return True
    else:
        return False

def doubleUpAWord(aWord : str) -> str:
    # cat -> catcat
    # segue -> seguesegue
    return aWord+aWord

print(doubleUpAWord('turtle'))

class Student():
    def __init__(self, GPA, schedule, address):
        self.GPA = GPA
        self.schedule = schedule
        self.address = address

    def getNumOfLecture(self):
        return len(self.schedule)
    

s = Student(3.8, ['CS101', 'Eng203', 'Math415'], '315 Happy Ln')
t = Student(3.6, ['CS102', 'Eng213', 'Math318'], '317 Happy Ln')
print("s's GPA: ", s.GPA)
print('s is in ', s.getNumOfLecture(), ' lectures')






