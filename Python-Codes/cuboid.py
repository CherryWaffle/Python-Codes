
def cuboid():
    """A simple code to find TSA, LSA and volume of cuboid."""

    # Gets option from users.
    res: str = input(
"""Select an option, eg: 1
        1) Find TSA of cuboid
        2) Find LSA of cuboid
        3) Find volume of cuboid"""
    )

    try:
        # Converting to integer.
        resint = int(res)
    except:
        # If convertion failed raise TypeError and stops repl.
        raise TypeError('Response must be numbers (option numbers).')
    
    if resint == 1:
        # If option selected is 1 then calls tsa function
        tsa()
        return
    elif resint == 2:
        # If option selected is 2 then calls lsa function
        lsa()
        return
    elif resint == 3:
        # If option selected is 3 then calls volume function
        volume()
        return
    else:
        # If number is not 1, 2 or 3 then raise TypeError and stops repl.
        raise TypeError('You can only select 1, 2 and 3.')



def tsa():
    """Function to find TSA of cuboid."""

    # Length, breadth and height.
    lbh: str = input('What are the length, breadth and height?. Seperate by comma\n\t').replace(' ', '') # To remove blank spaces
    # Seperates returned string.
    splitted: list = lbh.split(',')

    if not len(splitted) == 3:
        # If there is more than 3 values, stops repl.
        raise TypeError(f'Expected 3 values got {len(splitted)}.')

    try:
        # Converting to float like we did in find_tsa function.
        splitted_: list = [float(x) for x in splitted]
    except ValueError:
        # If convertion failed stops repl.
        raise TypeError('Only decimals or numbers allowed.')


    # Length is the first part then breath and height.
    l: int = splitted_[0] # Gets first item on the index, index starts with 0.
    b: int = splitted_[1]
    h: int = splitted_[2]

    # Formula to find TSA of cuboid
    tsa_ = 2 * (l*h + b*h + l*b)

    
    print(
f"""TSA of cuboid of length {l}, breadth {b} and height {h} is
        {tsa_}"""
    )
    return

def lsa():
    """Function to find LSA of cuboid."""

    # Length, breadth and height.
    lbh: str = input('What are the length, breadth and height?. Seperate by comma\n\t').replace(' ', '') # To remove blank spaces
    # Seperates returned string.
    splitted: list = lbh.split(',')

    if not len(splitted) == 3:
        # If there is more than 3 values, stops repl.
        raise TypeError(f'Expected 3 values got {len(splitted)}.')

    try:
        # Converting to float like we did in find_tsa function.
        splitted_: list = [float(x) for x in splitted]
    except ValueError:
        # If convertion failed stops repl.
        raise TypeError('Only decimals or numbers allowed.')


    # Length is the first part then breath and height.
    l: int = splitted_[0] # Gets first item on the index, index starts with 0.
    b: int = splitted_[1]
    h: int = splitted_[2]

    # Formula to find LSA of cuboid
    lsa_ = 2 * h * (l + b)

    
    print(
f"""LSA of cuboid of length {l}, breadth {b} and height {h} is
        {lsa_}"""
    )
    return


def volume():
    """Function to find Volume of cuboid."""

    # Length, breadth and height.
    lbh: str = input('What are the length, breadth and height?. Seperate by comma\n\t').replace(' ', '') # To remove blank spaces
    # Seperates returned string.
    splitted: list = lbh.split(',')

    if not len(splitted) == 3:
        # If there is more than 3 values, stops repl.
        raise TypeError(f'Expected 3 values got {len(splitted)}.')

    try:
        # Converting to float like we did in find_tsa function.
        splitted_: list = [float(x) for x in splitted]
    except ValueError:
        # If convertion failed stops repl.
        raise TypeError('Only decimals or numbers allowed.')


    # Length is the first part then breath and height.
    l: int = splitted_[0] # Gets first item on the index, index starts with 0.
    b: int = splitted_[1]
    h: int = splitted_[2]

    # Formula to find Volume of cuboid
    volume_ = l * b * h

    
    print(
f"""Volume of cuboid of length {l}, breadth {b} and height {h} is
        {volume_}"""
    )
    return


cuboid() # Calls the cuboid function