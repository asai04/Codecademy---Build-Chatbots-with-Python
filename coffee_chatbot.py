#coffee_bot()
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a {} {}!".format(size,drink_type))
  name = input("Can I get your name please?\n")
  print("Thanks, {}! Your drink will be ready shortly".format(name))

#print_message()
def print_message():
  print('Im sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

#get_size
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

# get_drink_type()
def get_drink_type():
  res = input('''What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte \n ''')
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#order_latte()
def order_latte():
  res = input('''And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk \n''')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return get_drink_type()

#Running coffee_bot()
coffee_bot()










