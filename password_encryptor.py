import base64

exit = False

while not exit:
    print("Encode Password - 1")
    print("Decode Password - 2")
    print("Quit = q")
    print("")

    user = input("Your Choice: ")
    print("")

    #encode
    def encrypt_pass(password):
        encrypt_pass = base64.b64encode(password.encode())
        print(f"Encrypt password ==> {encrypt_pass}")
        
    #decode

    def decode_pass(password):
        decode_byte = base64.b64decode(password)
        decode_data = decode_byte.decode()
        print(f"Decode password ==> {decode_data}")
        
    if user == "1":
        user_pass = input("Enter Your Password: ")
        encrypt_pass(user_pass)

    elif user == "2": 
        encode_string = input("Enter the base64 string: ")
        decode_pass(encode_string)

    elif user == "q":
        exit = True

    else:
        print("Invalid Number")





