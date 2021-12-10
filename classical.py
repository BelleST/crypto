#古典密码
#简单移位密码
import base64
import binascii
import codecs
'''
m,k
以k的长度l切分m
明文字符位置1234
密文字符位置3124（如把第一个字符放到第三个去）
'''
#
# def shift_encrypt(m,k):
#     l = len(k)
#     c = ""
#     for i in range(0,len(m),l):
#         tmp_c = [""]*l
#         if i + 1 > len(m):
#             tmp_m = m[i:]
#         else:
#             tmp_m = m[i:i+l]
#         for kidx in range(len(tmp_m)):
#             tmp_c[int(k[kidx]) - 1] = tmp_m[kidx]
#         c += "".join(tmp_c)
#     return c
#
# def shift_decrypt(c,k):
#     l = len(k)
#     m = ""
#     for i in range(0,len(c),l):
#         tmp_m = [""] * l
#         if i + l >= len(c):
#             tmp_c = c[i:]
#             use = []
#             for kidx in range(len(tmp_c)):
#                 use.append(int(k[kidx]) - 1)
#             use.sort()
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[use.index(int(k[kidx])-1)]
#
#         else:
#             tmp_c = c[i:i+l]
#             for kidx in range(len(tmp_c)):
#                 tmp_m[kidx] = tmp_c[int(k[kidx]) - 1]
#
#         m += "".join(tmp_m)
#
#     return m
#
# #云影密码
#
# def c01248_decode(c):
#     l=c.split("0")
#     origin = "abcdefghijklmnopqrstuvwxyz"
#     r = ""
#     for i in l:
#         tmp = 0
#         for num in i:
#             tmp += int(num)
#             r += origin[tmp-1]
#     return r

#xor
# a = 'lovelovelovelovelovelovelovelove'
# b = [0x0A,0x03,0x17,0x02,0x56,0x01,0x15,0x11,0x0A,0x14,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x0E,0x0A,0x1E,0x30,0x14,0x0C,0x19,0x0D,0x1F,0x10,0x0E,0x06,0x03,0x00]
#
# c = ''
# for i in range(len(a)):
#     c += chr(ord(a[i])^b[i])
# print(c)

#"凯撒密码解密")
#密文
# str = 'R5UALCUVJDCGD63RQISZTBOSO54JVBORP5SAT2OEQCWY6CGEO53Z67L'
# #密钥(平移位数)
# m = ''
# for my in range(1,26):
#     print("密钥",my)
#     for i in str:
#       mw = ord(i)
#       if (64 < mw < 91):#大写字母
#         jm = mw + my
#         if jm > 90:
#               jm = (mw - 26) + my
#               m += chr(jm)
#           #m.join(chr(jm))
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       elif (96 < mw < 123):#小写字母
#         jm = mw + my
#         if jm > 122:
#             jm = (mw - 26) + my
#             m += chr(jm)
#           #print(chr(jm), end='')
#         else:
#             m += chr(jm)
#           #print(chr(jm), end='')
#       else:#数字和特殊字符不做修改
#         jm = mw + 0
#         m += chr(jm)
#         #print(chr(jm), end='')
#     print(m)
#     try:
#         print(base64.b32decode(m))
#     except binascii.Error:
#         missing_padding = 2 - len(m) % 2  #base64为4
#         if missing_padding:
#             m += '=' * missing_padding
#         print(base64.b32decode(m))
#     m = ''
#

#polybius
# import itertools
#
# key = []
# cipher = "ouauuuoooeeaaiaeauieuooeeiea"
#
# for i in itertools.permutations('aeiou', 5):
#     key.append(''.join(i))
#
# for now_key in key:
#     solve_c = ""
#     res = ""
#     for now_c in cipher:
#         solve_c += str(now_key.index(now_c))
#     for i in range(0,len(solve_c),2):
#         now_ascii = int(solve_c[i])*5+int(solve_c[i+1])+97
#         if now_ascii>ord('i'):
#             now_ascii+=1
#         res += chr(now_ascii)
#     if "flag" in res:
#         print(now_key, res)


#移位
# fib = ""
#
# f =   ""
#
# c = "喵汪哞叽双哇顶，眠鸟足屁流脑，八哇报信断流脑全叽，眠鸟进北脑上草，八枝遇孙叽，孙叽对熬编叶：值天衣服放鸟捉猴顶。鸟对：北汪罗汉伏熬乱天门。合编放行，卡编扯呼。人离烧草，报信归洞，孙叽找爷爷。"
#
# m = ['']*32
#
# fib = fib.split('')
# f = f.split('')
# print(fib)
#
# for i in range(len(f)):
#     m[fib.index(f[i])] = c[i]
# for i in m:
#     print(i,end='')


#四方密码
# import collections
# import re
#
# matrix = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
# pla = 'abcdefghijklmnoprstuvwxyz'
# key1 = '[SECURITY]'
# key2 = '[INFORMATION]'
# key1 = ''.join(collections.OrderedDict.fromkeys(key1))
# key2 = ''.join(collections.OrderedDict.fromkeys(key2))
#
# matrix1 = re.sub('[\[\]]', '', key1) + re.sub(key1, '', matrix)
# matrix2 = re.sub('[\[\]]', '', key2) + re.sub(key2, '', matrix)
#
# matrix_list1 = []
# matrix_list2 = []
# pla_list = []
# for i in range(0, len(matrix1), 5):
#     matrix_list1.append(list(matrix1[i:i + 5]))
# # print matrix_list1
#
# for i in range(0, len(matrix2), 5):
#     matrix_list2.append(list(matrix2[i:i + 5]))
# # print matrix_list2
#
# for i in range(0, len(pla), 5):
#     pla_list.append(list(pla[i:i + 5]))
#
#
# # print pla_list
#
# # 查询两个密文字母位置
# def find_index1(x):
#     for i in range(len(matrix_list1)):
#         for j in range(len(matrix_list1[i])):
#             if matrix_list1[i][j] == x:
#                 return i, j
#
#
# def find_index2(y):
#     for k in range(len(matrix_list2)):
#         for l in range(len(matrix_list2[k])):
#             if matrix_list2[k][l] == y:
#                 return k, l
#
#
# def gen_pla(letter):
#
#
# # 两个子母中第一个字母位置
#     first = find_index1(letter[0])
#
# # 两个子母中第二个字母位置
#     second = find_index2(letter[1])
#
#     pla = ''
#     pla += pla_list[first[0]][second[1]]
#     pla += pla_list[second[0]][first[1]]
#
#     return pla
#
#
# def main():
#     cip = 'ZHNJINHOOPCFCUKTLJ'
#
#
#     pla = ''
#     for i in range(0, len(cip), 2):
#         pla += gen_pla(cip[i:i + 2])
#     print(pla)
#
# if __name__ == '__main__':
#     main()


#hill 希尔密码
# s='wznqcaduqopfkqnwofDbzgeu'
# #未给密钥的自己猜测
# flag_pre='utflag'
# def getit(a1,b1,c1,a2,b2,c2,a3,b3,c3):
#     for i in range(26):
#         for j in range(26):
#             if (a1 * i + b1 * j) % 26 == c1 and (a2 * i + b2 * j) % 26 == c2 and (a3 * i+b3*j) % 26 == c3:
#                 return (i,j)
# x1=getit(22,25,20,13,16,5,2,0,0)
# x2=getit(22,25,19,13,16,11,2,0,6)
# import string
# flag=''
# for i in range(0, len(s),2):
#     flag+=string.ascii_letters[(x1[0]*string.ascii_letters.index(s[i])+x1[1]*string.ascii_letters.index(s[i+1]))%26]
#     flag+=string.ascii_letters[(x2[0]*string.ascii_letters.index(s[i])+x2[1]*string.ascii_letters.index(s[i+1]))%26]
# print(flag)

#培根密码
# letters1 = [
#     'A', 'B', 'C', 'D', 'E', 'F', 'G',
#     'H', 'I', 'J', 'K', 'L', 'M', 'N',
#     'O', 'P', 'Q', 'R', 'S', 'T',
#     'U', 'V', 'W', 'X', 'Y', 'Z',
# ]
# letters2 = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g',
#     'h', 'i', 'j', 'k', 'l', 'm', 'n',
#     'o', 'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y', 'z',
# ]
# cipher1 = [
#     "aaaaa", "aaaab", "aaaba", "aaabb", "aabaa", "aabab", "aabba",
#     "aabbb", "abaaa", "abaab", "ababa", "ababb", "abbaa", "abbab",
#     "abbba", "abbbb", "baaaa", "baaab", "baaba", "baabb",
#     "babaa", "babab", "babba", "babbb", "bbaaa", "bbaab",
# ]
# cipher2 = [
#     "AAAAA", "AAAAB", "AAABA", "AAABB", "AABAA", "AABAB", "AABBA",
#     "AABBB", "ABAAA", "ABAAA", "ABAAB", "ABABA", "ABABB", "ABBAA",
#     "ABBAB", "ABBBA", "ABBBB", "BAAAA", "BAAAB", "BAABA",
#     "BAABB", "BAABB", "BABAA", "BABAB", "BABBA", "BABBB",
# ]
#
#
# def bacon1(string):
#     lists = []
#     # 分割，五个一组
#     for i in range(0, len(string), 5):
#         lists.append(string[i:i+5])
#     # print(lists)
#     # 循环匹配，得到下标，对应下标即可
#     for i in range(0, len(lists)):
#         for j in range(0, 26):
#             if lists[i] == cipher1[j]:
#                 # print(j)
#                 print(letters1[j], end="")
#     print("")
#
#
# def bacon2(string):
#     lists = []
#     # 分割，五个一组
#     for i in range(0, len(string), 5):
#         lists.append(string[i:i+5])
#     # print(lists)
#     # 循环匹配，得到下标，对应下标即可
#     for i in range(0, len(lists)):
#         for j in range(0, 26):
#             if lists[i] == cipher2[j]:
#                 # print(j)
#                 print(letters2[j], end="")
#     print("")
#
#
# bacon2("AABABABABAAAAAAAABBAABAAABAABAAABABABAAAABAABAABABABAABABAABB")


#猪圈变式，左右字母表相对应替换
# if __name__ == '__main__':
#     dic = {'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 's': 'w', 'v': 'z',
#            't': 'x', 'u': 'y', 'j': 'a', 'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g', 'q': 'h', 'r': 'i',
#            'w': 's', 'z': 'v', 'x': 't', 'y': 'u'}
#     crypto = 'ocjp{zkirjwmo-ollj-nmlw-joxi-tmolnrnotvms}'
#     plaintext = ''
#     for c in crypto:
#         if c in dic:
#             plaintext += dic[c]
#         else:
#             plaintext += c
#     print(plaintext)

#词频分析
#爆破密钥长度
    #找子串（长度3-4），爆破，（应该还有别的找最大字串算法）
cipher = ""
sub_str = []
for i in range(26):
    sub_str[0] = chr(ord('a')+i)
    for j in range(26):
        sub_str[1] = chr(ord('a')+j)
        for k in range(26):
            sub_str[2] = chr(ord('a') + k)
            for l in range(26):
                sub_str[3] = chr(ord('a')+l)
                if cipher.count("".join(sub_str)) > 20:
                    key = sub_str
                    print(key)
                    break
    #找第i次出现的位置（下标j）
def get_position(s,sub_s,i):
    
