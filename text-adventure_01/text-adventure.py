
print(r'''
 
                 _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                              ~
             ~

''')

print('''
   ▄▄▄▄▀ █▄▄▄▄ ▄█         ▄█    ▄▄▄▄▄   █     ▄███▄      ▄▄▄▄▄   
▀▀▀ █    █  ▄▀ ██         ██   █     ▀▄ █     █▀   ▀    █     ▀▄ 
    █    █▀▀▌  ██         ██ ▄  ▀▀▀▀▄   █     ██▄▄    ▄  ▀▀▀▀▄   
   █     █  █  ▐█         ▐█  ▀▄▄▄▄▀    ███▄  █▄   ▄▀  ▀▄▄▄▄▀    
  ▀        █    ▐          ▐                ▀ ▀███▀              
          ▀                                                      
                                                              ''')
print("You wake up on a boat. Standing you see that you are in the middle of no where on a small dingy pirate boat.")
answer_1 = input("You see three islands around you. A triangular one. A rectangular one. A circular one. Which do you take your boat to? T for triangular - C for circular - and - R for rectangular: ").lower()

if (answer_1 == "r"):
  print("You arrive at the rectangular island. Looking straight, you are met with a dense   forest. Too dense to walk through. Looking to the left and right the island makes sharp   turns. To the left you can see a bunch of sharp rocks and to the right you think you    can hear crying.")
  
  answer_02_rect = input("Do you go (L) left or (R) right? ").lower()
  if (answer_02_rect == "l"):
    print("You walk to the left side towards the sharp rocks. When you're just about there, a bird chirps loudly next to you in a tree and makes you trip. You fall right into the sharp rocks. You are dead.")
  elif (answer_02_rect == "r"):
    answer_03_rect = input(("You walk to the right and cautiously turn around the bend. You see a crying baby squirrel and behind it is a river and across the river you can see a hut with it's lights on. Do you (cts) console the squirrel or (satr) swim across the river?")).lower()
    if (answer_03_rect == "cts"):
      print("You decide to console the squirrel. You pick it up and rock it back and forth. You whisper to it and sing to it. The crying stops and it starts to giggle. It snuggles in your chest. You close your eyes and stay in the moment. The squirrel is so cute after all. Suddenly, the squirrel jumps up and says to you in a human voice, 'Thank you human! Here is your gold!’ YOU WIN.")
      print('''
      ██    ██ ██ ██    ██     ██     ██    ████   ██ ██
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ ''')

    elif (answer_03_rect == "satr"):
      print("You decide to swim and leave the squirrel behind. You jump in the water ready to break for the other side, the cries behind you are getting fainter. Getting about halfway across the river you feel something pull at your boots under the water. Before you have time to react again, there it is again. And again. And again. Before you know it, as you look around you see red water floating all around you. You are screaming in pain. Piranha’s start jumping up and eating your face. You're dead.")
    
elif (answer_1 == "c"):
  print("You arrive at the circular island. The edges are nice rounded curves and you can see fairly far around the bend. Straight ahead there is a beautiful waterfall and you can hear singing. To the right there is a door on the that is attached to a rock, almost as if it's a cave's entrance.")
  answer_02_circ = input("Do you go (s) straight or (r) right? ").lower()
  
  if (answer_02_circ == "s"):
    answer_03_circ = input(("You head straight for the waterfall and when you get to it, you go into the water and you are met with a door attached to the mountain behind it. There are drawings etched into the rock. On the left side it shows three dogs and on the right side it shows three cats. They seem to be fighting each other. Above the door is a sign that says: 'In one word, what does my sketch mean?'")).lower()
    if (answer_03_circ == "war"):
      answer_04_circ = input("The door enters and upon entrance the world vanishes left behind by darkness. You can't see or feel anything but you can hear a voice that asks you... What is more important to you, (k) knowing or (s) seeking?").lower()
      if(answer_04_circ == "k"):
        answer_05_circ = input("You say knowing. The voice grunts in acknowledgment. You start to rise upwards. You feel like your neck is about to snap by the force you feel. You enter a domain. Completely void of light and a few feet ahead of you lies a puddle of water. You go up to it. Do you (d) drink it or (b) bathe in it?").lower()
        if (answer_05_circ == "b"):
          print("You bathe in it. You hear the voice again and it says, 'Seeing the truth and experiencing the truth are two different things.' You take your clothes off, and slowly walk into the puddle. It’s warm. Suddenly you see everything. Everything that has happened and will happen. You are stuck forever. The voice says 'You are now my heir. The prince of the future. Behold the truth and live on protecting it.'")
        elif( answer_05_circ == "d"):
          print("You drink it. You hear the voice again and it says, 'Seeing the truth and experiencing the truth are two different things.' You feel all the emotions felt by all the creatures of all time. You can't handle it and you die.")
      elif (answer_04_circ == "s"):
        print("You say seeking. The voice grunts in acknowledgement. You start to fall. For what feels like forever. Until you open your eyes. Your in your bed. What was that a dream?")
        
  elif (answer_02_circ == "r"):
    answer_06_circ = input("Heading to the right you get to the door and open it up with no hesitation. You are met with a snarl and a creature made entirely of bones makes an appearance. They are holding a sword and a shield. Looking around you see another (sword) sword on the ground but it's a little far, you have to get in close to the monster to use it. You can use your (fist) fist to punch the creature or you can throw a (br) big rock at it that lies beside your foot?").lower()
    if (answer_06_circ == "sword"):
      print("You decide that going for the sword is the right decision but you'd be wrong because the monster gets there first and slices you. You are dead.")
    elif (answer_06_circ == "br"):
      print("You decide that not moving and throwing the rock beside you in the best option but the monster dodges the rock and once you threw it, you have nothing left to defend yourself with. The skeleton comes to you quickly and slices you. You are dead.")
    elif(answer_06_circ == "fist"):
      print("You decide that punching the monster is the best bet. You come in close and wind up the strongest punch of your life. You connect, you feel the bones breaking throughout the monsters body. He's down for the count and not moving. Behind him you find the treasure. You win!")
      print('''
      ██    ██ ██ ██    ██     ██     ██    ████   ██ ██
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    
   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ ''')
    
    
if (answer_1 == "t"):
  print("A giant whirlpool appears as you float by. You are sucked in and you die.")





#### 
print()
####

# print("You arrive at a beach. To the left is a jungle, the right is a cave.")

# choice_01 = input("Do you want to go left or right? ")
# choice_01.lower()

# if choice_01 == "left":
#   print(f"You've chosen {choice_01}.")
#   print()
#   print()

