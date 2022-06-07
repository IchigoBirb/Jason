#This program asks the user(teacher) for the amount of students and their Name(s),ID(s),Score(s) and prints them in the format below
#Eg(2 students)
#=================
#Student: Name_list[0] 
#ID: Id_list[0]
#Score: Score_list[0]
#=================
#Student: Name_list[1] 
#ID: Id_list[1]
#Score: Score_list[1]
#=================

#Imports
import sys
#Functions
def check_ID(ID):
    if len(ID) == 7 and ID[6].isalpha() and ID[0:5].isdigit():
        Valid = ID
        return Valid
def check_score(Score):
    if Score_int > 0 or Score_int <= 100:
        Valid = Score
        return Valid
    else:
        print('Invalid Input,please enter a score between 1 and 100')
#Defining global variables/lists/dictionaries
Name_list = []
Id_list = []
Score_list = []
Amt = 0

Skip = input('Type \'Skip\' to skip program else press any key\n')#Typing 'Skip' skips the program
while Skip != 'Skip':
    Amt = input('How many students are there?\n')#Tells program how much time to run
    try:
        Amt = int(Amt)#Ensure that Amt is an int
    except:
        continue#If Amt is not int continue asking until input can be int
    break
for i in range(Amt):
    while Skip != 'Skip':
        name_input = input('Please enter name:\n')
        while name_input.isdigit():#Checks if name has digits
            print('Invalid input,please type a name without integers')
            break
        else:
            Name_list.append(name_input)
            while Skip != 'Skip':
                ID_input = input('Please enter ID (eg 222114X) \n')
                if ID_input == (check_ID(ID_input)):#Checks if ID matches the requirements in the checkID function
                    Id_list.append(ID_input)
                    while Skip != 'Skip':
                        Score = input('Please type score:\n')
                        while not Score.isdigit():#Checks if Score is digit
                            print('Invalid Input,please enter a score')
                        else:
                            Score_int = int(Score)
                            if Score_int == (check_score(Score_int)):
                                Score_list.append(Score_int)
                                Skip = 'Skip'
                            else:
                                print('Invalid Input,please enter a score')
    Skip = ''#resets loop breaker for next student
#prints the data collected above
print(17*'=')
try:
    for i in range(Amt):
        print('Student:', Name_list[0], '\nID:', Id_list[0], '\nScore:', Score_list[0])
        del(Name_list[0],Id_list[0],Score_list[0])
        print(17*'=')
    sys.exit()
except:
    pass

