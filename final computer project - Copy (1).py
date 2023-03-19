import random
#global variable declaration
name=[]
phno=[]
qid=[]
arrival=[]
riskzone=[]
report=[]
room=[]
price=[]
rc=[]
roomno=[]
custid=[]
#intro
def home():
    print("\t\t\t QUARANTINE HOTEL BOOKING \n")
    print("1. INFORMATION")
    print("2. BOOKING")
    print("3. PAYMENT")
    ch=input("DO YOU WISH TO PROCEED? Y/N->")
    if ch=="y" or ch=="Y":
        print("")
        info()
    elif ch=="N" or ch=="n":
        exit()
    else:
        print()
        print("enter valid option!")
        home()
    

def info():
    print("PASSENGER INFORMATION \n")
    while True:
        n=input("Enter Name:")
        ph=int(input("Enter Phone Number:"))
        q=int(input("Enter Q.ID:"))
        arr=input("Arrival from:")
        zone=input("Riskzone(high/low):")
        rep=input("Test report:")

        if n!="" and ph!="" and q!="" and arr!="" and zone!="" and rep!="":
            name.append(n)
            phno.append(ph)
            qid.append(q)
            arrival.append(arr)
            riskzone.append(zone)
            report.append(rep)
        booking()

def booking():
    #room type
    print()
    print("\t----SELECT ROOM TYPE----")
    print("\t1. STANDARD \nSingle bedroom and bathroom(for one/two person(s)--- \tQR 2000",
          "\t2. DOUBLE \nDouble bedroom and two bathroom(for upto four person(s)--- \tQR 3000",
          "\t***room service included *** ",
          sep="\n")
    print()
    ch=int(input("please enter your choice->"))    
    if ch==1:
        room.append('STANDARD')
        price.append(2000) 

    elif ch==2:
        room.append('DOUBLE')
        price.append(3000) 

    else:
        print("enter valid option!!!")
    print()
    #food options
    print("\t\t\tSELECT FOOD OPTIONS")
    print("\n\t\t 1. Vegetarian---QR 150(breakfast included)",
          "\n\t\t 2. Non-Vegetarian---QR 200(breakfast included)",
          "\n\t\t 3. Vegan---QR 100(breakfast included)")
    print()
    ch=int(input("please enter your choice->"))
    if ch==1:
        rc.append(150) 

    elif ch==2:
        rc.append(200)
        
    elif ch==3:
        rc.append(100)

    else:
        print("enter valid option!!!")

    print()

    #generate room no and customer id
        
    rn = random.randrange(50)+300
    cid = random.randrange(50)+10
    while rn in roomno or cid in custid:
        rn = random.randrange(70)+300
        cid = random.randrange(70)+10
    print("\t\t<<<ROOM BOOKED SUCCCESSFUL>>>",
          "\n\tRoom no.:",rn,
          "\n\tCustomer id:",cid)
    
    roomno.append(rn) 
    custid.append(cid)
    print()
    payment()
    
def payment():
    global roomno
    global name
    global custid
    global rc
    Sum=0
    print("THE FOLLOWING WILL SHOW YOU THE BILL FOR YOUR 14 DAY STAY")
    print("PAYMENT INFORMATION \n")
    print("NAME:",name[0])
    print("YOU HAVE SELECTED ROOM:",roomno[0])
    print("YOUR CUSTOMER ID",custid[0])
    while True:
        if room[0]=="STANDARD":
                print("SINCE YOU HAVE CHOSEN STANDARD,THE STAY COSTS QR 2000")
                Sum+=2000
                break
        else:
                print("SINCE YOU HAVE CHOSEN DOUBLE, THE STAY COSTS QR 3000")
                Sum+=3000
                break
    while True:
        if rc[0]==150:
                print("TOTAL FOR FOOD: QR 150")
                Sum+=150
                break
        elif rc[0]==200:
                print("TOTAL FOR FOOD:QR 200")
                Sum+=200
                break
        elif rc[0]==100:
                print("TOTAL FOR FOOD:QR 100")
                Sum+=100
                break
    print("YOUR TOTAL BILL IS QR",Sum)    
    print()
    
    print("\tPLEASE MAKE PAYMENT USING CREDIT/DEBIT CARD ONLY")
    z1=int(input("\tCARD NUMBER "))
    z2=input("\tCARD HOLDER NAME ")
    z=int(input("\tCVV "))
    print("\tSUCCESFULLY PAYED")
    print()
    a=int(input("HOW WOULD YOU RATE YOUR STAY OUT OF 10 "))
    if a in range(1,5):
        print()
        print("WE WILL DEFINITELY IMPROVE")
    else:
        print("THANK YOU!!,THAT'S WONDERFULL")
    print()
    print("thank you for your opinion")
    print("YOU HAVE SUCCESFULLY CHECKED OUT OF THE HOTEL")
    print("THANK YOU FOR YOUR STAY AND STAY SAFE!!!")
    print()

    c=int(input("press 0 to exit "))
    if c==0:
        exit()
    else:
        pass
           
home()
