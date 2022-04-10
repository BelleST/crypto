n = 0x6cb77aaf0bdc8c89cb7874cfad460897a41199df8dcfc6b991715f59a8c264d699a5d40c16ccc7625fd95c7a53e47dc70294128196badb5fa520e557d2eef972dc948924bf5af879407e445b06cf12a3504392391fb59d9c71a89aa6afab8a7afe31a4ff4e6f6c190628599eb1019f16264aa77d8f44fcb780c60715eb7beec7
e = 0x10001
c = 0x1c88587ac5c541d47368fc03e054d30ef8d963896113daaa8c4ca8e0a95c5cbca72867301b86618ea86a758b011802bfe33597a4eaac6c7050cedbc671a49a44f584df8c1304616b5fa1a6af0e9c517caf94679eaba46015b486e329b59ab229960b728293fa5fb71157afe9762c29c88bdb06a1742ed1083a511d68996cf4ec
sub = 0x535408bdf9e1c11d5b41867ede3d953bd33bccdc4adccf830a2ac8d0b66c12cfbc7bdee300559807d3c2f063d1c0af0970603c3afa4dd3ee8012fdcd8be02a56
import math
import Rsa
for i in range(5,int(math.sqrt(n))):
    if i*(i+sub) == n:
        print("find!",i)
        d = Rsa.get_d(e,i+sub,i)
        m = Rsa.decrypt(e,c,d,n)