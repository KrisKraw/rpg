#!/usr/bin/python3

## A dictionary linking a room to other rooms
rooms = {
            'Hall' : {
                  'items'  : ['key','letter','dagger'],
                  'directions'  : {'south' : 'Kitchen','east'  : 'Dining Room','north'  : 'Library','west'  : 'Stairs'}
                },
            'Kitchen' : {
                  'items'  : ['cake'],
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