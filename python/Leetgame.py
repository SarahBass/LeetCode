

############################################################################
#                _      _               _     ___     _   
#         __   _(_)_ __| |_ _   _  __ _| |   / _ \___| |_ 
#         \ \ / / | '__| __| | | |/ _` | |  / /_)/ _ \ __|
#          \ V /| | |  | |_| |_| | (_| | | / ___/  __/ |_ 
#           \_/ |_|_|   \__|\__,_|\__,_|_| \/    \___|\__|
#   ˚☽                                     
#  ｡       ☆                                           ☆         ☆
# ☆‌ ╭◜◝‌ ‌͡‌ ‌◜◝╮‌ ‌    ..... ‌҉‌ ‌        / `     ‌ ╭◜◝‌ ‌͡‌ ‌◜◝◜◝‌ ‌͡‌ ‌◜◝‌ ‌◜◝‌◜◝◜◝‌ ‌͡‌ ‌◜◝‌ ‌◜◝  
#  ‌ (‌ 。‌•‿•‌‌ ‌) ☆ (‌。•‿•‌‌ )  ‌      ‌<。‌•‿•‌。>  <   Practice Leetcode Skills~! )          
#   ╰◟◞‌ ‌͜‌ ‌◟◞      ~~~~~ ☆    ‌҉‌ ‌  /, ,'\    ╰◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌  
#
#            ☆                          ☆                 ☆            ☆
#               Virtual Star comes from a galaxy far, far away...                  
############################################################################


#                              Written by Sarah Bass



import math
import random
from random import randrange

#Global Variables-------------------------#                             
userInput=11                              # 
num = random.randint(0,36)                #
randy1=[3, 6, 10, 60, 25, 100, 120, 333,  #
    444, 605, 999 ,                       #
    17,18,19,21,28,35,36,                 #
    37,42,63,73,74,84,85,                 #
    94,101,111,119,126,131,               #    
    185,202,303,404,409]                  #
randnum = randy1[num]                     #    
randy2=[4, 7, 10, 8, 32, 38, 44, 64,      #
    77, 86, 100, 111, 120,                #
    17,18,19,21,28,35,36,                 #
    37,42,63,73,74,84,85,                 #
    94,101,111,119,126,131,               #    
    185,102,103,104,109]                  #
randnumber = randy2[num]                  #    
randy3=[5,6,7,9,11,12,14,15,              #
    17,18,19,21,28,35,36,                 #
    37,42,63,73,74,84,85,                 #
    94,101,111,119,126,131,               #    
    185,202,303,404,409]                  #
palindromenum= randy3[num]                #    
data= False                               #
abutton = 0                               #
pageNumber=0                              #
game = 0                                  #
#-----------------------------------------#

###########################################################################################
###################MINI GAME LOGIC ########################################################
###########################################################################################
def intToRoman(num: int) -> str:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

def isPalindrome(self, x):
    if x > 0:
        temp = x
        rev_int_elements = []
        while temp > 0:
            digit = temp % 10
            rev_int_elements.append(digit)
            temp = temp // 10
        org_int_elements = rev_int_elements[::-1]
        return rev_int_elements == org_int_elements
    elif x == 0:
        return True
    else:
        return False

class Game:
    def __init__(self, name, answer, text, userAnswer):
        self.name = name
        self.answer = answer
        self.text = text
        self.userAnswer= userAnswer
                
game1 = Game("Roman Quest", randnum, intToRoman(randnum),userInput)    
game2 = Game("PAlindroME!", True, palindromenum, isPalindrome(isPalindrome,(userInput))) 
game3 = Game("BinaryBeats", randnumber,bin(randnumber)[2:], userInput)
game4 = Game("Witch's Hex",randnumber,hex(randnumber)[2:],userInput)

game1.answer = randy1[num]
game1.text = intToRoman(game1.answer)
game2.text =  randy3[num]
game3.answer = randy2[num]
game3.text = bin(game3.answer)[2:]
game4.answer = randy2[num]
game4.text = hex(game4.answer)[2:]

###########################################################################################
###########################################################################################
###########################################################################################

#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
#                        START OF GAME                           # 
#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=

print( "☆‌ ╭◜◝‌ ‌͡‌ ‌◜◝╮‌ ")
print( "  ‌(‌ 。‌•‿•‌‌ ‌) ☆ " + game1.name)
print( "☆‌ ╰◟◞‌ ‌͜‌ ‌◟◞‌  Question:" + game1.text)
game1.userAnswer= int(input("Enter Number = "))
if game1.userAnswer == game1.answer:
    print("Correct!")
else:
    print("Oops! The correct answer is ", game1.answer)

#game2.userAnswer= isPalindrome(isPalindrome, int(input("Enter Number = ")))
#game3.userAnswer= int(input("Enter Number = "))
#game4.userAnswer= int(input("Enter Number = "))
            

        
#When game answer and useranswer match say correct
