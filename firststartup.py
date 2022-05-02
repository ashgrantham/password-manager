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

write_key()