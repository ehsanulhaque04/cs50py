name = input("WHat is your name? ")

if name== "Abdul":
    print("Enter The House")
elif name == "Kulsuma":
    print("Enter The house")
elif name == "Hazera":
    print("Enter The House")
elif name == "Ehsanul":
    print("Enter The Hosue")
elif name== "Ariful":
    print("Enter The House")
elif name== "Munirul":
    print("Enter The Hosue")
else:
    print("Who is this? If you are not the Member of family Then call The House holder: 7167708511")

# match will ignore in the name in not in the list.
match name:
    case  "Abdul":
        print("Enter The house")
    case "Kulsuma":
        print("Enter The house")
    case "Hazera" :
        print("Enter The house")
    case "Ehsanul":
        print("Enter The house")
    case "Ariful":
        print("Enter The house")
    case "Munirul":
        print("Enter The house")

match name:
    case "Abdul" | "Kulsuma" | "Hazera"| "Ehsanul"| "Ariful"| "Munirul":
        print("Enter the house")
    case _:
        print("Who is this? If you are not the Member of family Then call The House holder: 7167708511")

