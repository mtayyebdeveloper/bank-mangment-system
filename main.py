from tkinter import *
import random
import os
import time

if __name__=="__main__":
    account_balance=0
    prize_list=[100,200,500,800,80,50,10,1000,3000,5000,10000,100000,50000,20000,70000,1,2,3,4,5,6,7,8,9,0]
    def genarate_random_price():
        choice1=random.randint(1,3)
        choice2=random.randint(1,3)
        choice3=random.randint(1,3)

        print("Game is started....")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        
        print(f"{choice1} | {choice2} | {choice3}")

        if choice1==choice2==choice3:
            prize=random.choice(prize_list)
            print(f"Wow, You win Rs.{prize}")
            return prize
        else:
            print("Sorry, You loss. Please try again....")
            return 0
    
    def signup_form():
        print("............ Signup form................")

        fullname=input("Enter your full name: ")
        username=input("Enter your username: ")
        email=input("Enter your email id: ")
        mobile=input("Enter your mobile number: ")
        password=input("Enter your password: ")
        cpassword=input("Conform password: ")
        if not password==cpassword:
            return print("please conform password.")

        if not fullname or not username or not email or not mobile or not password or not cpassword:
            print("please fill the form..")
            signup_form()
        else:
            alldata=f"{fullname}\n{username}\n{email}\n{mobile}\n{password}"

            with open("signup.txt","w") as signupfile:
                signupfile.write(alldata)

            return True
    

    def login_form():
        print("............ Login form................")

        email=input("Enter your email id: ")
        password=input("Enter your password: ")

        newform =[]
        with open("signup.txt") as loginfile:
            h=loginfile.readlines()
            for i in h:
                l=i.replace("\n","")
                newform.append(l)
            # print(h)
        
        if email==newform[2] and password==newform[4]:
            with open("logintoken.txt","w") as f:
                f.write("10")
            return True
        else:
            print("You enterd wrong email or password.")
            tryagain =input("Do you want to try again (y or n) :")
            if tryagain=="y":
                login_form()
            else:
                return False


    def expire_token():
        if os.path.isfile("logintoken.txt"):
            with open("logintoken.txt") as tokenfile:
                token=tokenfile.read()
                inttoken=int(token)
                if inttoken>0:
                    inttoken=inttoken-1

                    with open("logintoken.txt","w") as f:
                        strtoken=str(inttoken)
                        f.write(strtoken)

                        return True
                else:
                    l=login_form()
                    if l:
                        return True
                    else:
                        return False
        else:
            l=login_form()
            if l:
                return True
            else:
                return False



    def create_wallet():
        newform =[]
        with open("signup.txt") as loginfile:
            h=loginfile.readlines()
            for i in h:
                l=i.replace("\n","")
                newform.append(l)

        print("............ Create Bank wallet ................")

        accountname=input("Enter your account name: ")
        password=input("Enter 4 digit PIN: ")
        
        if not accountname or not password:
            print("please fill the form..")
            create_wallet()
        elif not len(password)==4:
            print("please enter only 4 digit PIN..")
            create_wallet()
        else:
            accountids=["sd2137sadhg216372136","sdad7243472374asj6as","2343ha7sad7asdas7d6s","asd7sdfgg32432ghhfsd"]
            r=random.choice(accountids)
            allform=f"{newform[0]}\n{accountname}\n{password}\nABL\n{newform[3]}\n{newform[2]}\n{r}\n{account_balance}"

            with open("bankwallet.txt","w") as walletfile:
                walletfile.write(allform)

            return True


    def account_details():
        newform =[]
        with open("signup.txt") as loginfile:
            h=loginfile.readlines()
            for i in h:
                l=i.replace("\n","")
                newform.append(l)
        
        print(f".............. Welcome to ABL Bank {newform[0]}. This is your wallet .................")

        newdata=[]
        with open("bankwallet.txt") as bankfile:
            data=bankfile.readlines()
            for i in data:
                l=i.replace("\n","")
                newdata.append(l)

        print(f"Full Name: {newform[0]}")
        print(f"username: {newform[1]}")
        print(f"Email Id: {newform[2]}")
        print(f"Mobile Number: {newform[3]}")
        print(f"Account Name: {newdata[1]}")
        print(f"Account Id: {newdata[6]}")
        print(f"Your Balance is: {newdata[7]}")


    def win_money_game():

        newdata=[]
        with open("bankwallet.txt") as bankfile:
            data=bankfile.readlines()
            for i in data:
                l=i.replace("\n","")
                newdata.append(l)


        print("........... Welcome to our ABL win money game .................")
        print(".....Check you luck.....")
        print(".....Play 1 game in only Rs.10 and win Rs.100,000......")

        print("..............................................................")
        print(f"You account balance is {newdata[7]}")
        user =input("Do you want to play game (y or n): ")

        if user=="y":
            newdata=[]
            with open("bankwallet.txt") as bankfile:
                data=bankfile.readlines()
                for i in data:
                    l=i.replace("\n","")
                    newdata.append(l)
            
            code=input("Enter your account 4 digit code: ")
            if code==newdata[2]:
                if int(newdata[7])>15:
                   int_balance=int(newdata[7])
                   int_balance=int_balance-10
                   str_balance=str(int_balance)

                   newdata[7]=str_balance

                   with open("bankwallet.txt", "w") as walletfile:
                        newwallet=""
                        for i in newdata:
                           newwallet+=i+"\n"

                        walletfile.write(newwallet)
                else:
                    print("Your account balance is less then 15")
                #    exit()
                    isexit=input("Do you want to Exit this programe (y or n): ")
                    if isexit=="n":
                        start_programe()
                    else:
                        exit() 
            else:
                print("You enterd wrong code. please try again..")
                # exit()
                isexit=input("Do you want to Exit this programe (y or n): ")
                if isexit=="n":
                    start_programe()
                else:
                    exit() 

            user_prize=genarate_random_price()

            int_prize=int(newdata[7])
            int_prize=int_prize+user_prize
            str_prize=str(int_prize)

            newdata[7]=str_prize

            with open("bankwallet.txt", "w") as walletfile:
                newwallet=""
                for i in newdata:
                    newwallet+=i+"\n"

                walletfile.write(newwallet)

            play_again=input("Do you want to play again (y or n): ")
            if play_again=="y":
                win_money_game() 
            else:
                start_programe()     
        else:
            start_programe()
        
        isexit=input("Do you want to Exit this programe (y or n): ")
        if isexit=="n":
            start_programe()
        else:
            exit() 
    

    def amount_adding():
        newdata=[]
        with open("bankwallet.txt") as bankfile:
            data=bankfile.readlines()
            for i in data:
                l=i.replace("\n","")
                newdata.append(l)
            
        code=input("Enter your account 4 digit code: ")
        if code==newdata[2]:
            amount=int(input("Enter amount to add in your account: "))

            int_amount=int(newdata[7])
            int_amount=int_amount+amount
            str_amount=str(int_amount)

            newdata[7]=str_amount

            print("Amount adding please wait for 5s.........")
            print("5")
            time.sleep(1)
            print("4")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)

            with open("bankwallet.txt", "w") as walletfile:
                newwallet=""
                for i in newdata:
                    newwallet+=i+"\n"

                walletfile.write(newwallet)
                print("Amount added successfuly......")
            
            print(f"Your account balance is {newdata[7]}......")
            isexit=input("Do you want to Exit this programe (y or n): ")
            if isexit=="n":
                start_programe()
            else:
                exit()
        else:
            print("You enterd wrong code. please try again..")
                # exit()
            isexit=input("Do you want to Exit this programe (y or n): ")
            if isexit=="n":
                start_programe()
            else:
                exit() 



    def start_programe():
        print(".............. Welcome to ABL Bank .................")

        if os.path.isfile("signup.txt"):
            l=expire_token()
            if l==True:
                if os.path.isfile("bankwallet.txt"):
                    account_details()

                    user_choice=input("For playing game enter (g), for amount adding enter (a) and for exit programe enter (e): ")
                    if user_choice=="g":
                        win_money_game()
                    elif user_choice=="a":
                        amount_adding()
                    else:
                        exit()
                else:
                    c=create_wallet()
                    if c==True:
                        start_programe()
                    else:
                        isexit=input("Do you want to Exit this programe (y or n): ")
                        if isexit=="n":
                            start_programe()
                        else:
                            exit()
        else:
            s=signup_form()
            if s==True:
                start_programe()
            else:
                isexit=input("Do you want to Exit this programe (y or n): ")
                if isexit=="n":
                    start_programe()
                else:
                    exit()

    start_programe()