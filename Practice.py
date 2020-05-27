def main():
    say(3)
    names = ["sri","kanth"]

    if "sri" in names:
        print("found")
    else:
        print("not found")

    people = {
        "sri":"999999",
        "dee":"88888"
    }

    if "sri" in people:
        print("Found : ",people["sri"])

    x = 1
    y = 5
    print("x=",x , "y=",y)

    x,y = y,x
    print("x=",x , "y=",y)


def say(n):
    for i in range(n):
        print("Hello")

main()