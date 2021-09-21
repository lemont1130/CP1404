def main():
    email_box={}
    email=input("Enter your email:")
    while email !="":
        name=get_name(email)
        print(f"Is your name {name}")
        check=input("(Y/n)")
        if check.upper()!= "Y" and check!="":
            name=input("Enter your name:")
            email_box[email]=name
        else:
            email_box[email]=name
        email=input("Enter your email:")
    for key,value in email_box.items():
        print(f"{key}({value})")

def get_name(email):
    name=email.split("@")[0]
    return name



main()
