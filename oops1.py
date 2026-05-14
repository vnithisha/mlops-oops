# initiate a class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing data/attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("data/attributes have been initiated")

    def travel(self, destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# creating an instance of the class
sam = employee()

# # printing the attributes
# print(sam.salary) # or sam.id or sam.designation
#
# # calling a method
# sam.travel("Kerala")

print(type(sam))