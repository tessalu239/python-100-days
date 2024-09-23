alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# def encrypt(original_text, shift_amount):
#     # print(original_text[0])
#     new_text=''
#     alphabet_shift=alphabet.copy()
#     for time in range(shift_amount):
#         temp=alphabet[time]
#
#         alphabet_shift.pop(time)
#         alphabet_shift.append(temp)
#         # print(alphabet_shift)
#     for ch in original_text:
#         new_text+=alphabet_shift[alphabet.index(ch)]
#
#     print(f"Here is the encoded result: {new_text}")

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
#method that recommended by the code
def encrypt(original_text, shift_mount):
    cipher_text=""
    for ch in original_text:
        shifted_position=alphabet.index(ch)+shift_mount
        #could get out of range, then step make sure it is in range
        shifted_position%=len(alphabet)#0-25
        cipher_text+=alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text,shift)