n = int(input())
reserved = set()
for i in range(n):
    reserved.add(input())

attending = set()
command = input()
while not command == "END":
    if command in reserved:
        attending.add(command)
    command = input()

did_not_attend = len(reserved) - len(attending)
did_not_attend_list = reserved.difference(attending)
list_vip_not_attending = sorted([el for el in did_not_attend_list if el[0].isdigit()])
list_regular_not_attending = sorted([el for el in did_not_attend_list if el[0].isalpha()])
print(did_not_attend)
for guest in list_vip_not_attending:
    print(guest)
for guest in list_regular_not_attending:
    print(guest)
