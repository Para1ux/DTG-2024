error = "Please enter a number more than 0/n"
while True:

  try:
    width = float(input("Width: "))

    if width > 0:
         break
    else:
         print(error)

  except ValueError:
    print(error)