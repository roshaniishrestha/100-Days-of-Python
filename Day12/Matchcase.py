x = (input("Do you want to vote: "))
match x.lower():
    case "yes": 
        print ("vote is yes")
    case "No":
        print("vote is no")
    case _:
        print ("it is neither yes nor no. ")