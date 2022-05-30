letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
direction=input('if you want to encode "type encode" or if you want to decode "type decode" \n')
message=input("type your message \n").lower()
shift=int(input("type the shift amount \n"))
if direction=="encode":
    def encode(plain_text,shiftamount):
        encoded_message=""
        for text in plain_text:
           position=letters.index(text)
           new_position=position+shiftamount
           encoded_message +=letters[new_position]
        print(encoded_message)        
    encode(message,shift)
if direction=="decode":
    def decode(plain_text,shiftamount):
        decoded_message=""
        for text in plain_text:
            position=letters.index(text)
            new_position=position-shiftamount
            decoded_message +=letters[new_position]
        print(decoded_message)        
    decode(message,shift)  
  
    