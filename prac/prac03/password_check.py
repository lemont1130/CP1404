def main():
    MIN_LENGTH = 2
    MAX_LENGTH = 6
    password = get_password(MIN_LENGTH,MAX_LENGTH)
    print_starts(password)
def get_password(MIN_LENGTH,MAX_LENGTH):
    password=input("Enter password:")
    while len(password)<MIN_LENGTH or len(password)>MAX_LENGTH:
        print("Password invalid")
        password = input("Enter password:")
    return password
def print_starts(password):
    print("*"*len(password))
main()

