class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = ['com', 'bg', 'org', 'net']

while True:
    command = input()

    if command == "End":
        break

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    command = command.split("@")
    name = command[0]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = command[1].split(".")[1]

    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
