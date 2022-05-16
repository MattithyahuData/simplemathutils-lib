def add(*args:int or float):
    ''' 
    Returning the sum of the inputs.

    :param args: Any integer or float | Datatype: int or float

    Returns: 
    Sum of arguments   

    '''
    
    try:
        # Initiating total variable equal to 0
        total = 0

        # For loop to iterate over tuple indexes and add totals  
        for i in args:
            total += i
            
        # Returning total     
        return total
    

    except TypeError:

        # exception error for incorrect datatype 
        print("TypeError: Arguments can only be integer or float type.")


def subtract(num1: int or float,num2: int or float):
    ''' 
    Returning the difference of 2 inputs. 

    :param num1: The first number. | Datatype: int or float
    :param num2: The second number. | Datatype: int or float

    Returns: 
    1st paramter - 2nd parameter  

    '''

    # Returning 1st paramter - 2nd parameter  
    return num1-num2


def multiply(*args:int or float):
    ''' 
    Returning the product of the inputs.

    :param args: Any integer or float | Datatype: int or float

    Returns: 
    Product of arguments   

    '''
    
    try:
        # Initiating total variable equal to 1
        total = 1

        # For loop to iterate over tuple indexes and multiply totals  
        for i in args:
            total *= i
            
        # Returning total     
        return total
    

    except TypeError:

        # exception error for incorrect datatype 
        print("TypeError: Arguments can only be integer or float type.")


def divide(num1: int or float,num2: int or float):
    ''' 
    Returning the product of dividing 2 inputs. 

    :param num1: The first number. | Datatype: int or float
    :param num2: The second number. | Datatype: int or float

    Returns: 
    1st paramter / 2nd parameter  

    '''

    # Returning 1st paramter - 2nd parameter  
    return num1/num2

### function to add all!! 

