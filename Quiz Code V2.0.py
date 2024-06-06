# Time = to make the program wait for added effect
import time

# ------------------------------------------------------
# Introduction to the quiz and ask user for their username

score = 0

print("Hello and welcome to the Kate Sheppard Quiz!")
time.sleep(2)
print()

username = input("To get started, type your username: ")
print()
print(f"Welcome {username} to the quiz that'll test your knowledge on Kate Sheppard.")
time.sleep(2.5)
print()

while True:
  response = input("Are you ready? (yes/no): ").strip().lower()
  if response == 'yes':
      print("Great! Let's get started.")
      break
  else:
      print("Okay, I'll ask again.")
print()
# -----------------------------------------------------
# Questions and answers ordered corresponding to the order of the questions

questions = [
    {
        "question": "What is Kate Sheppard's middle name?",
        "answers": ["Willy", "Wilson", "Wilbur", "William"],
        "correct_index": 2
        
    },
    {
        "question": "When did Kate Sheppard pass away?",
        "answers": ["1987", "1924", "1934", "1904"],
        "correct_index": 3
    },
    {
        "question": "Where was Kate Sheppared raised and born in?",
        "answers": ["Australia", "Paris", "England", "Luxembourg"],
        "correct_index": 3
    },    
    {
        "question": "When was Kate Sheppard born?",
        "answers": ["1847", "1787", "1897", "2000"],
        "correct_index": 1
    },
    {
        "question": "How many spouses did Kate Sheppard have in her lifetime?",
        "answers": ["2", "3", "4", "5"],
        "correct_index": 1
    },
    {
        "question": "What is Kate Sheppard's nationality?",
        "answers": ["British", "Welsh", "NZ", "Chinese"],
        "correct_index": 3
    },
    {
        "question": "Who was Kate Sheppared inspired by?",
        "answers": ["Chris Hansen", "Mary Leavitt", "Bruce Willis", "Mary Rose"],
        "correct_index": 2
    },
    {
        "question": "What is Kate Sheppard famous for?",
        "answers": ["Helping poverty.", "Being the first to climb Mt. Everest.", "Giving the women the right to vote.", "Having 30 children."],
        "correct_index": 3
    }
]

# -----------------------------------------------------
# Randomize the questions (and answers) and give the expected output for each question

for q in questions:
    correct = q["answers"][q["correct_index"]]
    q["correct_index"] = q["answers"].index(correct)

for i, q in enumerate(questions):
    print()
    print(f"q{i+1}: {q['question']}")
    for j, answer in enumerate(q["answers"]):
        print(f"{j+1}. {answer}")
    user_answer = int(input("Choose an answer (1-4): "))
    if user_answer == q["correct_index"]:
        score = score + 1
    else:
        print(f"Incorrect. The correct answer is {q['answers'][q['correct_index']]}.")
# -----------------------------------------------------
# Display the final score and a message based on the score

print(f"Congratulations {username}! You have finished the quiz.")
print()
time.sleep(1)
print("Your final score is...")
time.sleep(1)
print(f"{score} out of 8 questions.")