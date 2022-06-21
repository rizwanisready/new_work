lipstick = 25
cust_lipstick = 0
foundation = 20
cust_foundation = 0
kajal = 10
cust_kajal = 0
blush = 20
cust_blush = 0
eyeliner = 15
cust_eyeliner = 0
compact = 25
cust_compact = 0
highlighter = 20
cust_highlighter = 0
def intro(start=1):
    print("Welcome to SADIQA BEAUTY Shop!!")
    print("The latest and biggest online store for your beauty needs..")
    start = int(input("Click 1 to continue: "))
    while start == 1:
        print('''Click [5] for Booking | [6] for Cancellation????''')
        print(f"{lipstick} number of lipstick available in stock")
        print(f"{foundation} number of foundation available in stock")
        print(f"{kajal} number of kajal available in stock")
        print(f"{blush} number of blush available in stock")
        print(f"{eyeliner} number of eyeliner available in stock")
        print(f"{compact} number of compact available in stock")
        print(f"{highlighter} number of highlighter available in stock")
        proceed = int(input("Enter the keyword:- [5] for Booking/[6] for Cancellation "))
        try:
            if proceed == 5:
                booking()
            elif proceed == 6:
                cancel_booking()
            else:
                intro(start=1)
        except:
            print("Enter Correct Keyword:- ")
            intro(start=1)
    else:
        print("Sorry!! Repeat Again.........")
        intro(start=1)
def booking():
    print('''
    Booking ID |1| Lipstick price per piece is 100 rupees
    Booking ID |2| Foundation price per piece is 500 rupees
    Booking ID |3| Kajal price per piece is 200 rupees
    Booking ID |4| Blush price per piece is 150 rupees
    Booking ID |5| Eyeliner price per piece is 100 rupees
    Booking ID |6| Compact price per piece is 250 rupees
    Booking ID |7| Highlighter price per piece is 450 rupees
    ''')
    book = int(input("Enter booking ID to purchase: "))
    if book == 1:
        lipstickd()
    elif book == 2:
        foundationd()
    elif book == 3:
        kajald()
    elif book == 4:
        blushd()
    elif book == 5:
        eyelinerd()
    elif book == 6:
        compactd()
    elif book == 7:
        highlighterd()
    else:
        print("Please give correct keyword!!!")
def lipstickd():
    global lipstick
    global cust_lipstick   
    
    qty = int(input("How many lipstick you want..?? "))
    if qty <= lipstick:
        lipstick = lipstick - qty
        cust_lipstick = cust_lipstick + qty
        print(f'Available lipstick stock: {lipstick}')
        print(f'Your bucket contains {cust_lipstick} lipstick')
    else:
        print("Sorry!!!..")
def cancel_booking():
    print('''
    Cancel ID |1| Lipstick price per piece is 100 rupees
    Cancel ID |2| Foundation price per piece is 500 rupees
    Cancel ID |3| Kajal price per piece is 200 rupees
    Cancel ID |4| Blush price per piece is 150 rupees
    Cancel ID |5| Eyeliner price per piece is 100 rupees
    Cancel ID |6| Compact price per piece is 250 rupees
    Cancel ID |7| Highlighter price per piece is 450 rupees
    ''')
    cancel = int(input("Enter cancellation ID to return: "))
    if cancel == 1:
        lipstickc()
    elif cancel == 2:
        foundationc()
    elif cancel == 3:
        kajalc()
    elif cancel == 4:
        blushc()
    elif cancel == 5:
        eyelinerc()
    elif cancel == 6:
        compactc()
    elif cancel == 7:
        highlighterc()
    else:
        print("Please give correct keyword!!!")
def lipstickc():
    global lipstick
    global cust_lipstick
    
    qty = int(input("How many lipstick you want to return..?? "))
    if qty <= cust_lipstick:
        cust_lipstick = cust_lipstick - qty
        lipstick = lipstick + qty
        print(lipstick)
        print(cust_lipstick)
    else:
        print("Sorry!!!")

def foundationd():
    global foundation
    global cust_foundation  
    
    qty = int(input("How many foundation you want..?? "))
    if qty <= foundation:
        foundation = foundation - qty
        cust_foundation = cust_foundation + qty
        print(f"Available stock of foundation is {foundation}.")
        print(f"You have bought {cust_foundation} foundation.")
    else:
        print("Sorry!!!")

def foundationc():
    global foundation
    global cust_foundation
    
    qty = int(input("How many foundation you want to return..?? "))
    if qty <= cust_foundation:
        cust_foundation = cust_foundation - qty
        foundation = foundation + qty
        print(f"Available stock of foundation is {foundation}.")
        print(f"You have remaining {cust_foundation} foundation.")
    else:
        print("Sorry!!!")


def kajald():
    global kajal
    global cust_kajal 
    
    qty = int(input("How many Kajal you want..?? "))
    if qty <= kajal:
        kajal = kajal - qty
        cust_kajal = cust_kajal + qty
        print(f"Available stock of kajal is {kajal}.")
        print(f"You have bought {cust_kajal} kajal.")
    else:
        print("Sorry!!!")

def kajalc():
    global kajal
    global cust_kajal
    
    qty = int(input("How many kajal you want to return..?? "))
    if qty <= cust_kajal:
        cust_kajal = cust_kajal - qty
        kajal = kajal + qty
        print(f"Available stock of kajal is {kajal}.")
        print(f"You have remaining {cust_kajal} kajal.")
    else:
        print("Sorry!!!")


def blushd():
    global blush
    global cust_blush 
    
    qty = int(input("How many blush you want..?? "))
    if qty <= blush:
        blush = blush - qty
        cust_blush = cust_blush + qty
        print(f"Available stock of blush is {blush}.")
        print(f"You have bought {cust_blush} blush.")
    else:
        print("Sorry!!!")

def blushc():
    global blush
    global cust_blush
    
    qty = int(input("How many blush you want to return..?? "))
    if qty <= cust_blush:
        cust_blush = cust_blush - qty
        blush = blush + qty
        print(f"Available stock of blush is {blush}.")
        print(f"You have remaining {cust_blush} blush.")
    else:
        print("Sorry!!!")


def eyelinerd():
    global eyeliner
    global cust_eyeliner
    
    qty = int(input("How many eyeliner you want..?? "))
    if qty <= eyeliner:
        eyeliner = eyeliner - qty
        cust_eyeliner = cust_eyeliner + qty
        print(f"Available stock of eyeliner is {eyeliner}.")
        print(f"You have bought {cust_eyeliner} number of eyeliner")
    else:
        print("Sorry!!!")

def eyelinerc():
    global eyeliner
    global cust_eyeliner
    
    qty = int(input("How many eyeliner you want to return..?? "))
    if qty <= cust_eyeliner:
        cust_eyeliner = cust_eyeliner - qty
        eyeliner = eyeliner + qty
        print(f"Available stock of eyeliner are {eyeliner}.")
        print(f"Remaining you have {cust_eyeliner} eyeliner")
    else:
        print("Sorry!!!")


def compactd():
    global compact
    global cust_compact
    
    qty = int(input("How many compact you want..?? "))
    if qty <= compact:
        compact = compact - qty
        cust_compact = cust_compact + qty
        print(f"Availavle compact in stock are {compact}")
        print(f"You have bought {cust_compact} number of compact")
    else:
        print("Sorry!!!")

def compactc():
    global compact
    global cust_compact
    
    qty = int(input("How many compact you want to return..?? "))
    if qty <= cust_compact:
        cust_compact = cust_compact - qty
        compact = compact + qty
        print(f"Available number of compact are {compact}")
        print(f"You have remaining {cust_compact} number of compact")
    else:
        print("Sorry!!!")


def highlighterd():
    global highlighter
    global cust_highlighter   
    
    qty = int(input("How many highter you want..?? "))
    if qty <= highlighter:
        highlighter = highlighter - qty
        cust_highlighter = cust_highlighter + qty
        print(f"Available Highters in stock are {highlighter}.")
        print(f"You have bought {cust_highlighter} number of highlighter")
    else:
        print("Sorry!!!")

def highlighterc():
    global highlighter
    global cust_highlighter
    
    qty = int(input("How many highlighter you want to return..?? "))
    if qty <= cust_highlighter:
        cust_highlighter = cust_highlighter - qty
        highlighter = highlighter + qty
        print(f"Available highlighters in stock are {highlighter}")
        print(f"You have remaining {cust_highlighter} number of highlighter")
    else:
        print("Sorry!!!")


intro(start=1)

