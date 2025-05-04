alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_decode):
    output_text=""
    if encode_decode=='decode':
        shift_amount *= -1

    for letter in original_text:

        
        if letter not in alphabet:
            output_text+=letter

        else:
            shifted_possition = alphabet.index(letter) + shift_amount
            shifted_possition %= len(alphabet)
            output_text += alphabet[shifted_possition] 

    print(f"Here is the {encode_decode}d result = {output_text}")

should_countinue = True
while should_countinue:

    direction = input("Enter what do you want encode or decode ? ").lower()
    text = input("Enter yout message...").lower()
    shift = int(input("Enter your shift number."))

    caesar(original_text=text,shift_amount=shift,encode_decode=direction)
    restart = input("Do you want to continue... ?").lower()
    if restart == 'no':
        should_countinue=False
        print("Good Bye....")