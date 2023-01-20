import binascii

import gmpy2

gmpy2.get_context().precision = 8196

from binascii import unhexlify
from functools import reduce
from gmpy2 import root
from functions import *

# Håstad's Broadcast Attack
# https://id0-rsa.pub/problem/11/

# Resources
# https://en.wikipedia.org/wiki/Coppersmith%27s_Attack
# https://github.com/sigh/Python-Math/blob/master/ntheory.py

EXPONENT = 3

CIPHERTEXT_1_F = open('ciphertext.1b.txt', 'w')
CIPHERTEXT_2_F = open('ciphertext.2b.txt', 'w')
CIPHERTEXT_3_F = open('ciphertext.3b.txt', 'w')

CIPHERTEXT_1 = binascii.hexlify(open('messages/message_bob.rsa', 'rb').read()).decode()
CIPHERTEXT_2 = binascii.hexlify(open('messages/message_bertrand.rsa', 'rb').read()).decode()
CIPHERTEXT_3 = binascii.hexlify(open('messages/message_bernard.rsa', 'rb').read()).decode()

CIPHERTEXT_1_F.write(f'0x{CIPHERTEXT_1}')
CIPHERTEXT_2_F.write(f'0x{CIPHERTEXT_2}')
CIPHERTEXT_3_F.write(f'0x{CIPHERTEXT_3}')

CIPHERTEXT_1_F.close()
CIPHERTEXT_2_F.close()
CIPHERTEXT_3_F.close()

CIPHERTEXT_1 = "messages/ciphertext.1b.txt"
CIPHERTEXT_2 = "messages/ciphertext.2b.txt"
CIPHERTEXT_3 = "messages/ciphertext.3b.txt"

# print("CIPH : ", (binascii.hexlify(CIPHERTEXT_3).decode()))

# print("E5DCFDE5A9D0E1D5B59D2B19592414A9F2B7079E1B53F91DC4892902AEC79986E11F0FDB49DE5626FAC07156A031930331FAA2428AC22AFFBB8D8A96EED6E1208036CC4B16BCF1C9665A2505FF367CA757C8ED848C82BDEB98F8B4B0F9C80AE49911E104BE2324BA0FFC261E3622AC07D9636109D6ED099DAC12B7B2CABFF9040298E51E98593838F21B3AC94FB8E607CB956D054564DAA25D8CB92749A178AA8A48156F4D95F53A14D0B8557A7D1B289ACCAA3A743B6A69EDCE8A0AFA7F05C160515F274A0C88E8130EE92EEA5FC4BB75FA54DC771BA29234D71C0D0707A92EA583C3A356A22F6EF4D6DE6E086669543D09D8C0EF8B41EB02F46F898EEEF3ECCF2629AC8CA38A2FDBD8E566258DC8D3EBBD87F1FD75F1B334A0059043992F3007EEC1BF609CD90CCEEEF0B612812C3FF050C2EF84899296AB57303E21052826A8C596F7FBBA8F7CC15C62A1C6DCDD65D902CC55884CBE8DFFC0E062162272F29E467283C5E440C6B4533FC57382B6E969F9479B420A97F7E3264220B7E49836D71E7CFF9023009DBF844C8B9D0930C8347824DEA520832706B452283A169AE112FF5DB4513B59BE0F098457219C90B403E0D4D0978EC706CA23CE2A7096A5753C8F57DA280BFFABC12CD2A6B7BF5905719B18684DFD873D4B417B62A98E371381FC5BDDF92FF1C2AA4EE0AE57D7F079A3C297012F1ADB8F9601722DCD47119C1A26291167656065F1135B31C2C47BEFB0C099646C715FEA6B459564ED70828AA0495EE42FC2119863E21FC5CBB65854D9DF6CE725065EFBB79CE6D15390181F23143CA44C585075C7C94B3BE3797C191EE565C98A0C46688CB96DB0C34D80522E394B7EA4740DF45E29A497E5B61C3DD67997BD7687C75221EBE15C7C7FF705A7A58F9CBCD038546DD63011BA226FB8CD527C24B245363E73ECED22012E235F00ABAE4C5FF383177F7B73C42290E705CA93B5FD5A370572B25982B0B5ABCBBCE93013870385DFA7A31FB20495E02D5D09E68C79C4F095E6C500686EBE43ACA8CCBEC1C92FB493F785A5DC8DE8E0DB12CB1D0F66F3C0BCEBC6941F19C8E5B0E997FE6595367C425148F52903FCC5EAB982D2A7C2A998E2E474D8807F336E4D9934A8EB74A08FD0291AE07B68713DDF96A0D1386C3EB5DFF690F10812EB2BDC189D74F598377562FB1C84C9D5C7ECED0CB2C20976884755EB8D4FA5CFBF61EAB85DF0D09BEA3073D5801DFD77DABC111B38281601D96CE8B6DCDB036E2971F5559945CCCE8680E3175D61C3B8D3223F60E003FF5F5E9216BB65121D560C37B81EF3E1D5CB1C711160CFF7BCE974E0654EC384620E23EFCAA3FE1C69E4D8238B9F026B1200D82B5ABD915E2847691D759CEB6554326A2DF5434E9245F1B1ED8D5030D750EC2D22E374E3677D5B3D2D43CF48DE307091B5E7C1EAB977967CADF5CB".lower())

MODULUS_1 = "messages/modulus.1.txt"
MODULUS_2 = "messages/modulus.2.txt"
MODULUS_3 = "messages/modulus.3.txt"


if __name__ == '__main__':
    C1 = get_value(CIPHERTEXT_1)
    C2 = get_value(CIPHERTEXT_2)
    C3 = get_value(CIPHERTEXT_3)
    ciphertexts = [C1, C2, C3]

    N1 = get_value(MODULUS_1)
    N2 = get_value(MODULUS_2)
    N3 = get_value(MODULUS_3)
    modulus = [N1, N2, N3]

    C = chinese_remainder_theorem([(C1, N1), (C2, N2), (C3, N3)])
    M = int(root(C, 3))

    M = hex(M)[2:]
    print(unhexlify(M).decode('utf-8'))
