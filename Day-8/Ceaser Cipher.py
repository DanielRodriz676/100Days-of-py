from operator import index

encode = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while encode:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input('Type your message:\n')
    shift_n = int(input('Type the shift number:\n'))
    if mode == 'encode':
        message_e = ''
        for x in message:
            message_e += alphabet[alphabet.index(x) + shift_n]
        print(f"Here's the encoded result: {message_e}")
    else:
        message_e = ''
        for x in message:
            message_e += alphabet[alphabet.index(x) - shift_n]
        print(f"Here's the decoded result: {message_e}")

    if input("Type 'yes' if you want to go again. Otherwise type 'no'.") == 'yes':
        print()
    else:
        encode = False