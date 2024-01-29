
class Grades:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

a = Grades("Mike", [34, 56, 23])
b = Grades("Peter", [])

b.grades = list(a.grades) 

b.grades.append(54)

print(a.grades)
print(b.grades)
        