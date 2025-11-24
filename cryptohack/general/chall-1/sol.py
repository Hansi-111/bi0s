#ascii
b=''
a=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in a:
    b=b+chr(i)
print(b)

##chr converts into ascii characters ord does the opposite

##hex
print(bytes.fromhex('63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'))

##base64
import base64
print(base64.b64encode(bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')))

#bytes and big integer
from Cryptodome.Util.number import *
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
