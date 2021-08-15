"""
  Created by : Sasidharan K
        Date : 3rd may 2021
        Info : To create a Lucky_draw by using random 
"""


###Creating LUCKY_DRAW###

import random

print("________________________ABC SUPERMARKET____________________________\n")  ##printing the name of the shop

print("The token numbers of the persons who won the gifts are shown below...!!\n")

Token_List=random.sample(range(201,220),10) 

print(Token_List,'\n')                     ##printing the token numbers randomly

print("The persons who have above token numbers can collect their gifts from the shopkeeper....!!!")

    
