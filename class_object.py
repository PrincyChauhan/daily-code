# create student class that takes name and marks of 3 subject as argumnet in constructor then create a metgod to print the average



class Student():
    
    def __init__(self,name,marks) :
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("Average marks of student",self.name,"is",sum/3)
        
s1=Student('Princy',[99,98,97]) 
s1.get_avg()           