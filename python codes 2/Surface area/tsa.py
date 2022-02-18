import math



def find_tsa():
    """A simple code to find Total Surface Area (TSA)"""

    # Gets options from user.
    res: str = input(
"""Select one option to find Total surface Area!, eg: 1
        1) Cuboid
        2) Cube
        3) Right circular cylinder
        4) Right circular cone
        5) Sphere
        6) Hemisphere"""
    )

    try:
        # Converts string instance to integer.
        resint = int(res) 
    except ValueError:
        # If convertion failed stops repl.
        raise TypeError('You should only select option numbers.')


    if resint == 1:
        # Calls cuboid function and return None.
        cuboid()
        return



def cuboid():
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
    tsa = 2 * (l*h + b*h + l*b)

    
    print(
f"""TSA of cuboid with length {l}, breadth {b} and height {h} is
        {tsa}"""
    )
    return



find_tsa() #Calls find tsa function