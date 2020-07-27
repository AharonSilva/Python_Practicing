message = input()
decripted = []
key = sum(int(input()).to_bytes(2, 'little'), 0)
print(key)
for letter in message:
    decripted.append(chr(ord(letter) + key))
print(''.join(decripted))
