

filename = 'fileprocessor.input'

with open(filename, 'r') as file:
    lines = file.readlines()


print("Printing out User Data:\n")

for line in lines:
    if line.startswith('#'):
        continue

    user_data = line.strip().split(':')

    username = user_data[0]
    password = user_data[1]
    userID = user_data[2]
    groupID = user_data[3]

    print(f"The user {username} has a password of {password} and has userID {userID} and groupID {groupID}")

print("\n End of User Data \n")
