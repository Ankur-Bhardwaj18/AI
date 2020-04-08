# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:11:29 2020

@author: surya teja reddy
"""

# Function declaration for seating arrangement of the people in the bus.
def seatarrangement(n):
    i=0
    j=0
    name = []
    age = []
    b = []
    c = []
    d = []
    
    if n<1 or n>18:
        print("invalid input")
        return
    for x in range(n):
        print("PASSENGER-",x+1)
        print("Enter your personal details: ")
        name.append(input("Name --> "))
        age.append(int(input("Age --> ")))    
        b.append(input("Are you physically handicapped ? (Y/N) --> "))
        print("\n")
        
    
    for x in range(n):
        if b[x]=='Y':    #A new list that consist of only handicapped ppassenger.
            c.append(age[x])
            i=i+1
        else:
            d.append(age[x]) #Separate list for normal passenger.
            j=j+1
    
    c.sort(reverse=True) #Sorting the list of handicapped passenger in reverse acc. to their age.
    d.sort(reverse=True) #Sorting the list of normal passenger in reverse acc. to their age.
    print(c)
    print(d)
    
    
    print("Physically handicapped are suggested to be seated at the front")
    print("Seats are allocated according to age")
    
                    
    print("\nSeat no.   Name      Age")
    for x in range(len(c)):
        print(x+1,"       ", name[age.index(c[x])],"      ",c[x])
    size=len(c)
    
    
      
    print("\nSeat no.   Name      Age\n\n")
    for x in range(len(d)):
        size=size+1
        print(size,"       ",name[age.index(d[x])],"      ",d[x])
        
    
    print("\n\n",18-n," seats are still vacant")
    
    
def bus_rule():
    print("There are 18 seats in the vehicle")
    n=int(input("Enter the number of passengers:"))
    if n<1 or n>18:
        print("Sorry for the inconvenience but there are only 18 seats available ")
        return 
    else:
        seatarrangement(n)
        
bus_rule()