# 요구사항3: 학생의 과목별 성적과 가중치 (i.e 수학, 75, 0.05)
from collections import namedtuple

Grade = namedtuple('Grade', ('subject', 'score', 'weight'))

class Gradebook:
    def __init__(self):
        self._grades = {}
    
    def report_grade(self, name, subject, score, weight):
        if name not in self._grades:
            self._grades[name] = list() 
        self._grades[name].append(Grade(subject, score, weight))

    def average_grade(self, name):
        total, count = 0, 0
        subjects = {grades.subject for grades in self._grades[name]}
        for subject in subjects:
            total += self._average_subject(name, subject)
            count += 1
        return total / count

    def _average_subject(self, name, subject):
        total, total_weight = 0, 0
        for grade in self._grades[name]:
            if grade.subject != subject:
                continue

            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


book = Gradebook()
albert, math, gym = '알버트 아인슈타인', '수학', '체육'
book.report_grade(albert, math, 75, 0.05)
book.report_grade(albert, math, 65, 0.15)
book.report_grade(albert, math, 70, 0.80)
book.report_grade(albert, gym, 100, 0.40)
book.report_grade(albert, gym, 85, 0.60)
print(book.average_grade(albert))  

