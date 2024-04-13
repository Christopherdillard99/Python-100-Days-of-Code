# Zombie Apocalypse Simulator - Conditional Statements
# Ascii Art from https://ascii.co.uk/art

print('''

            ,
        _,-""-._
      ,"        ".
     /    ,-,  ,"\
    "    /   \ | o|
    \    `-o-"  `-',
     `,   _.--'`'--`
       `--`---'                    |   _)
         ,' '      _  /  _ \  ` \   _ \ |  -_)
       ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
       / /     \
      (_)))_ _,"
         _))))_,
--------(_,-._)))-------------------------------

''')
print("Welcome to the Zombie Apocalypse.")
print("Your mission is make it out of Phase 1 alive.")


print('It\'s a beautiful spring day and you decide to go out for a run while you listen to your favorite playlist. About a minute into the run you notice that your shoes are untied and crounch down to fix them. But... wait. Uhhh... as you get up you notice someone is running towards you full-throttle in your peripheral, but something\'s off. They\'re a ZOMBIE?!?!.') 

choice1 = input('There\'s a shovel two feet to your right. Do you pick up the shovel and fight back? OR since you already have your running shoes on do you run back home to safety? Type "fight" or "run" \n').lower()
if choice1 == "fight":
  choice2 = input('You finished off the zombie and quickly run back home. After locking the door, you call your friend to ask if he\'s seen any zombies around. Apparently you missed the memo and he says his pilot friend has a plane that is leaving in 30 mins to escape to a remote island and you need to rush over RIGHT NOW to the address he gave you. Your car is near empty but you should have enough gas to make it there on time. Do you drive over to catch the flight or do you stay home and wait for more news. Type "drive" to catch the flight with your friend. Type "wait" to stay home. \n').lower()
  if choice2 == "drive":
    print('''

           .--------.
      ____/_____|___ \___
     O    _   - |   _   ,*
      '--(_)-------(_)--' 
    ''')
    choice3 = input('You make it just barely in time, but your friend\'s grandma tagged along and there\'s only one seat left. Do your offer up your seat to save grandma or try to convince everyone that she lived a good, long life and you should take her place. Type "stay" to give up your seat or "argue" to leave grandma behind. \n').lower()
    if choice3 == "stay":
      choice4 = input('You are instructed to wait in the pilot\'s house by the airstrip till tomorrow afternoon for the pilot and your friend to come back for you. It\'s nightfall now and you\'re very hungry, but all the pilot left behind was expired milk and an empty pantry. Do you sleep off the hunger till tomorrow or drive to the supermarket that you remember seeing just down the road? Type "sleep" to stay in the pilot\'s house or "leave" to drive out for some food. \n').lower()
      if choice4 == "sleep":
        print("You made the right choice. You woke up very hungry, but you trust your friend. Later that day, you hear a plane approaching the landing strip and quickly run towards the aircraft. Congratulations, you survived phase 1 of the Zombie Apocolypse and are now heading to the island.")
        print('''
                                         _       
                                        | |      
          ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
         / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
        | (_| (_) | | | | (_| | | | (_| | |_\__ \
         \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                          __/ |                  
                         |___/         
        ''')
      else: 
        print("There are no zombies in sight, so you quickly drive out to the store. 10 minutes into the ride, you think you might have taken a wrong turn and try to open up Google Maps and search the store to no avail. Cellular networks are already down and you are now lost with an empty tank of gas. You're stranded on the side of the road and try to break into a house while escaping zombies. The owners mistake you for a zombie and kill you.")
        print('''
          __  __ _         _               ______    _ _          _ 
         |  \/  (_)       (_)             |  ____|  (_) |        | |
         | \  / |_ ___ ___ _  ___  _ __   | |__ __ _ _| | ___  __| |
         | |\/| | / __/ __| |/ _ \| '_ \  |  __/ _` | | |/ _ \/ _` |
         | |  | | \__ \__ \ | (_) | | | | | | | (_| | | |  __/ (_| |
         |_|  |_|_|___/___/_|\___/|_| |_| |_|  \__,_|_|_|\___|\__,_|

        ''')
    else:
      print("Everyone thinks you're selfish and leaves you behind to never come back. You are angry and decide to drive back home and eventually find that your neighborhood is completely overrun by zombies. Your car is quickly swarmed and you are eventually eaten alive.")
      print('''
        __  __ _         _               ______    _ _          _ 
       |  \/  (_)       (_)             |  ____|  (_) |        | |
       | \  / |_ ___ ___ _  ___  _ __   | |__ __ _ _| | ___  __| |
       | |\/| | / __/ __| |/ _ \| '_ \  |  __/ _` | | |/ _ \/ _` |
       | |  | | \__ \__ \ | (_) | | | | | | | (_| | | |  __/ (_| |
       |_|  |_|_|___/___/_|\___/|_| |_| |_|  \__,_|_|_|\___|\__,_|

      ''')
  else:
    print("Your neighborhood is quickly overrun with zombies and all electricity is lost so... no more news updates :(. Later that night, you wake up to zombies attacking you.")
    print('''
      __  __ _         _               ______    _ _          _ 
     |  \/  (_)       (_)             |  ____|  (_) |        | |
     | \  / |_ ___ ___ _  ___  _ __   | |__ __ _ _| | ___  __| |
     | |\/| | / __/ __| |/ _ \| '_ \  |  __/ _` | | |/ _ \/ _` |
     | |  | | \__ \__ \ | (_) | | | | | | | (_| | | |  __/ (_| |
     |_|  |_|_|___/___/_|\___/|_| |_| |_|  \__,_|_|_|\___|\__,_|

    ''')
else:
  print("You never finished tying your laces and tripped and fell. You were eaten by the zombie.")
  print('''


                         ,////,
                         /// 6|
                         //  _|
                        _/_,-'
                   _.-/'/   \   ,/;,
                ,-' /'  \_   \ / _/
                `\ /     _/\  ` /
                  |     /,  `\_/
                  |     \'
  pb  /\_        /`      /\
    /' /_``--.__/\  `,. /  \
   |_/`  `-._     `\/  `\   `.
             `-.__/'     `\   |
                           `\  \
                             `\ \
                               \_\__
                                \___)
    __  __ _         _               ______    _ _          _ 
   |  \/  (_)       (_)             |  ____|  (_) |        | |
   | \  / |_ ___ ___ _  ___  _ __   | |__ __ _ _| | ___  __| |
   | |\/| | / __/ __| |/ _ \| '_ \  |  __/ _` | | |/ _ \/ _` |
   | |  | | \__ \__ \ | (_) | | | | | | | (_| | | |  __/ (_| |
   |_|  |_|_|___/___/_|\___/|_| |_| |_|  \__,_|_|_|\___|\__,_|

  ''')