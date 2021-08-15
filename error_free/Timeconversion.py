### Function defenitions for Time conversion ###

## Hours to minutes ##
def h2m():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n*60,'minutes','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:    ## It will find and print the exception type automatically ##
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')
    
## Minutes to hours ##
def m2h():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n/60,'hours','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:   
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Seconds to hours ##
def s2h():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n/3600,'hours','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:   
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Hours to seconds ##        
def h2s():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n*3600,'seconds','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:   
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

## Seconds to minutes ##
def s2m():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n/60,'minutes','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:   
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted successfully \\\\','\n_________________________________________________________________________')

## Minutes to seconds ##
def m2s():
    try:
        n=int(input('Enter value :')) 
        print('\nOutput :',n*60,'seconds','\n')
    except ValueError:
        print('\nValue Error Raised..!!','\nPlease provide a number\n') 
    except Exception as ex:   
        print(ex,'\n')
    else:
        print('### Output printed ###\n')
    finally:
        print('\\\\ Code excecuted sucessfully \\\\','\n_______________________________________________________________________________')

