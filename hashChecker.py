import hashlib
import os
import re

rex = re.compile(r'2017-B\.7z\.\d{3}', re.IGNORECASE)

# Credit to Glen Thompson for posting these
target_hashes = {
    '2017-B.7z.001':  '2a0a9ea08883ee372e87dc5c1a7019fd',
    '2017-B.7z.002':  '3118c66475aca07f6de42993189194cc',
    '2017-B.7z.003':  'c3d97eff52e5a7f4a8c7c0dc4c916e5e',
    '2017-B.7z.004':  '2ee04ed432a78e12df3245b0f8876f67',
    '2017-B.7z.005':  '6598c65e608c99b827d9a557b24d463b',
    '2017-B.7z.006':  'b7543610b84ab940b3f21469c0efc91d',
    '2017-B.7z.007':  '3f6d272d0dad361c085dc2cc071bc48f',
    '2017-B.7z.008':  '53f4be13ba17b40437452a1b53c2cc9d',
    '2017-B.7z.009':  '40fd41ead379bd85ab57dbbb7ce76274',
    '2017-B.7z.010':  '2917ea8b8806d52c6582e2e82ca704ed',
    '2017-B.7z.011':  '143cb37a33752ed9f37163f436437885',
    '2017-B.7z.012':  'a2b5c232c0c936cb570a91705d6454ef',
    '2017-B.7z.013':  'bbfdf7c8e7318fdbb581b0ea4829892a',
    '2017-B.7z.014':  'd819caf4bb27dbff027d4e1bf27bb78e',
    '2017-B.7z.015':  '487382aba2415e87722b4def451e6178',
    '2017-B.7z.016':  '0fffd08be5a9b383797caec5ea933fea',
    '2017-B.7z.017':  '7eeb710c2607f17ac63bf47d333a1e8a',
    }

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Change with your own path name
actual_hashes = {}
for root, dirs, files in os.walk(r'D:\Uni Stuff'): #< Change this to suit
    print(root)
    for file in files:
        m = rex.search(file)
        if m:
            hash_value = md5(os.path.join(root, file))
            actual_hashes[hash_value] = file
            print(file, hash_value, sep="|")

unmatched = [actual_hashes[h] for h in actual_hashes.keys() 
                if not h in target_hashes.values()]
                
if len(unmatched) > 0:
    for idx, file in enumerate(unmatched):
        if idx == 0:
            print('The following files have issues:')
        print('[+] ' + file)
else:
    print('All good, your files have been successfully downloaded!')
