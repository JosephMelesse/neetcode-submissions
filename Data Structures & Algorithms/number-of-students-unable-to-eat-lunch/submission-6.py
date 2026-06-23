class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = sandwiches[::-1]
        counter = 0
        while counter != len(students):
            san = sandwiches[-1]
            stu = students.popleft()
            if san != stu:
                students.append(stu)
                counter += 1
            else:
                sandwiches.pop()
                counter = 0
        return len(students)
        