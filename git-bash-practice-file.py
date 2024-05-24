print("Hello world")


def add_something(sth=""):
    if sth:
        print("Something has been added: {0}".format(sth))
    else:
        print("nothing added")
    pass


name = "book list"

add_something(name)
add_something()

check = add_something(10)

typeof(check)
print("added sth")
print(2+2)
