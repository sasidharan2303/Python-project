### Finding the values for Log,Sin,Cos and Tan ###

import math                 ##importing math module

##Log=>function defenition
def log():                 
    try:
        n=int(input("Enter value :"))
        print('\nOutput :',math.log(n),'\n')
    except ValueError:
        print('\nValueError Exception Raised..!!','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
   
##Sin=>function defenition
def sin():                
    try:
        n=int(input("Enter value :"))
        print('\nOutput :',math.sin(n),'\n')
    except ValueError:
        print('\nValueError Exception Raised..!!','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

##Cos=>function defenition
def cos():                 
    try:
        n=int(input("Enter value :"))
        print('\nOutput :',math.cos(n),'\n')
    except ValueError:
        print('\nValueError Exception Raised..!!','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
##Tan=>function defenition    
def tan():                 
    try:
        n=int(input("Enter value :"))
        print('\nOutput :',math.tan(n),'\n')
    except ValueError:
        print('\nValueError Exception Raised..!!','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')



