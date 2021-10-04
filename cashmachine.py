# Cashmachine project
# Takes a PIN and number and dispenses cash if PIN correct and 
# balance available.
# QA

master_pin = "5678"
balance = 99999.0
pin = "xxxx"

def check_pin(pin):
    if pin == master_pin:
        return True
    else:
        return False

def give_money(amount):
    global balance
    balance -= amount
    print(f"Giving you £{amount} of moolah. You have £{balance} remaining.")

def atm(pin, amount):
  pinok = check_pin(pin)
  if pinok == True:
      if balance - amount > 0:
        give_money(amount)
        return True
      else:
          print(f"Alas, not enough money. You have only £{balance} left.")
          return False
  else:
      print(f"NOT AUTHORISED. Are you sure you are you?   (in case you forgot, your pin was {master_pin})")
      return False

# Keep looping around until nothing is entered (empty string)
while pin != "":
  pin = input("What is your PIN? ")
  if pin != "":
    amount = float(input(f"How much lovely money do you want? (You have £{balance} remaining)  £"))
    atm(pin, amount)
