# For data analysis generat random customer detials

class Customer:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def __repr__(self):
        return f'[{self.name},{self.department},{self.salary}]'
    
c1=Customer('jobayed','data analysis',40000)
c2=Customer('hossen','marketing',76000)
c3=Customer('islam','sales',30000)

c_list=[c1,c2,c3]
# getting the highest salary 
heightSalary=[hsalary.salary for hsalary in c_list]
print(max(heightSalary))
