print("Hello,welcome to my quiz...")
ans=input("Are you ready to play ? (yes/no): ")
score=0
total_q=5
if ans.lower() == 'yes':
    ans=int(input("1.How many bones in a human body...? : "))
    if ans==206:
        score += 1
        print("Correct answer..")
    else :
        print("oops,Incorrect answer..")


    ans=(input("2. Who is the father of COMPUTER ? : ")
    if ans.lower() == 'Charles Babbage':
         print("Correct Answer..")
         print("Just two quizes remains , you will be winner..")
    else:
        print("oh,Try Again ")


    ans=int(input("3. how many states in INDIA/ : "))
    if ans == 29:
        print(" Wohooo...Correct Answer ")
        print(" you just awesome...")
    else:
        print("oh no, Incorrect Answer")


    ans=input("name our national anthem : ")
    if ans.lower() == 'Jana Gana Mana' :
        print("wow , you are genuis...")
        print("Just one remains")
    else:
        print(" Shit,that was going very well")


    ans=input("Which state is know as NAWABO KA SEHAR ? : ")
    if ans.lower() == 'Lucknow':
        print("hurrey,correct answer")
        print("you win")
    else:
        print("oh no,well played")z    
