#class - blueprint that contains attributes of a particular   and all the function 
#class laptop():
#    making = 2026---- attribute
#   RAM = 234---- attribute
 #   ROM = 786---- attribute
  #  GPU = 567---- attribute
#
 #   def laptop_on():---- function
  #      pass
 #   def laptop_off():---- function
 #       pass

#dell = laptop("dell 3690") ----object






#object - instance of class
class employee ():#class
    def __init__(self,name):
         self.name = name
    def login (self):
        print(f"{self.name} has logged in")

    def view_task (self):
        print(f"{self.name} has viewed task")

class teammember(employee):#inheritance
        def submit_task (self):
            print(f"{self.name} has summited the task")

class manager(employee):#inheritance
      def assign_task (self):
        if name['role'] == "manager":
              print(f"{self.name} has assigned the task")
        else:
              print("team memnber cannot assign the task")

john = teammember("john")#object
sam = teammember("sam")
john.login()
john.submit_task()