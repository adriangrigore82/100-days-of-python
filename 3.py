print('''
    _____  
^..^     \9
(oo)_____/ 
   WW  WW
''')
print("Escape the farm")
print("\nYour mission is to help Prikoke stay alive.") 
choice_1 = input('\nPrikoke jumped the farm fence and can either take the main road or run through the fields: Please type one option: "road" or "field".\n\n').lower()
if choice_1 == "field":
  choice_2 = input ('\nPrikoke manages to evade being spoted and, as he reaches the end of the field, he faces a forest. Should he go through the "forest" or "go around"?\n\n').lower()
  if choice_2 == "forest":
    choice_3 = input('\nPrikoke ventures into the forest and encounters a pack of wolves.Fortunately for Prikoke, they were vegan, already stuffed with avocados. Lucky pig ! He continues to a river, but Prikoke cannot swim: He can either: go across a wonky "bridge", "go around" or "turn back"\n\n').lower()
    if choice_3 == "bridge":
      print ('''\nPrikoke has escaped to freedom ! 
          CONGRATULATIONS !
          _____
^..^     \9
(oo)_____/
    WW WW''')
    elif choice_3 == "go around":
      print ("Prikoke died of exposure. What a waste of pork! GAME OVER !")
    elif choice_3 == "turn back":
      print ("/nPrikoke went back to the sausage factory/n")
  else:
    print ('Prikoke continues across the field and falls into a hole. Tough luck! GAME OVER!')
else:
  print ("The farmer spots Prikoke and turns him into delicious saussages. GAME OVER !")
