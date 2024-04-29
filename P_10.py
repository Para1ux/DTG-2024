def statement_generator(statement, decoration):
  print(f"/n{decoration * 5} {statement} {decoration * 5}")

def instructions():
  statement_generator(statement="instructions", decoration: 
  "-")

  print('''
instructions go here.
-instruction 1
-instruction 2
-etc
  ''')
want_instructions = input("Press <enter> to read the instructions " "or any key to continue ")

if want_instructions == "":
  instructions()

print("program continues")

def get_filetype():
  response = input("File type: ").lower()


  if response == "xxx" or response == "i":
    return response

  elif response in ['integer', 'int']:
    return "integer"

  else:
    print("Please enter a valid file type")

while True:
  file_type = get_filetype()
  print(f"You chose {file_type}")

  if file_type == "xxx":
    break


