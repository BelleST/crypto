import base64
import binascii
import codecs
import libnum
import rsa
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
import sympy

n = 156808343598578774957375696815188980682166740609302831099696492068246337198792510898818496239166339015207305102101431634283168544492984586566799996471150252382144148257236707247267506165670877506370253127695314163987084076462560095456635833650720606337852199362362120808707925913897956527780930423574343287847
p = 12847964754765427496399764780328918622503990027015223921752369659611143245908239173177604049265523011184163182090867099853786582101440246414647619495980989
q = 12204917011499204793467396627331950459243603269732530719870032567474409945243640569351016419835483810515390876443640549604664275934407520354979414742015923
#d =139916095583110895133596833227506693679306709873174024876891023355860781981175916446323044732913066880786918629089023499311703408489151181886568535621008644997971982182426706592551291084007983387911006261442519635405457077292515085160744169867410973960652081452455371451222265819051559818441257438021073941183
e = 65537
c = 108542078809057774666748066235473292495343753790443966020636060807418393737258696352569345621488958094856305865603100885838672591764072157183336139243588435583104423268921439473113244493821692560960443688048994557463526099985303667243623711454841573922233051289561865599722004107134302070301237345400354257869




#dp，dq，c求m (RSA_CRT leaks)
# dp =6500795702216834621109042351193261530650043841056252930930949663358625016881832840728066026150264693076109354874099841380454881716097778307268116910582929
# dq =783472263673553449019532580386470672380574033551303889137911760438881683674556098098256795673512201963002175438762767516968043599582527539160811120550041
# def r_dpq(dp,dq):
#     invq = gmpy2.invert(q,p)
#     mp = pow(c,dp,p)
#     mq = pow(c,dq,q)
#     m = (((mp-mq)*invq) % p) * q + mq
#     m = hex(m)
#     print("m:"+ str(m))
#     print("n2s"+str(libnum.n2s(m)))
# r_dpq(dp,dq)

#n,dp,e求m dp泄露
dp = 734763139918837027274765680404546851353356952885439663987181004382601658386317353877499122276686150509151221546249750373865024485652349719427182780275825


for i in range(1,e):
    if (dp * e - 1) % i == 0:
        p = gmpy2.mpz(((dp * e - 1) // i) + 1)
        if n % p == 0:
            q= gmpy2.mpz(n / p)
            print(p)
            print(q)
            phi = gmpy2.mpz((p-1)*(q-1))
            d = gmpy2.invert(gmpy2.mpz(e),phi) % phi

print(d)
#d = gmpy2.mpz(d)
print("DP,d:"+str(d))
M = pow(c,d,n)
print("十进制M："+ str(M))
print(hex(M))
print(codecs.decode(hex(M)[2:],'hex'))
print(long_to_bytes(M))

# 共模攻击
# e1 = 773
# e2 = 839
# c1 = 3453520592723443935451151545245025864232388871721682326408915024349804062041976702364728660682912396903968193981131553111537349
# c2 = 5672818026816293344070119332536629619457163570036305296869053532293105379690793386019065754465292867769521736414170803238309535
# n = 6266565720726907265997241358331585417095726146341989755538017122981360742813498401533594757088796536341941659691259323065631249
# gcd,s,t = gmpy2.gcdext(e1,e2)
# if s < 0:
#     s = -s
#     c1 = gmpy2.invert(c1,n)
# if t < 0:
#     t = -t
#     c2 = gmpy2.invert(c2,n)
#
# M = gmpy2.powmod(c1,s,n)*gmpy2.powmod(c2,t,n) % n
# m = hex(M)
# print(m)
# print(codecs.decode(m[2:],'hex'))
# m = m[2:]
# missing_padding = 4 - len(m) % 4
# if missing_padding:
#     m += '=' * missing_padding
# print(base64.b64decode(m))


#多文件共模攻击
e1 = 2333
e2 = 23333
n = 14853081277902411240991719582265437298941606850989432655928075747449227799832389574251190347654658701773951599098366248661597113015221566041305501996451638624389417055956926238595947885740084994809382932733556986107653499144588614105694518150594105711438983069306254763078820574239989253573144558449346681620784979079971559976102366527270867527423001083169127402157598183442923364480383742653117285643026319914244072975557200353546060352744263637867557162046429886176035616570590229646013789737629785488326501654202429466891022723268768841320111152381619260637023031430545168618446134188815113100443559425057634959299
with open('myflag1','rb') as f:
    c1 = base64.b64decode(f.read())
    print(c1)
with open('myflag2','rb') as f:
    c2 = base64.b64decode(f.read())
    print(c2)
gcd,s,t = gmpy2.gcdext(e1,e2)
c1 = libnum.s2n(c1)
c2 = libnum.s2n(c2)
if s < 0:
    s = -s
    c1 = gmpy2.invert(c1,n)
if t < 0:
    t = -t
    c2 = gmpy2.invert(c2,n)

M = gmpy2.powmod(c1,s,n)*gmpy2.powmod(c2,t,n) % n
m = hex(M)
print(m)
print(codecs.decode(m[2:],'hex'))
m = m[2:]
missing_padding = 4 - len(m) % 4
if missing_padding:
    m += '=' * missing_padding
print(base64.b64decode(m))


# 分行加密，解密
# m = ""
# with open("data.txt",'r') as f:
#     for c in f.readlines():
#         m += chr(pow(int(c), d, n))
# print(m)


# 小公钥指数攻击（一般e为3） 对K进行爆破，只要k满足 kn + C能够开e次方就可以得明文
# k = 0
# while 1:
#     res = gmpy2.iroot(c + k * n, e)
#     if res[1] == True:
#        print(libnum.n2s(int(res[0])))
#        break
#     k = k + 1


#爆破，给出e的范围
# for e in range(50000,70001):
#     if gmpy2.gcd(e,phi) == 1:
#             d = gmpy2.invert(e, phi)
#             m = pow(c, d, n)
#             flag = hex(m)[2:]
#             #不是偶数就要加0？？？但是libnum不可用？？？
#             if (len(str(flag)) % 2 == 1):
#                 flag = '0' + flag
#             print(codecs.decode(flag,'hex'))

#低解密指数广播攻击，多个n,c找n的公因数

# n1= 331310324212000030020214312244232222400142410423413104441140203003243002104333214202031202212403400220031202142322434104143104244241214204444443323000244130122022422310201104411044030113302323014101331214303223312402430402404413033243132101010422240133122211400434023222214231402403403200012221023341333340042343122302113410210110221233241303024431330001303404020104442443120130000334110042432010203401440404010003442001223042211442001413004
# c1= 310020004234033304244200421414413320341301002123030311202340222410301423440312412440240244110200112141140201224032402232131204213012303204422003300004011434102141321223311243242010014140422411342304322201241112402132203101131221223004022003120002110230023341143201404311340311134230140231412201333333142402423134333211302102413111111424430032440123340034044314223400401224111323000242234420441240411021023100222003123214343030122032301042243
#
# n2= 302240000040421410144422133334143140011011044322223144412002220243001141141114123223331331304421113021231204322233120121444434210041232214144413244434424302311222143224402302432102242132244032010020113224011121043232143221203424243134044314022212024343100042342002432331144300214212414033414120004344211330224020301223033334324244031204240122301242232011303211220044222411134403012132420311110302442344021122101224411230002203344140143044114
# c2= 112200203404013430330214124004404423210041321043000303233141423344144222343401042200334033203124030011440014210112103234440312134032123400444344144233020130110134042102220302002413321102022414130443041144240310121020100310104334204234412411424420321211112232031121330310333414423433343322024400121200333330432223421433344122023012440013041401423202210124024431040013414313121123433424113113414422043330422002314144111134142044333404112240344
#
# n3= 332200324410041111434222123043121331442103233332422341041340412034230003314420311333101344231212130200312041044324431141033004333110021013020140020011222012300020041342040004002220210223122111314112124333211132230332124022423141214031303144444134403024420111423244424030030003340213032121303213343020401304243330001314023030121034113334404440421242240113103203013341231330004332040302440011324004130324034323430143102401440130242321424020323
# c3= 10013444120141130322433204124002242224332334011124210012440241402342100410331131441303242011002101323040403311120421304422222200324402244243322422444414043342130111111330022213203030324422101133032212042042243101434342203204121042113212104212423330331134311311114143200011240002111312122234340003403312040401043021433112031334324322123304112340014030132021432101130211241134422413442312013042141212003102211300321404043012124332013240431242
# n=[]
# c=[]
# for i in range(1,4):
#     n.append(eval('n'+str(i)))
#     c.append(eval('c'+str(i)))
# for i in range(len(n)):
#     n[i]=int(str(n[i]),5)
#     c[i]=int(str(c[i]),5)
# #print(n)
# def CRT(data):
#     plian=0
#     m=1
#     for x in data:
#         m=m*x[1]
#     for z,n in data:
#         mi=m//n
#         mr=gmpy2.invert(mi,n)
#         plian=plian+z*(mr*mi)
#     return plian%m
#
# data=list(zip(c,n))
# f=CRT(data)
# for e in range(2,97):
#     m2,h=gmpy2.iroot(f,e)
#     if(h==1):
#         m2 = hex(m2)
#         print(m2)
#         print(codecs.decode(m2[2:],'hex'))

#模不互素，n1,n2不互素,有e
# n1 = 13508774104460209743306714034546704137247627344981133461801953479736017021401725818808462898375994767375627749494839671944543822403059978073813122441407612530658168942987820256786583006947001711749230193542370570950705530167921702835627122401475251039000775017381633900222474727396823708695063136246115652622259769634591309421761269548260984426148824641285010730983215377509255011298737827621611158032976420011662547854515610597955628898073569684158225678333474543920326532893446849808112837476684390030976472053905069855522297850688026960701186543428139843783907624317274796926248829543413464754127208843070331063037
# n2 =12806210903061368369054309575159360374022344774547459345216907128193957592938071815865954073287532545947370671838372144806539753829484356064919357285623305209600680570975224639214396805124350862772159272362778768036844634760917612708721787320159318432456050806227784435091161119982613987303255995543165395426658059462110056431392517548717447898084915167661172362984251201688639469652283452307712821398857016487590794996544468826705600332208535201443322267298747117528882985955375246424812616478327182399461709978893464093245135530135430007842223389360212803439850867615121148050034887767584693608776323252233254261047
# c1 = 12641635617803746150332232646354596292707861480200207537199141183624438303757120570096741248020236666965755798009656547738616399025300123043766255518596149348930444599820675230046423373053051631932557230849083426859490183732303751744004874183062594856870318614289991675980063548316499486908923209627563871554875612702079100567018698992935818206109087568166097392314105717555482926141030505639571708876213167112187962584484065321545727594135175369233925922507794999607323536976824183162923385005669930403448853465141405846835919842908469787547341752365471892495204307644586161393228776042015534147913888338316244169120
#
#
# p1 = gmpy2.gcd(n1,n2)
# q1 = n1/p1





#多个n、c求
import libnum
# n4 = 22822039733049388110936778173014765663663303811791283234361230649775805923902173438553927805407463106104699773994158375704033093471761387799852168337898526980521753614307899669015931387819927421875316304591521901592823814417756447695701045846773508629371397013053684553042185725059996791532391626429712416994990889693732805181947970071429309599614973772736556299404246424791660679253884940021728846906344198854779191951739719342908761330661910477119933428550774242910420952496929605686154799487839923424336353747442153571678064520763149793294360787821751703543288696726923909670396821551053048035619499706391118145067
# c4 = 15406498580761780108625891878008526815145372096234083936681442225155097299264808624358826686906535594853622687379268969468433072388149786607395396424104318820879443743112358706546753935215756078345959375299650718555759698887852318017597503074317356745122514481807843745626429797861463012940172797612589031686718185390345389295851075279278516147076602270178540690147808314172798987497259330037810328523464851895621851859027823681655934104713689539848047163088666896473665500158179046196538210778897730209572708430067658411755959866033531700460551556380993982706171848970460224304996455600503982223448904878212849412357
#
# p = gmpy2.mpz(132585806383798600305426957307612567604223562626764190211333136246643723811046149337852966828729052476725552361132437370521548707664977123165279305052971868012755509160408641100548744046621516877981864180076497524093201404558036301820216274968638825245150755772559259575544101918590311068466601618472464832499)
#
# q = n4//p        #“//”  整除
#
# phi = (p-1)*(q-1)
#
# e = 65537
# d = gmpy2.invert(e,phi)
#
# m = pow(c4,d,n4)
#
# #print(libnum.n2s(m))    # "n2s" (数值转字符串)
# print(hex(m))
# print(bytes.fromhex(hex(m)[2:]))


#低解密指数广播攻击，三个n、c，同一个e加密且e较小,且n均互素

# n1= 331310324212000030020214312244232222400142410423413104441140203003243002104333214202031202212403400220031202142322434104143104244241214204444443323000244130122022422310201104411044030113302323014101331214303223312402430402404413033243132101010422240133122211400434023222214231402403403200012221023341333340042343122302113410210110221233241303024431330001303404020104442443120130000334110042432010203401440404010003442001223042211442001413004
# c1= 310020004234033304244200421414413320341301002123030311202340222410301423440312412440240244110200112141140201224032402232131204213012303204422003300004011434102141321223311243242010014140422411342304322201241112402132203101131221223004022003120002110230023341143201404311340311134230140231412201333333142402423134333211302102413111111424430032440123340034044314223400401224111323000242234420441240411021023100222003123214343030122032301042243
#
# n2= 302240000040421410144422133334143140011011044322223144412002220243001141141114123223331331304421113021231204322233120121444434210041232214144413244434424302311222143224402302432102242132244032010020113224011121043232143221203424243134044314022212024343100042342002432331144300214212414033414120004344211330224020301223033334324244031204240122301242232011303211220044222411134403012132420311110302442344021122101224411230002203344140143044114
# c2= 112200203404013430330214124004404423210041321043000303233141423344144222343401042200334033203124030011440014210112103234440312134032123400444344144233020130110134042102220302002413321102022414130443041144240310121020100310104334204234412411424420321211112232031121330310333414423433343322024400121200333330432223421433344122023012440013041401423202210124024431040013414313121123433424113113414422043330422002314144111134142044333404112240344
#
# n3= 332200324410041111434222123043121331442103233332422341041340412034230003314420311333101344231212130200312041044324431141033004333110021013020140020011222012300020041342040004002220210223122111314112124333211132230332124022423141214031303144444134403024420111423244424030030003340213032121303213343020401304243330001314023030121034113334404440421242240113103203013341231330004332040302440011324004130324034323430143102401440130242321424020323
# c3= 10013444120141130322433204124002242224332334011124210012440241402342100410331131441303242011002101323040403311120421304422222200324402244243322422444414043342130111111330022213203030324422101133032212042042243101434342203204121042113212104212423330331134311311114143200011240002111312122234340003403312040401043021433112031334324322123304112340014030132021432101130211241134422413442312013042141212003102211300321404043012124332013240431242
# n=[]
# c=[]
# for i in range(1,4):
#     n.append(eval('n'+str(i)))
#     c.append(eval('c'+str(i)))
# for i in range(len(n)):
#     n[i]=int(str(n[i]),5)
#     c[i]=int(str(c[i]),5)
# #print(n)
# def CRT(data):
#     plian=0
#     m=1
#     for x in data:
#         m=m*x[1]
#     for z,n in data:
#         mi=m/n
#         mr=gmpy2.invert(mi,n)
#         plian=plian+z*(mr*mi)
#     return plian%m
# data=list(zip(c,n))
# f=CRT(data)
# for e in range(2,97):
#     m2,h=gmpy2.iroot(f,e)
#     if(h==1):
#         print (m2)
#         print (hex(m2)[2:].decode('hex'))

#d泄露，遍历
#p,q是1024位的,因此两者相乘不低于2048位,通过运算可知ed-1为2064位,因此k一定小于16位
# e_d_1=e*d-1
# p=0
# q=0
# for k in range(pow(2,15),pow(2,16)):
#     if e_d_1%k==0:
#         p=sympy.prevprime(gmpy2.iroot(e_d_1//k,2)[0])
#         q=sympy.nextprime(p)
#         if (p-1)*(q-1)*k==e_d_1:
#             break
# n=p*q

#rsa的变形、n=p*q*r   威尔逊定理
# def get_pq(A,B):
#     tmp = 1
#     for i in range(B+1,A-1):
#         tmp *= i
#         tmp %= A
#     tmp_inv = gmpy2.invert(tmp,A)
#     return sympy.nextprime(tmp_inv)
#
# A1=21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467234407
# B1=21856963452461630437348278434191434000066076750419027493852463513469865262064340836613831066602300959772632397773487317560339056658299954464169264467140596
#
# A2=16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858418927
# B2=16466113115839228119767887899308820025749260933863446888224167169857612178664139545726340867406790754560227516013796269941438076818194617030304851858351026
#
# p = get_pq(A1,B1)
# q = get_pq(A2,B2)
# print(p)
# print(q)
# r = n//p//q
# phi = (p-1)*(q-1)*(r-1)
# d = gmpy2.invert(e, phi)
# print("d:"+ str(d))


#计算d
# phi_n = (p - 1) * (q - 1)
# d = gmpy2.invert(e, phi_n)
# print("d:"+ str(d))

# #根据c求m
# M = pow(c,d,n)
# print("十进制M："+ str(M))
# print(long_to_bytes(M))
# H = hex(M)
# print("十六："+H)
# flag = codecs.decode(H[2:], "hex")
# print(flag)

#从公钥文件中获取n、e的值
with open("pubkey2.pem",'rb') as f:
    pub = RSA.importKey(f.read())
    n = pub.n
    e = pub.e
    print(n,'\n',e)


#解密文件

key_info = RSA.construct((n, e, int(d), p, q))
key = RSA.importKey(key_info.exportKey())
key = PKCS1_OAEP.new(key)
f = open('myflag1', 'r').read()
c = base64.b64decode(f)
flag = key.decrypt(c)
print(flag)




