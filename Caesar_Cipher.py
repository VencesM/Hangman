alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction): 
  if direction == "encode": 
    cipher_text = ''
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")
  elif direction == "decode": 
    plain_text = ''
    for letter in text: 
      position = alphabet.index(letter)
      new_postion = position - shift
      plain_text += alphabet[new_postion]
    print(f"The decoded text is {plain_text}")





#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
print('''
    This program decodes and encodes words, the shift number can go only up to 30
      ''')
is_run = True
while is_run:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text=text, shift=shift, direction=direction)

  run_again = input("Do you wish to continue: Yes or No? ").lower()
  if run_again == "no": 
    print("GOODBYE!")
    is_run = False



