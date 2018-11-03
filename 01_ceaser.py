letters='abcdefghijklmnopqrstuvwxyz'


def main():

	choice=input("Do you wish to encrypt or decrypt?")
	if choice=="encrypt":
		encrypt()
	elif choice=="decrypt":
		decrypt()
def encrypt():
	message=input("Enter the encrption code:- ")
	cipher = ''
	for letter in message: 
	  if letter in letters:
                position=(letters.find(letter) + 3) % 26
                cipher +=letters[position]
	  else:
                cipher +=letter
	print(cipher)
	return cipher
def decrypt():
	message=input("Enter the encrption code:- ")
	cipher = ''
	for letter in message: 
	  if letter in letters:
                position=(letters.find(letter) - 3) % 26
                cipher +=letters[position]
	  else:
                cipher +=letter
	print(cipher)
	return cipher
main()

