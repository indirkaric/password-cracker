import hashlib
from datetime import datetime

FILE_NAME = "10-million-password-list-top-1000000.txt"
flag = 0
counter = 0

def load_password_list():
    passwords = []
    with open(FILE_NAME,'r') as password_file:
        for password in password_file:
            passwords.append(password.strip('\n'))

    print("most common password list size is {}".format(len(passwords)))
    return passwords


most_common_passwords = load_password_list()

pass_hash = input("Enter md5 hash:")

start_time = datetime.now()

for password in most_common_passwords:
    counter += 1
    encoded_password = password.encode("utf-8")
    digest = hashlib.md5(encoded_password.strip()).hexdigest()
    if digest == pass_hash:
        print("Password found")
        print("Password is " + password)
        print("Attempts " + str(counter))
        flag = 1
        break

if flag == 0:
    print("Password is not in the list")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))