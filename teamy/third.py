
class person:
    def __init__(self, national_Id, name, age,father_name,mother_name,birthplace,date_of_birth):
        self.nationalId = national_Id
        self.name = name
        self.age = age
        self.father_name = father_name
        self.mother_nam = mother_name
        self.birthplace = birthplace
        self.date_of_birth = date_of_birth
def Add_information():
    print("PLease enter your information:")
    x = input("National_ID: ")
    y = input("Name: ")
    z = input("Age: ")
    w = input("Father_name: ")
    n = input("Mother_name: ")
    l = input("Birthplace: ")
    o = input("Date_of_birth: ")
    p1 = person(x, y, z, w, n, l, o)
    f = open("MyFile.txt", "a")
    for i in range(7):
        k = [x, y, z, w, n, l, o]
        r = ["National_id: ", "Name: ", "Age: ", "Father_name: ", "Mother_name: ", "Birthplace: ", "Date_of_birth: "]
        f.write(r[i])
        f.write(k[i])
        f.write("\n")
    f.write("*********************")
    f.write("\n")
def look_for_aUser():
    f = open("MyFile.txt","r")
    x=input("please enter user ID: ")
    print("**************")
    for line in f:
        if x in line:
            for i in range(6):
                print(f.readline(),end='')

    f.close()

def print_information():
    f = open("MyFile.txt", "r")
    print("\n",end='')
    print(f.read())
    f.close()
print("1.Add information")
print("2.Print information")
print("3.look for a user")
x=int(input("please select your choice: "))
if (x==1):
    Add_information()
if (x==2):
    print_information()
if (x==3):
    look_for_aUser()





