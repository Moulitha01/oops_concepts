#team member and manager 
def login (user):
    print(f"{user["name"]} has logged in")

def view_task (user):
    print(f"{user["name"]} has viewed task")

def submit_task (user):
    if user['role'] == "team_member":
        print(f"{user["name"]} has summited the task")
    else:
        print("manager no need to sumbit the task")

#key value pair data collection
user = {"name":"xxx","role":"team_member"}

login(user)
view_task(user)
submit_task(user)