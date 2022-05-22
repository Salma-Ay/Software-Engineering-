
class person:
    def __init__(self, national_Id, name, age,father_name,mother_name,birthplace,date_of_birth):
        self.nationalId = national_Id
        self.name = name
        self.age = age
        self.father_name = father_name
        self.mother_nam = mother_name
        self.birthplace = birthplace
        self.date_of_birth = date_of_birth
print("PLease press enter then type your infromation:")
x=input("National_id: ")
y=input("Name: ")
z=input("Age: ")
w=input("Father_name: ")
n=input("Mother_name: ")
l=input("Birthplace: ")
o=input("Date_of_birth: ")
p1 = person(x,y,z,w,n,l,o)
f = open("MyFile.txt","a")
for i in range (7):
    k=[x,y,z,w,n,l,o]
    r=["National_id: ","Name: ","Age: ","Father_name: ","Mother_name: ","Birthplace: ","Date_of_birth: "]
    f.write(r[i])
    f.write(k[i])
    f.write("\n")
f.write("\n")
f = open("MyFile.txt","r")
print(f.read())
f.close()

