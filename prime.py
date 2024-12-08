li:list[int]=[]

def is_prime(start:int,end:int)->int:
    """
    Find prime numbers in a given range and append them to a global list.
    
    Args:
        start (int): Starting number of the range (inclusive)
        end (int): Ending number of the range (inclusive)
        
    Returns:
        list[int]: List of prime numbers found in the range
        
    Note:
        This function modifies the global list 'li' by appending prime numbers to it
    """
    for num in range(start,end+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                li.append(num)
    return li
print(sorted(is_prime(1,10), reverse=True))