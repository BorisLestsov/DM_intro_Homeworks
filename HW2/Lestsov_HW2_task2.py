def MurMurHash(s, seed = 0):
    m = 0x5bd1e995
    r = 24
    h = int(seed) ^ r
    
    while len(s) >= 4:
        k = ord(s[0])
        k |= ord(s[1]) << 8
        k |= ord(s[2]) << 16
        k |= ord(s[3]) << 24

        k *= m
        k ^= k >> r
        k *= m

        h *= m
        h ^= k

        s = s[4:]
        
    if len(s) == 1:
        h ^= ord(s[0]);
        h *= m;
    elif len(s) == 2:
        h ^= ord(s[1]) << 8
    elif len(s) == 3:
        h ^= ord(s[2]) << 16

    h ^= h >> 13;
    h *= m;
    h ^= h >> 15;
    
    return h

def hashing_trick(features, bits):
    x = {}
    for k, v in features.iteritems():
        h = MurMurHash("".join([str(k), ':', str(v)]))
        x[h % 2**bits] = {k: v}
    return x

feat = {'Hello': 1, 'World':5}
feat1 = {'Hello': 2, 'aaa':8}
print feat
print hashing_trick(feat, 16)
print feat1
print hashing_trick(feat1, 16)