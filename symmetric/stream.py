import codecs
import string
from itertools import cycle
from z3 import *
#z3-solver，已知部分明文和密文，用z3-solver建立方程，爆破key，并尝试其是否为正确的key
def z3key(out,plain):
    #out.append((out[i+1] + ((out[i] * ord(plaintext[i])) ^ (key+out[i+1]))) ^ (key*out[i]))
    for count in range(2,78):
        key=BitVec('key',count)
        s=Solver()
        for i in range(8):
            s.add(((out[i + 1] + ((out[i] * ord(plain[i])) ^ (key + out[i + 1]))) ^ (key * out[i]))==out[i+2])
        s.check()
        res=s.model()
        print(res)
        res = res[key].as_long().real
        print(res)
        f=open('conversation','r').readlines()
        x=[]
        for j in f:
            x.append(j.strip())
        flag=''
        for j in range(1,len(x),2):
            li=x[j].split(' ')
            for k in range(1,len(li)):
                li[k]=eval(li[k])
            for k in range(1,len(li)-2):
                try:
                    flag += chr(((res + li[k + 1]) ^ (((res * li[k]) ^ li[k + 2]) - li[k + 1])) // li[k])
                except:
                    break
        if 'watevr{' in flag:
            print(flag)
            break


# break repeating-key [xorz]

##计算a,b之间的汉明距离res
# def haming(a,b):
#     res = 0
#     for x,y in zip(a,b): #打包为元组的列表，个数与最短的一致
#         res += bin(ord(x)^ord(y)).count(1) #异或之后计算1的数量即两个字母之间的汉明距离
#     #print(res)
#     return res
#
#
# def break_single_key_xor(text):
#     key = 0
#     possible_space = 0
#     max_possible = 0
#     letters = string.ascii_letters # 所有的大小写英文字母
#     for a in range(0,len(text)):
#         maxpossible = 0
#         for b in range(0,len(text)):
#             if(a == b):
#                 continue
#             c = ord(text[a])^ord(text[b])
#             if chr(c) not in letters and c!=0:
#                 continue
#             maxpossible += 1
#         if maxpossible>max_possible:
#             max_possible = maxpossible
#             possible_space = a
#     key = ord(text[possible_space])^0x20
#     return chr(key)
#
# cipher = '49380d773440222d1b421b3060380c3f403c3844791b202651306721135b6229294a3c3222357e766b2f15561b35305e3c3b670e49382c295c6c170553577d3a2b791470406318315d753f03637f2b614a4f2e1c4f21027e227a4122757b446037786a7b0e37635024246d60136f7802543e4d36265c3e035a725c6322700d626b345d1d6464283a016f35714d434124281b607d315f66212d671428026a4f4f79657e34153f3467097e4e135f187a21767f02125b375563517a3742597b6c394e78742c4a725069606576777c314429264f6e330d7530453f22537f5e3034560d22146831456b1b72725f30676d0d5c71617d48753e26667e2f7a334c731c22630a242c7140457a42324629064441036c7e646208630e745531436b7c51743a36674c4f352a5575407b767a5c747176016c0676386e403a2b42356a727a04662b4446375f36265f3f124b724c6e346544706277641025063420016629225b43432428036f29341a2338627c47650b264c477c653a67043e6766152a485c7f33617264780656537e5468143f305f4537722352303c3d4379043d69797e6f3922527b24536e310d653d4c33696c635474637d0326516f745e610d773340306621105a7361654e3e392970687c2e335f3015677d4b3a724a4659767c2f5b7c16055a126820306c14315d6b59224a27311f747f336f4d5974321a22507b22705a226c6d446a37375761423a2b5c29247163046d7e47032244377508300751727126326f117f7a38670c2b23203d4f27046a5c5e1532601126292f577776606f0c6d0126474b2a73737a41316362146e581d7c1228717664091c'
# salt="WeAreDe1taTeam"
#
# i = 0
# text = ''
# si = cycle(salt)
# while i < 1199:
#   text += chr(int(("0x"+cipher[i:i+2]),16) ^ ord(next(si)))
#   i += 2
# print(text)
#
# normalized_distances = []
#
# for keysize in range(2,40):
#     c1 = text[:keysize]
#     c2 = text[keysize:keysize*2]
#     c3 = text[keysize*2:keysize*3]
#     c4 = text[keysize*3:keysize*4]
#     c5 = text[keysize*4:keysize*5]
#     c6 = text[keysize*5:keysize*6]
#
#     normalized_distance = float(
#         haming(c1,c2)+
#         haming(c2,c3)+
#         haming(c3,c4)+
#         haming(c4,c5)+
#         haming(c5,c6)
#         )/(keysize*5)
#     normalized_distances.append((keysize,normalized_distance))
#
# normalized_distances = sorted(normalized_distances,key=lambda x:x[1])
# print(normalized_distances)
#
# for keysize,_ in normalized_distances[:5]:
#     block_bytes = [[] for _ in range(keysize)] # 列表的列表
#     for i,byte in enumerate(text):
#         block_bytes[i%keysize].append(byte)
#     keys = ''
#     for bbytes in block_bytes:
#         keys += break_single_key_xor(bbytes)
#     key = cycle(keys)
#     plaintext = ''.join(chr(ord(next(key))^ord(p)) for p in text)
#     print("keysize:",keysize)
#     print("key is:",keys)
#     print(plaintext)


# Lfsr

# from Crypto.Util.strxor import strxor
# import codecs
# cip = open('cipher.txt', 'rb').read()
# msg = open('Plain.txt', 'rb').read()
#
# print(codecs.encode(strxor(cip, msg)[:8], 'hex'))
#
# key = '0123456789abcdef'

#
#
from Crypto.Util.number import long_to_bytes



def lfsr(R, mask):
    # 左移1位：保留末尾 63 位，在最后添加一个0
    output = (R << 1) & 0xffffffffffffffff

    # i：保留 R 的前 0、1、3、4位
    i = (R & mask) & 0xffffffffffffffff

    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i >> 1
    # lastbit：统计 i 里面有多少个1, 奇数个则为1, 偶数个则为0

    # output: R 左移1位，再添加 lastbit
    output ^= lastbit
    return (output, lastbit)
#
#
# cip = open('flag_encode.txt', 'rb').read()
# a = ''.join([chr(int(b, 16)) for b in [key[i:i + 2] for i in range(0, len(key), 2)]])
#
# ans = ""
#
# for i in range(len(a)):
#     ans += (chr((cip[i] ^ ord(a[i]))))
#
# lent = len(cip)
#
# for i in range(len(a), lent):
#     tmp = 0
#     for j in range(8):
#         (R, out) = lfsr(R, mask)
#         tmp = (tmp << 1) ^ out
#     ans += (chr(tmp ^ cip[i]))
#
# print(ans)

# MT19937 randcrack
from hashlib import md5
from randcrack import RandCrack
def foo(l,i):
    a=[]
    a.append(l[i])
    b1=l[i+1]>>32
    b2=l[i+1]&(2**32-1)
    a.append(b2)
    a.append(b1)
    b1=l[i+2]>>64
    b2=(l[i+2]&(2**64-1))>>32
    b3=l[i+2]&(2**32-1)
    a.append(b3)
    a.append(b2)
    a.append(b1)
    return a

def mt19937(filename):
    with open(filename,'r') as f:
        l=f.readlines()
    l=[int(i.strip()) for i in l]
    ll=[]
    for i in range(0,len(l),3):
        ll+=foo(l,i)
    rc=RandCrack()
    for i in ll:
        rc.submit(i)
    aa=rc.predict_getrandbits(32)
    print(md5(str(aa).encode()).hexdigest())

# 魔改梅森旋转mt97731
# 逆向next部分（提取伪随机数部分），
# right shift inverse
def inverse_right(res, shift, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp >> shift
    return tmp


# right shift with mask inverse
def inverse_right_mask(res, shift, mask, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp >> shift & mask
    return tmp

# left shift inverse
def inverse_left(res, shift, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp << shift
    return tmp


# left shift with mask inverse
def inverse_left_mask(res, shift, mask, bits=32):
    tmp = res
    for i in range(bits // shift):
        tmp = res ^ tmp << shift & mask
    return tmp

# sage, 逆向提取伪随机数部分（X(state，1*32) * T（32*32） = Z(输出的随机数 1*32) 
# from sage.all import *
# from random import Random

# def buildT():
#     rng = Random()
#     T = matrix(GF(2),32,32)
#     for i in range(32):
#         s = [0]*624
#         # 构造特殊的state
#         s[0] = 1<<(31-i)
#         rng.setstate((3,tuple(s+[0]),None))
#         tmp = rng.getrandbits(32)
#         # 获取T矩阵的每一行
#         row = vector(GF(2),[int(x) for x in bin(tmp)[2:].zfill(32)])
#         T[i] = row
#     return T

# def reverse(T,leak):
#     Z = vector(GF(2),[int(x) for x in bin(leak)[2:].zfill(32)])
#     X = T.solve_left(Z)
#     state = int(''.join([str(i) for i in X]),2)
#     return state

# def test():
#     rng = Random()
#     # 泄露信息
#     leak = [rng.getrandbits(32) for i in range(32)]
#     originState = [i for i in rng.getstate()[1][:32]]
#     # 构造矩阵T
#     T = buildT()
#     recoverState = [reverse(T,i) for i in leak]
#     print(recoverState==originState)



# mask=0b10100100000010000000100010010100 #0,2,5,12,20,24,27,29

# lfsr 求逆

def solve(c):
    li = []
    for i in range(32):
        temp = '1' + ''.join(li) + c[:31 - len(li)]
        if int(temp[0]) ^ int(temp[2]) ^ int(temp[5]) ^ int(temp[12]) ^ int(temp[20]) ^ int(temp[24]) ^ int(
                temp[27]) ^ int(temp[29]) == int(c[31 - len(li)]):

            li.insert(0, '1')
        else:

            li.insert(0, '0')
    return li




# flag{926201d7} 在buuctf提交时要添加0x,为此白给了好多次.
def re_lfsr(mask,output):
    N = 32
    with open(output, 'rb') as f:
        b = f.read()
    key = ''
    for i in range(N // 8):
        t = ord(long_to_bytes(b[i]))
        for j in range(7, -1, -1):
            key += str(t >> j & 1)
    idx = 0
    ans = ""
    key = key[31] + key[:32]
    while idx < 32:
        tmp = 0
        for i in range(32):
            if mask >> i & 1:
                tmp ^= int(key[31 - i])
        ans = str(tmp) + ans
        idx += 1
        key = key[31] + str(tmp) + key[1:31]
    num = int(ans, 2)
    print(hex(num))

# sage
# output -> mask / seed  B-M算法
# in : output输出序列 ； length掩码长度
# return : mask
# def BM(output,length):
#     with open(output,'r') as f:
#         out = f.read()
#         s = [int(x) for x in out]
#         print(len(s))
#     list2 = []
#     for i in range(length):
#         list2.append(int(j) for j in list(reversed(out[i:i+length])))
#
#     M = matrix(GF(2),list2)
#     T = vector(GF(2),length)
#
#
#     for i in range(length):
#         T[i] = s[i + length ]
#
#     try:
#         mask =  M.inverse() * T
#         print((int(''.join(map(str, (mask))), base=2)))
#         return mask
#     except:
#         return

# key为输出序列前n（mask.bitlength)位,已知输出序列和mask，逆推求seed
def get_key(mask,key):
    R = ""
    index = 0
    key = key[255] + key[:256]
    while index < 256:
        tmp = 0
        for i in range(256):
            if mask >> i & 1:
                # tmp ^= int(key[255 - i])
                tmp = (tmp+int(key[255-i]))%2
        R = str(tmp) + R
        index += 1
        key = key[255] + str(tmp) + key[1:255]
    return int(R,2)
def get_int(x):
    m=''
    for i in range(256):
        m += str(x[i])
    return (int(m,2))

# 输出序列output不够2n长度，爆破后面几位
# import hashlib
# import itertools
#
# # 输出序列r
# r = '001010010111101000001101101111010000001111011001101111011000100001100011111000010001100101110110011000001100111010111110000000111011000110111110001110111000010100110010011111100011010111101101101001110000010111011110010110010011101101010010100101011111011001111010000000001011000011000100000101111010001100000011010011010111001010010101101000110011001110111010000011010101111011110100011110011010000001100100101000010110100100100011001000101010001100000010000100111001110110101000000101011100000001100010'
# def pad(sz):
#     rr = [int(i) for i in r] + sz
#     M = matrix(GF(2),256,256)
#     X = vector(GF(2),256)
#     for i in range(256):
#         M[i] = rr[i:i+256]
#         X[i] = rr[i+256]
#     try:
#         m = M.inverse()*X
#         seed = get_key(get_int(m),r[:256])
#         seed = hex(seed)[2:]
#         sha = hashlib.sha256(seed.encode()).hexdigest()
#         if sha[:4] == '1224':
#             print('de1ctf{' + sha + '}')
#             return
#     except:
#         return
#
# for i in itertools.product([0,1],repeat = 8):
#     pad(list(i))



if __name__ == "__main__":
    #mt19937("random.txt")
    # mask = 0b10100100000010000000100010010100
    # re_lfsr(mask,"key")
    BM('output.txt',100)