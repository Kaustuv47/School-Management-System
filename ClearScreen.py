import os
class ClearScreen:
    def __init__(self):
        os.system('cls' if os.name=='nt' else 'clear')

