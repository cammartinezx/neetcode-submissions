class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #circular =0
        #square=1
        #sandwiches=students
        count0=students.count(0)
        count1=students.count(1)


        #noone wants 0 and top is 0, noone wants 1 and top is 1
        while (count0 != 0 and sandwiches[0] == 0) or (count1 != 0 and sandwiches[0] == 1):
            #if student likes sandwich then both leave 
            if sandwiches[0]==students[0]:
                if sandwiches[0]== 0: count0-=1
                else: count1-= 1
                sandwiches.pop(0)
                students.pop(0)
                
            #if not, student back of the array, sandwich stays
            else:
                students.append(students[0])
                students.pop(0)
        return len(students)
            

