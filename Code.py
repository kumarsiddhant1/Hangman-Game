 #----------------------------------------------------------THE HANGMAN GAME-----------------------------------------------------------------
import random
#------------------------------------------------------------First Screen-------------------------------------------------------------------
print("HEY THERE! WELCOME to Hangman Gaming console")     #Welcome user
username = input("Enter Your Username Here --> ")      #Input Username of user
print(f"WOW {username.title()}! Let the Game Begin :) ")      #Excite the user to play the game
print("Please Choose The Topic Of Your Interest Below. Type ")
print("A --> Cities \nB --> Bollywood \nH --> Hollywood \nC --> Company \nP --> Personality")
choice = input("Input Your Choice --> ")
#-----------------------------------------------------------Second Screen-------------------------------------------------------------------
if choice == 'A':
    data = ['NEWYORK','LASVEGAS','MUMBAI','SYDNEY','AUKLAND','SANFRANCISCO','PRETORIA','ROME','BERLIN','BUDAPEST','CHICAGO',
           'LONDON','PARIS','TORONTO','MOSCOW','TOKYO','KOLKATA','SHANGHAI','BEIJING','AMSTERDAM','ABUDHABI','DUBAI',
           'DUBLIN','HONGKONG','NEWDELHI','AHMEDABAD','BANGALORE','HYDERABAD','PATNA','BHUBANESWAR','INDORE','RAJKOT','VARANASI',
           'VISAKHAPATNAM','CHENNAI','JAIPUR','WASHINGTONDC','SANDIEGO']    #Data
elif choice == 'B':
    data = ['SANAMRE','CHHICHHORE','BHARAT','DABANGG','DANGAL','BAAGHI','PK','WAR','CHENNAIEXPRESS','GOLMAAL','BARFI','LAGAAN','RANGDEBASANTI',
           'WANTED','RACE','HATESTORY','RAID','SANJU','EKTHATIGER','ZINDAGINAMILEGIDOBARA']
elif choice == 'H':
    data = ['JOKER','AVENGERSENDGAME','TOYSTORY','THEINCRIDIBLEHULK','IRONMAN','FASTANDFURIOUS','DEADPOOL','CAPTAINAMERICA',
            'INCEPTION','STARWARS','TITANIC','THEMATRIX','DOCTORSTRANGE','PACIFICRIM','DIEHARD','WALLE','AVATAR','THELIONKING','THEHANGOVER']
elif choice == 'C':
    data = ['FORD','COCACOLA','MERCEDES','BMW','SPICEJET','EMIRATES','FERRARI','LAMBORGHINI','TATA','APPLE','XIAOMI','SAMSUNG','SUZUKI',
            'VISA','FACEBOOK','INSTAGRAM','WHATSAPP','LENOVO','MICROSOFT','WALMART','RELIANCE','BOEING','NIKE','ADIDAS','DOMINOS','ADOBE',
            'YOUTUBE','PAYPAL','GOOGLE','ALPHABET','INTEL','MASTERCARD','NETFLIX','TOYOTA','UNILEVER','NOKIA','AMERICANTOURISTER']
elif choice == 'P':
    data = ['SACHINTENDULKAR','SUNDARPICHAI','ELONMUSK','BILLGATES','VIRATKOHLI','BARACKOBAMA','MAHATMAGANDHI','NEILARMSTRONG','ADOLFHITLER',
            'ALBERTEINSTEIN','HILARYCLINTON','NARENDRAMODI','RATANTATA','MUKESHAMBANI','JKROWLING','LIONELMESSI','CRISTIANORONALDO',
            'ISACNEWTON','NIKOLATESLA','BRADPITT','ROHITSHARMA','SALMANKHAN','SHAHRUKHKHAN','ANGELINAJOLIE','DONALDTRUMP','VIRENDRASEHWAG',
            'MARKZUKERBERG','STEVEJOBS','WARRENBUFFETT','MICHEALJACKSON','HRITIKROSHAN','STEPHENHAWKINGS','SHAKIRA','TOMCRUISE','USAINBOLT'
            'CHARLIECHAPLIN','ABRAHAMLINCOLN','NELSONMANDELA','WILLIAMSHAKESPEARE','ELIZABETHTAYLOR','TIGERWOODS','WALTDISNEY','LADYGAGA']
random.shuffle(data)  #Shuffled the data
mdata = data[0]    #Got the main data(mdata)
# print(mdata)
wgcounter = 0      #Wrong Guess Counter
rgcounter = 0      #Right Guess Counter
finallist = []    #The list of all the correct input by the user. finallist = mdata when user wins.
wglist = []
list1 = [" " for i in range(0,len(mdata))]
for i in range(0,45):
    if i == 0:     #The First Guess
        print("You Will Be Given Total 7 Chances")
        print(list1)
        letter = input(f"Lets Start! Enter Your First Guess {username.title()} ")      #Input the first guess 
        for j in range(0,len(mdata)):      #Loop for Comparing mdata and first guess Indexwise
            if letter == mdata[j] :   #statement if right guess
                rgcounter = rgcounter + 1
                list1[j] = letter
        if rgcounter == 0 :      #statement If wrong guess
            wgcounter = wgcounter + 1
        print(list1)
        print()
    elif i > 0:            #The next guess
        frgcounter = 0     #First Right Guess Counter (right guess counter for only a particular loop)
        print(f"You Have {7-wgcounter} Chances Left")    #Update about the chances left
        letter = input(f"Its Time For Your Next Guess {username.title()} ")    #Input the next guess
        for j in range(0,len(mdata)):    #Loop for comparing mdata and next guess Indexwise
            if letter == mdata[j]:     #statement if right guess
                frgcounter = frgcounter + 1     #frgcounter used specially for this loop(if i>0)
                rgcounter = rgcounter + 1     #update rgcounter
                list1[j] = letter
        print(list1)     #Update about right guessed letters in list
        print()
        if frgcounter == 0 :    #statement if wrong guess
            wgcounter = wgcounter + 1
            if 7-wgcounter == 0:   #If no chances left
                print(f"YOU LOOSE!!. BAD LUCK. Better Luck Next Time {username.title()} ")
                print(f"The Word Was {mdata} ")   #Telling user what was the word
                break
        elif list1 == list(mdata):   #If user win
            print(f"HURRAY!! YOU WIN. Well Played {username.title()} ")
            break
# print(rgcounter)   #print rgcounter
# print(wgcounter)   #print wgcounter
# print(list1)
# print(list(mdata))
#--------------------------------------------------------------CODE END HERE------------------------------------------------------------------
