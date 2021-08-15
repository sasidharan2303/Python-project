### DEFINING FUNCTION FOR ARITHMETIC OPERATIONS ###
def  Arithmetic():
    try:
        if choice_1 == 1:
            ## Printing Instructions of Arithmetic Opearations ##
            print('*************************************')
            print(' Enter 1 for Addition Operation\n','Enter 2 for Subtraction Operation\n','Enter 3 for Multiplication Operation\n','Enter 4 for Division Operation\n','Enter 5 for Floor_Division Operation\n','Enter 6 for Modulus Operation\n','Enter 7 for Exponetial Operation')
            print('*************************************\n')

            while True:
                try:
                    choice_2 = int(input('Enter Your Choice :'))      ## Getting choice from user to perform Arithmetic Operations
                    if choice_2 <= 7:
                        try:
                            if choice_2 == 1:
                                error_free.add()
                            if choice_2 == 2:
                                error_free.sub()
                            if choice_2 == 3:
                                error_free.mul()
                            if choice_2 == 4:
                                error_free.div()
                            if choice_2 == 5:
                                error_free.f_div()
                            if choice_2 == 6:
                                error_free.mod()
                            if choice_2 == 7:
                                error_free.exp()

                        except ValueError:
                            print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
                    else:
                        print('\nThere is no choice like',choice_2,'in given instruction..','\nKindly enter valid choice..!!\n')
                except ValueError:
                    print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')

        else:
            print('/// You Have Choosen Nothing ///\n')

    except ValueError:
        print('ValueError Raised..!!','\nPlease Enter Valid Number\n')


### DEFINING FUNCTION FOR TRIGNOMETRIC OPERATIONS ###
def  Trignometric():
    try:
        if choice_1 == 2:
            ## Printing Instructions of Trignometric Opearations ##
            print('*************************************\n')
            print(' Enter 1 for Log Operation\n','Enter 2 for Sin Operation\n','Enter 3 for Cos Operation\n','Enter 4 for Tan Operation\n')
            print('*************************************\n')

            while True:
                try:
                    choice_3 = int(input('Enter Your Choice :'))      ## Getting choice from user to perform Arithmetic Operations
                    if choice_3 <= 4:
                        try:
                            if choice_3 == 1:
                                error_free.log()
                            if choice_3 == 2:
                                error_free.sin()
                            if choice_3 == 3:
                                error_free.cos()
                            if choice_3 == 4:
                                error_free.tan()
                        except ValueError:
                            print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
                    else:
                        print('\nThere is no choice like',choice_3,'in given instruction..','\nKindly enter valid choice..!!\n')
                except ValueError:
                    print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
        else:
            print('/// You Have Choosen Nothing ///\n')
    except ValueError:
        print('ValueError Raised..!!','\nPlease Enter Valid Number\n')


### DEFINING FUNCTION FOR TIME_CONVERSION OPERATION ###
def  Timeconversion():
    try:
        if choice_1 == 3:
            ## Printing Instructions of Timeconversion Opearations ##
            print('*****************************************')
            print(' Enter 1 for Hours_to_Minutes Operations\n','Enter 2 for Minutes_to_Hours Operation\n','Enter 3 for Seconds_to_Hours Operation\n','Enter 4 for Hours_to_Seconds Operation\n','Enter 5 for Seconds_to_Minutes Operation\n','Enter 6 for Minutes_to_Seconds Operation\n')
            print('*****************************************\n')

            while True:
                try:
                    choice_4 = int(input('Enter Your Choice :'))      ## Getting choice from user to perform Arithmetic Operations
                    if choice_4 <= 6:
                        try:
                            if choice_4 == 1:
                                error_free.h2m()
                            if choice_4 == 2:
                                error_free.m2h()
                            if choice_4 == 3:
                                error_free.s2h()
                            if choice_4 == 4:
                                error_free.h2s()
                            if choice_4 == 5:
                                error_free.s2m()
                            if choice_4 == 6:
                                error_free.m2s()
                        except ValueError:
                            print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
                    else:
                        print('\nThere is no choice like',choice_4,'in given instruction..','\nKindly enter valid choice..!!\n')
                except ValueError:
                    print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
        else:
            print('\n/// You Have Choosen Nothing ///')
    except ValueError:
        print('ValueError Raised..!!','\nPlease Enter Valid Number\n')


### DEFINING FUNCTION FOR CURRENCY_CONVERSION OPERATION ###
def  currency():
    try:
        if choice_1 == 4:
            ## Printing Instructions of Timeconversion Opearations ##
            print('*********************************')
            print(' Enter 1 for Rupees to Dollars\n','Enter 2 for Dollars to Rupees\n','Enter 3 for Rupees to Euro\n','Enter 4 for Euro to Rupees\n','Enter 5 for Dollars to Euro\n','Enter 6 for Euro to Dollars\n')
            print('*********************************\n')

            while True:
                try:
                    choice_5 = int(input('Enter Your Choice :'))      ## Getting choice from user to perform Arithmetic Operations
                    if choice_5 <= 6:
                        try:
                            if choice_5 == 1:
                                error_free.INR_to_USD()
                            if choice_5 == 2:
                                error_free.USD_to_INR()
                            if choice_5 == 3:
                                error_free.INR_to_EUR()
                            if choice_5 == 4:
                                error_free.EUR_to_INR()
                            if choice_5 == 5:
                                error_free.USD_to_EUR()
                            if choice_5 == 6:
                                error_free.EUR_to_USD()()
                        except ValueError:
                            print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
                    else:
                        print('\nThere is no choice like',choice_5,'in given instruction..','\nKindly enter valid choice..!!\n')
                except ValueError:
                    print('Value Error Raised','\nPlease Read The Instruction And Enter Valid Choice\n')
        else:
            print('\n/// You Have Choosen Nothing ///')
    except ValueError:
        print('ValueError Raised..!!','\nPlease Enter Valid Number\n')


## Importing package ##
import error_free

## Printing Instructions ##
print('*********************************************')
print(' Enter 1 for Arithmatic operations\n','Enter 2 for Trignometric Operations\n','Enter 3 for Time_conversion operations\n','Enter 4 for Currency_conversion operations')
print('*********************************************\n')

## Getting choice from user ##
while 1:
    try:
        choice_1 = int(input('Enter Your Choice :'))
        if choice_1 <= 4:

            if choice_1 == 1:
                while 1:
                    Arithmetic()        ## Function call of Arithmetic Operations

            if choice_1 == 2:
                while 1:
                    Trignometric()      ## Function call of Trignometric Operations

            if choice_1 == 3:
                while 1:
                    Timeconversion()    ## Function call of Time_conversion Operations

            if choice_1 == 4:
                while 1:
                  currency()           ## Function call of Currency_conversion Operations
        else:
            print('\nThere is no choice like',choice_1,'in given instruction..','\nKindly enter valid choice..!!\n')

    except ValueError:
        print('ValueError Raised..!!','\nPlease Enter Valid Number Within (1 to 4) As per the Instructions..\n')


