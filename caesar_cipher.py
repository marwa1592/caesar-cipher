import string
def decrypt(message,shift):
 alphabet=string.ascii_lowercase
 decrypted_message=""
 for decrypted_letter in message:
   if decrypted_letter.lower() in alphabet:
      original_position=alphabet.index(decrypted_letter.lower())
      new_position=(original_position + shift)%26
      decrypted_letter=alphabet[new_position]
      if decrypted_letter.isupper():
           decrypted_letter=decrypted_letter.upper()           
           decrypted_message+=decrypted_letter                                                    
      else:
           decrypted_message+=decrypted_letter
   else: 
        decrypted_message+=letter                                            
 print(
 f"\n\nHere is the original message\n*****\n\n{decrpted_message}\n\n*****")
used_message=input("Enter a message: ")
shift_number=int(input("Enter a shift number: "))

decrypt(message=user_message, shift=shift_number)
