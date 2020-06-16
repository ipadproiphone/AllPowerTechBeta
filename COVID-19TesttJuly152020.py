import time





def loading(x):
        print("Loading...")
        time.sleep(x)


print("This is All Power Tech's COVID-19 Digital Test kit. \n DISCLAIMER")
loading(2.8)
print("This test is not verified by medical health experts. \n Do not rely on this page to make any desecision to travel. \n Although the questions came from the CDC.")
loading(1.909090)
print("Login Successful!")




print(" \n")






riskcounter = 0




quest1 = input("Have you been experiencing any tooth pains? Answer yes or no.(This is case not sensitive). ")
loading(3)
if quest1 == "y" or quest1 == "Y" or quest1 == "yes" or quest1 == "Yes":
        riskcounter += 4
elif quest1 == "n" or quest1 == "N" or quest1 == "no" or quest1 == "No":
        riskcounter += 0



quest2 = input("Have you had any difficulty breathing?(If possible, consult an electronic breat tracker). Yes or No(This is not case senditive). ")
loading(2.6759)
if quest2 == "y" or quest2 == "Y" or quest2 == "yes" or quest2 == "Yes":
        riskcounter += 7
elif quest2 == "n" or quest2 == "N" or quest2 == "no" or quest2 == "No":
        riskcounter += 0




quest3 = input("Have you been getting the chills and\or shivering? Answer Yes Or No(This is not case sensitive). ")
loading(3.14159265)
if quest3 == "y" or quest3 == "Y" or quest3 == "yes" or quest3 == "Yes":
        riskcounter += 8
elif quest3 == "n" or quest3 == "N" or quest3 == "no" or quest3 == "No":
        riskcounter += 0



quest4 = input("Have you been experiencing muscle pain? Answer Yes Or No(This is not case sensitive). ")
if quest4 == "y" or quest4 == "Y" or quest4 == "yes" or quest4 == "Yes":
        riskcounter += 4
elif quest4 == "n" or quest4 == "N" or quest4 == "no" or quest4 == "No":
        riskcounter += 0


loading(3)


quest5 = input("Have you had sudden loss in taste/smell? Answer Yes Or No(This is not case sensitive). ")
if quest5 == "y" or quest5 == "Y" or quest5 == "yes" or quest5 == "Yes":
        riskcounter += 9.353678
elif quest5 == "n" or quest5 == "N" or quest5 == "no" or quest5 == "No":
        riskcounter += 0
else:
  riskcounter += 0



def findFinalRes():
                
        finalres = float(riskcounter)
        finalres += 3
        if finalres == 0:
                print("You have a %0-10 chance of having COVID-19(COronaVIrus Disease 2019).")
        elif finalres < 10 and finalres != 0:
                print("You have a %30-45 percent change of having COVID-19(COronaVIrus Disease 2019).")
        elif finalres >= 15 and finalres != 16:
                print("You have a %65-70 chance of having COVID-19(COronaVIrus Disease 2019).")
        elif finalres >= 80:
                print("You have a %80-90 percent chance of having COVID-19(COronaVIrus Disease 2019).")
        
        elif finalres >= 50:
                print("You have a %95-100 percent chance of having COVID-19(COronaVIrus Disease 2019).")
        else:
                print("You have a %75-80 percent chance of having COVID-19(COronaVIrus Disease 2019)")

        
     
        
loading(4)
findFinalRes()
