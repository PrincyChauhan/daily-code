candidate1=input("Enter 1st Candidate  name: ")
candidate2=input("Enter 2nd Candidate  name: ")

cand1_votes=0
cand2_votes=0

voters_id=[101,102,103,104,105,106]
no_of_voters=len(voters_id)

print("No of voters: ",no_of_voters)

voted=[]

while True:
    if voters_id==[]:
        print("Voting session is over")
        if cand1_votes>cand2_votes:
            percent=(cand1_votes/no_of_voters)*100
            print(candidate1,"has won with ",percent,"% votes")
            break
        elif cand2_votes>cand1_votes:
            percent=(cand2_votes/no_of_voters)*100
            print(candidate2,"has won with ",percent,"% votes")
            break
        elif and2_votes==cand1_votes:
            print("Both have equal votes")
            break
    else:
        voter=int(input("Enter your voter id: ")) 
        if voter in voted:
            print("You have already voted")
        else:
            if voter in voters_id:
                print(f"1.{candidate1}\n2.{candidate2}")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    cand1_votes+=1
                    voted.append(voter)
                    print( f"Thanks for casting your vote to  {candidate1}")
                elif choice==2:
                    cand2_votes+=1
                    voted.append(voter)
                    print( f"Thanks for casting your vote to  {candidate2}")                      
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("Your are not a voter here")    