'''
This short program produces an SHA256 hash of a variable.
'''
import hashlib

def sha256():
    message = ''
    while message != 'quit':
        message = input('Please enter your message: ')
        print(hashlib.sha256(message.encode('UTF-8')).hexdigest())

def sha256_with_nonce():
    message = input('Please enter your message: ')
    nonce = 0
    while nonce != 'quit':
        nonce = input('Please enter a 10-digit nonce: ')
        try:
            to_hash = message * int(nonce)
            print(hashlib.sha256(to_hash.encode('UTF-8')).hexdigest())
        except:
            print('Invalid nonce')

mode = input('Nonce mode? [y/n] ')

if mode == 'n':
    sha256()
elif mode == 'y':
    sha256_with_nonce()

