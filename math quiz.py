import random

score = 0

for _ in range(10):
  num1 = random.randint(1,15)
  num2 = random.randint(1,8)
  answer = num1 * num2
  user_answer = int(input(f"What is {num1} * {num2}? "))

  if user_answer == answer:
    print("Correct!")
    score += 1
  else:
    print("Incorrect!")
  print(f"Score: {score}")
print(f"Game Over. Your final score is {score}!")