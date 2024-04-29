def num_check(question):
  
  error = "Please enter a number more than 0/n"
  while True:
  
    try:
      response = float(input(question))
  
      if response > 0:
           return response
      else:
           print(error)
  
    except ValueError:
      print(error)

for item in range (0, 2):
width = num_check("Width: "")
print(Width)

for item in range (0, 2):
height = num_check("height: "")
print(height)