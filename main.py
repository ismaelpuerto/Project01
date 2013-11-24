import random

converter = {'rock':0, 'Spock':1, 'paper':2, 'lizard':3, 'scissors':4}

    
#while True:
#    value = raw_input('Chose number:')
#    try:
#        value = int(value)
#    except ValueError:
#        print 'Valid number, please'
#        continue
#        continue
#    if 0 <= value <= 4:
#        break
#    else:
#        print 'Valid range, please: 0-4'    

def number_to_name(number):
    if (number in converter.values()):
        return converter.keys()[number]
    else:
        print ("Error: There is no '" + str(number) + "' in " + str(converter.values()) +'\n')
def name_to_number(name):
    if (name in converter.keys()):
        return converter[name]
    else:
        print ("Error: There is no '" + name + "' in " + str(converter.keys()))



def rpsls(name):
    player_number = name_to_number(name)
    # converts name to player_number using name_to_number

    comp_number = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
   
    result = (player_number - comp_number) % 5
    # compute difference of player_number and comp_number modulo five

    # Announce the opponents to each other
    print 'Player chooses ' + name
    print 'Computer chooses ' + number_to_name(comp_number)
   
    # Setup the game's rules
    win = result == 1 or result == 2
    lose = result == 3 or result == 4
   
    # Determine and print the results
    if win:
        print 'Player wins!\n'
    elif lose:
        print 'Computer wins!\n'
    else:
        print 'Player and computer tie!\n'


# Main Program -- Test my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
