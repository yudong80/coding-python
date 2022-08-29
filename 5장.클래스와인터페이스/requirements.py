# 요구사항1: 학생의 전체 성적 (i.e 90)
# 요구사항2: 학생의 과목별 성적 (i.e 과학, 70)
# 요구사항3: 학생의 과목별 성적과 가중치 (i.e 수학, 75, 0.05)

# req1
class SimpleGradeBook:
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
    
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradeBook()
newton = '아이작 뉴턴'
book.add_student(newton)
book.report_grade(newton, 90)
book.report_grade(newton, 95)
book.report_grade(newton, 85)

print(book.average_grade(newton))