###ERROR_FREE_APPLICATION###

# 1.ADDITION
def add():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a+b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
        
# 2.SUBTRACTION    
def sub():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a-b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

# 3.MULTIPLICATION
def mul():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a*b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
# 4.DIVISION
def div():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a/b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
# 5.FLOOR_DIVISION
def f_div():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a//b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

# 6.MODULUS
def mod():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a%b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n________________________________________________________________________________________')

# 7.EXPONENTIAL
def exp():
    try:
        a=int(input("Enter a value :"))
        b=int(input("Enter b value :"))
        print('\nOutput :',a**b,'\n')
    except ValueError:
        print('\nValue Error Exception Raised','\nPlease provide a number\n')
    except Exception as ex:
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')


