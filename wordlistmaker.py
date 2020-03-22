import random
from colorama import Fore
from itertools import product
First = input(Fore.GREEN + "First name: ")
Sur = input("Surname: ")
Age = input("Age: ")
Address = input("Address: ")
Spec = input("Special character(s): ")
def allwords(chars, length):
	for letters in product(chars, repeat=length):
		yield ''.join(letters)
def main():
	letters = First + Sur + Age + Address + Spec
	for wordlen in range(7, 40):
		for word in allwords(letters, wordlen):
			print(word)
if __name__=="__main__":
	main()
