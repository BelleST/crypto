
#base64
import base64
import codecs

cipher = b'Q29uZ3JhdHVsYXRpb25zOm9janB7emtpcmp3bW8tb2xsai1ubWx3LWpveGktdG1vbG5ybm90dm1zfQ=='
de_b = base64.b64decode(cipher)
print(de_b)

#替换base字母表


dict={0: 'J', 1: 'K', 2: 'L', 3: 'M', 4: 'N', 5: 'O', 6: 'x', 7: 'y', 8: 'U', 9: 'V', 10: 'z', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: '7', 20: '8', 21: '9', 22: 'P', 23: 'Q', 24: 'I', 25: 'a', 26: 'b', 27: 'c', 28: 'd', 29: 'e', 30: 'f', 31: 'g', 32: 'h',33: 'i', 34: 'j', 35: 'k', 36: 'l', 37: 'm', 38: 'W', 39: 'X', 40: 'Y', 41: 'Z', 42: '0', 43: '1', 44: '2', 45: '3', 46: '4', 47: '5', 48: '6', 49: 'R', 50: 'S', 51: 'T', 52: 'n', 53: 'o', 54: 'p', 55: 'q', 56: 'r', 57: 's', 58: 't', 59: 'u', 60: 'v', 61: 'w', 62: '+', 63: '/', 64: '='}
base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
cipher='FlZNfnF6Qol6e9w17WwQQoGYBQCgIkGTa9w3IQKw'
res=''
for i in range(len(cipher)):
    for j in range(64):
        if(dict[j]==cipher[i]):
            res+=base64_list[j]
print(res)
flag=base64.b64decode(res)
print(flag)
#b'BJD{D0_Y0u_kNoW_Th1s_b4se_map}'

#hex to ascii
h = '424a447b57653163306d655f74345f424a444354467d'
asc = codecs.decode(h,'hex')
print(asc)

#base32
cipher_32 = b'J5XGY6JAN5XGKIDTORSXAIDBO5QXSOSRGI4XKWRTJJUGISCWONMVQUTQMIZDK6SPNU4WUYLOII3WK3LUOBRW24BTMJLTQ5DCGJ4HGYLJGF2WEV3YGNGFO4DWMVDWW5DEI4YXMYSHGV4WE3JZGBSG2ML2MZIT2PI='
de_b32 = base64.b32decode(cipher_32)
print(de_b32.decode('ascii'))




