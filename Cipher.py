def encrypt(text,s):
    result = ""
   
    for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = input("Enter the String: ")
s = int(input("Enter the Shift Number: "))
print ("#####################")
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
l = encrypt(text,s)
print ("Cipher: " + l.upper())