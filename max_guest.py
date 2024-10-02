#  A party has been organized on cruise. The party is organized for a limited time(T). The number of
#  guests
#  entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array. The
#  task is to
#  find the maximum number of guests present on the cruise at any given instance within T hours.
#  Example 1:
#  Input :
#  5-> Value of T
#  [7,0,5,1,3]-> E[], Element of E[0] to E[N-1], where input each element is separated by new line
#  [1,2,1,3,4]-> L[], Element of L[0] to L[N-1], while input each element is separate by new line.
#  Output :
#  8-> Maximumnumberofguests on cruise at an instance


def max_guest(T, E, L):
    current_guests = 0
    max_guests = 0
    
    for i in range(T):
        current_guests+=E[i]
        print("current_guests.............",current_guests)
        current_guests-=L[i]
        print("current_guests..........L",current_guests)
        
        if current_guests>max_guests:
            max_guests=current_guests
    return max_guests       
T=5
E=list(map(int,input().split()))
L=list(map(int,input().split()))
result=max_guest(T,E,L)
print(result)