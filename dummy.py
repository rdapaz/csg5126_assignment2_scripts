
def split_chunks(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


data = """
0b057be67f220767dd1075594432e8b8
cfc5a8e8a803645232990aaf2ff49fd7
7e9be033a955f18f777a87d28f93be3e
096254b20f79b6728384a54dbba69ea1
3fb617f7a7cc758a998410ad4567c126
f03b7614dfadbbe4c2e8f88b69d12e04
da632a0e6a0b6ec1c5066078e74b7c7f
670a9ce162208598f3efc09945da8f39
4364f14ecdd1380e8d60c54b92492baa
121956815de6276ddb5f1978e7431149
6f36f7cde31efc87d3edeb2d80060591
b436d314e9918621f8341fa4105da41d
318175c7f653f2480944c3ed3f61bcca
4e0af85db16d3ba53a221363346a3d8e
""".splitlines()

data = [x for x in data if len(x) > 0]

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

for x, y in pairwise(data):
   print (x, y, sep="|")


