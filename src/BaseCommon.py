#!/usr/bin/python
#print('----BELAJAR DICTIONARY-----');
#dict={'Nama':'Purwanto','Alamat':'Sragen'};
#print("Nama: ",dict['Nama']);
#print("Alamat: ",dict['Alamat']);

#print("FUNCTION");
#   print ("Nama Saya: ",name);
#    print("Usia Saya: ",age);
#    return;    
#printName("Aku");
# FUNCTION LENGHT ARGUMENT/PARAMETER
#def getData(arg1,*vartuple):
#    print("Output Is :",arg1);
#    for var in vartuple:
#        print(var);
#    return;
#getData(10,20,30,40,50);
#Anynomous Function/Lambda
#sum=lambda arg1,arg2,:arg1+arg2;
#print("Values of Total : ",sum(20,30));

#FUNCTION RETURN VALUE
#def getTotal(arg1,arg2):
#    total=arg1+arg2;
#    return total;
#print("Total is : ",getTotal(20,20));
class Employee:
    empCount=0;
    
    def __init__(self,name,saraly):
        self.name=name;
        self.salary=saraly;
        Employee.empCount +=1;

    def displayCount(self):
        print("Total Employee %d "%Employee.empCount);    
        
    def displayEmployee(self):
        print("Name : ",self.name,", Salary: ",self.salary);

#Create Instance Objects
emp1=Employee("Purwanto",2000);
emp2=Employee("Gunawan",4000);

emp1.displayEmployee();emp2.displayEmployee();

print("Count Employee : ",Employee.empCount);
    
    

    

    
    