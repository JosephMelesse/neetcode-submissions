class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while counter != len(students):
            san = sandwiches[0]
            stu = students.pop(0)
            if san != stu:
                students.append(stu)
                counter += 1
            else:
                sandwiches.pop(0)
                counter = 0
        return len(students)
        