# Program: ZbrozekP2_StateInfo.py
# Programmer: Mike Zbrozek 
# MZbrozek1@cnm.edu
# Date: 08 Sept 2023
# Purpose: Program displays the state’s capital, number of congressional districts and the order the state joined the union 

# Print title 
# Epic Logo - https://ascii.co.uk/art/usa
print("""   ,__                                                  _,
    \~\|  ~~---___              ,                          | \\
     | Wash.| |   ~~~~~~~|~~~~~| ~~---,   _            VT_/,ME>
    /~-_--__| |  Montana |N Dak\ Minn/ ~\~_/Mich.     /~| ||,'                
    |Oregon |  \         |------|   { WI / /~)     __-NY',|_\,NH           UNITED
   /       |Ida.|~~~~~~~~|S Dak.\    \   | | '~\  |_____,|~,-'Mass.       STATE
   |~~--__ |    | Wyoming|____  |~~~~~|--| |__ /_-'Penn.{,~Conn (RI)        FINDER! 
   |   |  ~~~|~~|        |    ~~\ Iowa/  `-' |`~ |~_____{/NJ
   |   | Nev |  '---------, Nebr.\----|   |IN|OH,' ~/~\,|`MD (DE)
   ',  \     |Utah| Colo. |~~~~~~~|    \IL| ,'~~\WV/ VA |
    |Cal\    |    |       | Kansas| MO  \_-~ KY /`~___--\\        Keeping you up to
    ',   \  ,-----|-------+-------'_____/__----~~/N Car./                   DATE
     '_   '\|     |      |~~~|Okla.|    | Tenn._/-,~~-,/             with your
       \    |Ariz.| New  |   |_    |Ark./~~|~~\    \,/S Car.               STATE!  
        ~~~-'     | Mex. |     `~~~\___|MS |AL | GA /
            '-,_  | _____|          |  /   | ,-'---~\\
                `~'~  \    Texas    |LA`--,~~~~-~~,FL\\
                       \/~\      /~~~`---`         |  \\
                           \    /                   \  |           
                            \  |                     '\\'
                             `~'""")

# Create lists  with - State Names, Capitals, # of congressional districts, order that the state joined the union. 
# Lists Copy/Pasted from https://www.chegg.com/homework-help/questions-and-answers/problem-write-program-display-information-state-typed-user-user-types-name-state-program-d-q91476752
states = [
'Alabama',
'Alaska',
'Arizona',
'Arkansas',
'California',
'Colorado',
'Connecticut',
'Delaware',
'Florida',
'Georgia',
'Hawaii',
'Idaho',
'Illinois',
'Indiana',
'Iowa',
'Kansas',
'Kentucky',
'Louisiana',
'Maine',
'Maryland',
'Massachusetts',
'Michigan',
'Minnesota',
'Mississippi',
'Missouri',
'Montana',
'Nebraska',
'Nevada',
'New Hampshire',
'New Jersey',
'New Mexico',
'New York',
'North Carolina',
'North Dakota',
'Ohio',
'Oklahoma',
'Oregon',
'Pennsylvania',
'Rhode Island',
'South Carolina',
'South Dakota',
'Tennessee',
'Texas',
'Utah',
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming'
]
capitals =[
'Montgomery',
'Juneau',
'Phoenix',
'Little Rock',
'Sacramento',
'Denver',
'Hartford',
'Dover',
'Tallahassee',
'Atlanta',
'Honolulu',
'Boise',
'Springfield',
'Indianapolis',
'Des Moines',
'Topeka',
'Frankfort',
'Baton Rouge',
'Augusta',
'Annapolis',
'Boston',
'Lansing',
'St. Paul',
'Jackson',
'Jefferson City',
'Helena',
'Lincoln',
'Carson City',
'Concord',
'Trenton',
'Santa Fe',
'Albany',
'Raleigh',
'Bismarck',
'Columbus',
'Oklahoma City',
'Salem',
'Harrisburg',
'Providence',
'Columbia',
'Pierre',
'Nashville',
'Austin',
'Salt Lake City',
'Montpelier',
'Richmond',
'Olympia',
'Charleston',
'Madison',
'Cheyenne'
]
districts =[
'7',
'1',
'8',
'4',
'53',
'7',
'5',
'1',
'25',
'13',
'2',
'2',
'19',
'9',
'5',
'4',
'6',
'7',
'2',
'8',
'10',
'15',
'8',
'4',
'9',
'1',
'3',
'3',
'2',
'13',
'3',
'29',
'13',
'1',
'18',
'5',
'5',
'19',
'2',
'6',
'1',
'9',
'32',
'3',
'1',
'11',
'9',
'3',
'8',
'1',
]
joinedNum =[
'22',
'49',
'48',
'25',
'31',
'38',
'5',
'1',
'27',
'4',
'50',
'43',
'21',
'19',
'29',
'34',
'15',
'18',
'23',
'7',
'6',
'26',
'32',
'20',
'24',
'41',
'37',
'36',
'9',
'3',
'47',
'11',
'12',
'39',
'17',
'46',
'33',
'2',
'13',
'8',
'40',
'16',
'28',
'45',
'14',
'10',
'42',
'35',
'30',
'44'
]
# Ask user for a state name - format to capitalize first letter to match lists
userState = input("Enter the name of a State you would like to learn about:  ").title()

# Find the index of that name / store in variable
indexOfState = states.index(userState)

# Get the ordinal suffix for the Joined number (eg 3rd, 42nd etc.) https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like
suffix = None
def suffix_placer():
    global suffix
    suffixList = ["th", "st", "nd", "rd"]

    if (joinedNum % 10 in [1, 2, 3] and joinedNum not in [11, 12, 13]):
        suffix = suffixList[joinedNum % 10]
    else:
        suffix = suffixList[0]
suffix_placer(joinedNum[indexOfState])
print(suffix)

# Provide report about the state. Populate by pulling the index from each list in turn
print("\n\nThe Capital of", states[indexOfState], "is", capitals[indexOfState], "it has", districts[indexOfState], "congressional districts and it is state number", joinedNum[indexOfState], "in the union!\n")

# Thank the user, demand bitcoin 
print("Thank you for using UNITED STATE FINDER!\nWe hope that you learned something new today.")

# ***Alternate solution *** create a dictionary from list - https://statisticsglobe.com/convert-multiple-lists-dictionary-python
stateInfo = [states[indexOfState], capitals[indexOfState], ]
states_dict = dict()
for i in range(len(states)):
    states_dict.setdefault(states[i],[capitals[i], districts[i], joinedNum[i]])
# print(states_dict)
# print(states_dict[userState])
# userState list
state_dictVals = states_dict[userState]

# Provide report about the state. Populate by pulling the index from each list in turn
# print("\n\nThe Capital of", userState, "is", state_dictVals[0],"it has", state_dictVals[1], "congressional districts and it is state number", state_dictVals[2], "in the union!\n")