import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = True

def caesar(direction, text, shift):
  
  print(art.logo)
  print()
  print()
  
  if shift > 26:
    shift %= 26
    
  if direction == "encode":
    encrypted_message = ""
    for letter in text:
      if letter not in alphabet:
        encrypted_message += letter
      elif letter in alphabet:
        shift_from_index = 0
        shift_from_index = alphabet.index(letter)
        encrypted_message += alphabet[shift_from_index + shift]
    print(f"The encoded text is: {encrypted_message}")
    print()
    print()
    
  elif direction == "decode":
    decrypted_message = ""
    for letter in text:
      if letter not in alphabet:
        decrypted_message += letter
      elif letter in alphabet:
        shift_from_index = 0
        shift_from_index = alphabet.index(letter)
        decrypted_message += alphabet[shift_from_index - shift]
    print(f"The encoded text is: {decrypted_message}")
    print()
    print()

  restart_answer = input("Do you want to en/decode another message? Y or N: ").lower()
  print()
  print()
  
  if restart_answer == "n":
    restart = False

### ### ### ###


while restart == True:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(direction, text, shift)