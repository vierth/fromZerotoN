# functions are defined in python using the def keyword

def pauls_function():
    print("Hello! This is Paul's function!")

def whose_function(name):
    print(f"Hi, {name}! Nice function!")

def greeting(yourname, myname):
    print(f"Hi {yourname}! My name is {myname}")

def interaction(yourname, myname, interaction_type="greeting"):
    if interaction_type == "greeting":
        print(f"Hi {yourname}! My name is {myname}")
    elif interaction_type == "parting":
        print(f"Goodbye {yourname}. {myname} out.")

def add(num_1, num_2):
    return num_1 + num_2
    

res = add(15, 20)
print(res)