#Ths is a program in which a students are given grades accroding to their marks in "grade subject".
Moralscience = int(input("Entre your marks for Moralscience :- "))
Generalknowledge = int(input("Entre your marks GeneralKnowledge :- "))
Computer = int(input("Entre your marks Computer :- "))
Hindi = int(input("Entre your marks  Hindi:- "))
Drawing = int(input("Entre your marks Drawing :- "))
enteredgrade = Moralscience,Generalknowledge,Computer,Hindi,Drawing
a = ( Moralscience+Generalknowledge+Computer+Hindi+Drawing)
print("Your total marks are " + str(a))
if(Moralscience>=10):
    print("You got 'D'grade")
if(Moralscience>20):
    print("You got 'C'grade")    
if(Moralscience>=40):
    print("You got 'B'grade")
if(Moralscience==50):
    print("You got 'A'grade")
if(Generalknowledge>10):
    print("You got 'D'grade")
elif(Moralscience>=50):
    print("Invald marks entred")
    if(Generalknowledge>20):
        print("You got 'C'grade")
        if(Generalknowledge>=40):
            print("You got 'B'grade")
            if(Generalknowledge==50):
                print("You got 'A'grade")
elif(Generalknowledge>=50):
 print("Invald marks entred")
if(Computer>10):
    print("You got 'D'grade")
if(Computer>=20):
 print("You got 'C'grade")
 if(Computer>40):
      print("You got 'B'grade")
 if(Computer==50):
    print("You got'A'grade")
 elif(Computer>=50):
     print("Invalid marks entred")
     if(Hindi>=10):
         print("You got 'D' grade")
         if(Hindi>=20): 
             print("You got 'C' grade")
             if(Hindi>40):
                 print("You got 'B' grade")
                 if(Hindi==50):
                     print("You got 'A'grade")
                 elif(Hindi>=50):
                     print("Invalid marks entered")  
                     if(Drawing>=10):
                         print("You got 'D' grade ")
                         if(Drawing>=20):
                             print("You got 'C'grade ")
                             if(Drawing>=40):
                                 print("You got 'B' grade")
                                 if(Drawing==50):
                                     print("You got 'A' grade")
                                 elif(Drawing>=50):
                                     print("Invalid marks entered")
                                     #Finish