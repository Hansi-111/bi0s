###xor
#starter
def xor(a,b):
    return a^b
s='label'
b=''
for i in s:
    c=xor(ord(i),13)
    b=b+chr(c)
print(b)
#property
KEY1 = bytes_to_long(bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'))
KEY2KEY1 = bytes_to_long(bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'))
KEY2KEY3 = bytes_to_long(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'))
FLAGKEY1KEY3KEY2 = bytes_to_long(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'))
x=xor(FLAGKEY1KEY3KEY2,KEY2KEY3)
print(long_to_bytes(xor(x,KEY1)))
