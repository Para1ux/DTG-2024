# Introductory print code to welcome user and inform them on the quiz topic
score = 0
question = 0
print("Welcome!")
print()
print("This is a quiz about the famous historic New Zealand figure Kate Sheppard.")
print("There will be 9 questions in total.")
print()

# Check if the user wants to start the quiz
start = input("Are you ready? (y) ")

while start != "y":
  print()
  print("That's not a valid answer")
  start = input("Are you ready? (y) ")
print()

# The questions of the quiz
# The first three questions are multiple choice
# Question 1
print("In what year was Kate Sheppard born?")

# The choices and expected output
print("A) 1847")
print("B) 1947")
print("C) 1850")
print("D) 1953")
print()
answer_1 = input("Answer: ")
if answer_1 == "A" or answer_1 == "a":
  print("Correct!")
  score = score+1
else:
  print("Incorrect.")
print()
question = question+1


# Question 2
print("What was Kate Sheppard famous for?")

# The choices and expected output
print("A) Her paintings when she was young.")
print("B) Giving women the right to vote in NZ.")
print("C) Being the first woman to be elected as the NZ prime minister.")
print()
answer_2 = input("Answer: ")
if answer_2 == "B" or answer_2 == "b":
  print("Correct!")
  score = score+1
else:
  print("Incorrect.")
print()
question = question+1


# Question 3
print("In what year did Kate Sheppard sadly pass away?")

# The choices and expected output
print("A) 1904")
print("B) 1914")
print("C) 1924")
print("D) 1934")
print()
answer_3 = input("Answer: ")
if answer_3 == "D" or answer_3 == "d":
  print("Correct!")
  score = score+1
else:
  print("Incorrect.")
print()
question = question+1

# MULTI-CHOICE QUESTIONS OVER
# The next three questions are true or false
# Question 4
print("True or False: Kate Sheppard was born in New Zealand.")


# User will either enter 'true' or 'false' and recieve an expected output
print()
answer_4 = input("Answer: ")
while True:
  if answer_4 == "false" or answer_4 == "False":
    print("Correct!")
    score = score+1
    break
  elif answer_4 == "true" or answer_4 == "True":
    print("Incorrect.")
    break
  else:
    print()
    print("That's not a valid answer.")
    answer_4 = input("Answer: ")
print()
question = question+1


# Question 5
print("True or False: Kate Sheppard had one son.")

# User will either enter 'true' or 'false' and recieve an expected output
print()
answer_5 = input("Answer: ")
while True:
  if answer_5 == "true" or answer_4 == "True":
    print("Correct!")
    score = score+1
    break
  elif answer_5 == "false" or answer_4 == "False":
    print("Incorrect.")
    break
  else:
    print()
    print("That's not a valid answer.")
    answer_5 = input("Answer: ")
print()
question = question+1


# Question 6
print("True or False: Kate Sheppard was part of the legislation superintendent of the WCTU.")

# User will either enter 'true' or 'false' and recieve an expected output
print()
answer_6 = input("Answer: ")
while True:
  if answer_6 == "true" or answer_6 == "True":
    print("Correct!")
    score = score+1
    break
  elif answer_6 == "false" or answer_6 == "False":
    print("Incorrect.")
    break
  else:
    print()
    print("That's not a valid answer.")
    answer_6 = input("Answer: ")
print()
question = question+1


# Question 7
print("Where was Kate Sheppard raised in?")

# User will either input answer of their choice then recieve the expected output
print()
answer_7 = input("Answer: ")
while True:
  if answer_7 == "scotland" or answer_7 == "Scotland":
    print("Correct!")
    score = score+1
    break
  else:
    print("Incorrect.")
    break
print()
question = question+1


# Question 8
print("Lets see if you can remember how to spell her name? (First name and Surname)")

# User will either input answer of their choice then recieve the expected output
print()
answer_8 = input("Answer: ")
while True:
  if answer_8.lower() == "kate sheppard" or answer_8.upper() == "Kate Sheppard":
    print("Correct!")
    score = score+1
    break
  else:
    print("Incorrect.")
    break
print()
question = question+1


# Question 9
print("What is Kate Sheppard's middle name?")

# User will either input answer of their choice then recieve the expected output
answer_9 = input("Answer: ")
while True:
  if answer_9.lower() == "wilson" or answer_9.upper() == "WILSON":
    print("Correct!")
    score = score+1
    break
  else:
    print("Incorrect.")
    break
print()
question = question+1

print("Congratulations! You have completed the quiz.")
print()
print("You have answered", score, "out of", question, "correctly.")
print("Thanks for playing!")