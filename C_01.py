print("🎲🎲 Roll it 13 🎲🎲")


while True:
  want_instructions = input("Do you want to read the instructions? ")
  
  if want_instructions == "yes":
    print("you chose yes")
  elif want_instructions == "no":
    print("you chose no")
  else:
    print("You did no pick a valid response")