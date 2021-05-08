dict={}
while True:
    print("_______________Birthday App________________")
    print("1.Show Birthday")
    print("2.Add to Birthday List")
    print("3.Exit")
    choice = int(input("Enter the choice: "))
    if choice==1:
        if len(dict.keys())==0:
            print("nothing to show....")
        else:
            name=input("Enter the name look for birthday....")
            birthday=dict.get(name,"No data found")
            print(birthday)
    elif choice==2:
        name=input("Enter your friend's name:  ")
        date=input("Enter the birthday: ")
        dict[name]=date
        print("Birthday added successfully")
    elif choice==3:
        break
    else:
        print("Choose a valid option")
