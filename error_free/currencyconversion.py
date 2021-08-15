### Currency Conversion Modules ###

## Defining function for Rupees to Dollars ##
def INR_to_USD():     
    try:
        inr = float(input('Enter The Rupees :'))
        print('\nOutput :',inr*0.014,'Dollars\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex: 
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
## Defining function for Dollars to Rupees ##        
def USD_to_INR():     
    try:
        usd = float(input('Enter The Dollars :'))
        print('\nOutput :',usd*73.84,'Rupees\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
## Defining function for Rupees to Euro ##
def INR_to_EUR():     
    try:
        inr = float(input('Enter The Rupees :'))
        print('\nOutput :',inr*0.011,'Euro\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Defining function for Euro to Rupees ##
def EUR_to_INR():    
    try:
        Euro = float(input('Enter The Euro :'))
        print('\nOutput :',Euro*88.62,'Rupees\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Defining function for Dollars to Euro ##
def USD_to_EUR():         
    try:
        usd = float(input('Enter The Dollars :'))
        print('\nOutput :',usd*0.83,'Euro\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Defining function for Euro to Dollars ##
def EUR_to_USD():
    try:
        Euro = float(input('Enter The Euro :'))
        print('\nOutput :',Euro*1.20,'Dollars\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
