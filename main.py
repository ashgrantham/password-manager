
#imports
import os
from cryptography.fernet import Fernet
import socket
from datetime import datetime
#define section
def write_key():
  key = Fernet.generate_key() #generates key
  with open('key.key', 'wb') as key_file:
    key_file.write(key)#Stores the key in a key.key file as bytes format
def load_key(): #loads key file
  return open("key.key", "rb").read() #reads key file in bytes/bits

def encrypt(filename, key):
  f = Fernet(key)
  with open(filename, "rb") as file:
    file_data = file.read()
    encrypted_data = f.encrypt(file_data)
  with open(filename, 'wb') as file:
    file.write(encrypted_data)
    
def decrypt(filename, key):
  f = Fernet(key)
  with open(filename, 'rb') as file:
    encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
  with open(filename, "wb") as file:
    file.write(decrypted_data)
ampwd = os.environ['masterpassword']
count = 0
print("Welcome to the password manager!")
while True:
  if count <3:
    mpwd = input("Please enter the master password: ")
    if mpwd == ampwd:
      break
    else:
      count += 1
      if count <3:
        print("incorrect, try again")
      
      
    
  else:
    print("too many failed attempts, try again later")
    f = open('.key', "a")
    f.write('Someone attempted to login and failed all attempts')
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "222.152.174.181":
      ip2 = ", home computer used "
    else:
      ip2 = ", random ip address "
    f.write(' the ip address for the user was {} {}'.format(ip, ip2))
    time = datetime.now()
    f.write(' time of breach was {}\n'.format(time))
    f.close()
    quit("Goodbye!")
    
#write_key() #Uncomment to write a new key if no key exists
key = load_key() # loading key
file = "passwords.txt"
#encrypt(file, key) #to encrypt
#decrypt(file, key) # to decrypt
while True:
  mode = input("enter the mode (q to quit, add or decrypt): ").lower()
  if mode == "q":
    break
  elif mode == "add":
    try:
      decrypt(file, key)
      pwd = input("enter a password: ")
      email = input('enter an email/username if applicable: ')
      webapp = input('enter the website or app: ')
      string = "password: {} | email: {} | website/app: {}".format(pwd, email, webapp)
      f = open('passwords.txt', 'a')
      f.write('\n' + string)
      f.close()
      encrypt(file, key)
      
    except:
      pwd = input("enter password: ")
      email = input('enter an email/username if applicable: ')
      webapp = input('enter the website or app: ')
      string = "password: {} | email: {} | website/app: {}".format(pwd, email, webapp)
      f = open('passwords.txt', 'a')
      f.write(string)
      f.close()
      encrypt(file, key)
      
  elif mode == "decrypt":
    try:
      decrypt(file, key)
      f = open('passwords.txt', 'r')
      print(f.read())
      f.close()
      encrypt(file, key)
    except:
      print("There is nothing to decrypt! try adding a new password.")
