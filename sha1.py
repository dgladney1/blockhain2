from urllib.request import sys, urlopen, hashlib;
import argparse

parser = argparse.ArgumentParser(description='Input Hash')
parser.add_argument('input')
args = parser.parse_args()

pswcount = 0
print("Cracking:", args.input)
for password in str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8').split('\n'):
    pswcount += 1
    [print("Found! Password is \""+str(password)+"\" in "+ str(pswcount)+ " attempts"), quit()] if (hashlib.sha1(bytes(password, 'utf-8')).hexdigest()) == args.input else print("We're sorry, password was not found.") if password == "" else print("Not Found! On to next (Attempt "+str(pswcount)+ ")")