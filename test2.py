# creating a class Student

class Student:
    # Adding a Constructer

    def __init__(self, name, section, rank):
        self.name= name
        self.section= section
        self.rank= rank

    # Accept

    def accept(self, name, section, rank):
        var= Student(name, section, rank)
        Slist.append(var)

    # Display
     
    def display(self, var):
         print("Name of Student : ", var.name)
         print("Section of Student : ", var.section)
         print("Rank of Student : ", var.rank)

    # Search

    def search(self, num):
        for i in range(Slist.__len__()):
            if (Slist[i].rank ==num):
                return i

    # Delete

    def delete(self, num):
        i= obj.search(num)
        del Slist[i]

    # Update

    def update(self, num, num2):
        i= obj.search(num)
        Slist[i].rank= num2

# list for Students
Slist= []
# object of class Student
obj= Student('','',0)

# Performing Accept function
print("\n After Accepting and Displaying : ")
obj.accept("Ram", "A", 32)
obj.accept("Shyam", "B", 12)
obj.accept("Raju", "C", 22)

# Performing Display function
for i in range(Slist.__len__()):
    obj.display(Slist[i])

# Performing Search function
print("\n After Searching : ")
a=obj.search(12)
obj.display(Slist[a])

# Performing Delete function
obj.delete(12)
print("\n After deleting: ")
for i in range(Slist.__len__()):
    obj.display(Slist[i])

# Performing Update function
obj.update(22, 40)
print("\n After updating: ")
for i in range(Slist.__len__()):
    obj.display(Slist[i])


        
        



    