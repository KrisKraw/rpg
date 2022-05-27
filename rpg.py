#!/usr/bin/python3


def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  room = rooms[currentRoom]
  if "items" in room:
    availableItems = ''
    for item in room['items']:
      availableItems = availableItems + ' ' + "'" + item + "'"
    print('You see a ' + availableItems)
  print("---------------------------")
  print("you can go:")

  room = rooms[currentRoom]
  directions = ''
  for direction in room['directions']:
      directions = directions + ' ' + direction
  print(directions)

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'items'  : ['key','letter','dagger'],
                  'directions'  : {'south' : 'Kitchen','east'  : 'Dining Room','north'  : 'Library','west'  : 'Stairs'}
                },
            'Kitchen' : {
                  'items'  : ['monster'],
                  'directions'  : {'north' : 'Hall'}
                },
            'Dining Room' : {
                  'items'  : ['candle stick','bottle of vodka','potion'],
                  'directions'  : {'west' : 'Hall','south': 'Garden','north' : 'Pantry'}
               },
            'Garden' : {
                  'items'  : ['ax','shovel'],
                  'directions'  : {'north' : 'Dining Room'},
               },
            'Pantry' : {
                  'items' : ['cookie', 'rat poison'],
                  'directions'  : {'south' : 'Dining Room'}
            },
            'Library' : {
                  'items' : ['letter opener', 'bible'],
                  'directions'  : {'west' : 'Garden'}
            },
            'Stairs' : {
                  'items' : ['dagger'],
                  'directions'  : {'north' : {'Kitchen'}}
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]['directions']:
      #set the current room to the new room
      currentRoom = rooms[currentRoom]['directions'][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      #delete the item from the room
      item_index = rooms[currentRoom]['items'].index(move[1])
      del rooms[currentRoom]['items'][item_index]
      print('picked up ' + move[1])
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'items' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['items']:
    if 'dagger' in inventory or 'ax' in inventory or 'rat poison' in inventory:
        print('You killed the monster... YOU WIN!')
    else:
        print('A monster has got you... GAME OVER!')
    break