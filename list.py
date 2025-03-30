class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"{self.name} ({self.age})"


new_person_list=[Person('jobayed',23),Person('Tanvir',35)]
new_person_list.sort(key=lambda x:x.name)
print(new_person_list)