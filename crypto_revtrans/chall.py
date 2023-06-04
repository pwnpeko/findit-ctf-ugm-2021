flag = 'FindITCTF{REDACTED}'

def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
   
   reversetext =''
   ciphertext = ''
   i=len(plaintext)-1
   while i >= 0:
      reversetext = reversetext + plaintext[i]
      i=i-1
   

   for index in sorted(order.keys()):
      for part in split_len(reversetext, len(key)):
         try:ciphertext += part[order[index]]
         except IndexError:
            continue
        
            
   return ciphertext



print(encode('4321', flag))