def view():
    with open("passwords.txt", "r") as views:
        for i in views.readlines():
            data = i.strip()
            user, passw = data.split("|")
            print("user:",user,"password:",passw)


def rewrite(user_name,new_password):
    new_lines = []
    updated = False
    with open("passwords.txt", "r") as write: 
        lines = write.readlines()
        for line in lines:
            user1,passw1 = line.strip().split("|")
            print(user1,"1")
            print(user_name,"2")
            if user1 == user_name:
                new_lines.append(f"{user1}:{new_password}\n")
                updated = True
            else:
                new_lines.append(line)

    if not updated:
        print("username not found")
        return 
    
    with open("passwords.txt", "w") as file:
        file.writelines(new_lines)


def add():
    user_name = input("enter your name ")
    newpassword = input("enter your password")
    with open("passwords.txt", "a") as f:
        f.write(user_name + "|" + newpassword + "\n")

user_password = input("welcome enter ur master password ").strip()
masterpasword = "g"

while True:
    if user_password == masterpasword:
        vorw = input("what do you wanna do view or write or rewrite(choose v or w or rr) or q to quit ").strip()
        if vorw == "v":
            view()
        elif vorw == "w":
            add()
        elif vorw == 'rr':
            user_name = input("enter the username which u want change username")
            new_password= input("enter the change password")
            rewrite(user_name,new_password)
        elif vorw == "q":
            break
        else:
            print("enter some valid")
            continue
