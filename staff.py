
class Staff:
    def __init__(self,name,age,position,location,id,salary,pasword):
        self.name=name
        self.age=age
        self.position=position
        self.location=location
        self.id=id
        self.salary=salary
        self.pasword=pasword
    def show(self):
        return f'name:{self.name},age:{self.age},id:{self.id},position:{self.position},salary:{self.salary},location:{self.location}'
srt=Staff("ahad","21","seller","novza","1",20000000,"1234")
str1=[str]
