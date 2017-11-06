import re
import os
from collections import Counter

data = """
  4 = NEWS STORIES
  49 = #3840.doc
  47 = #3295.doc
  11 = The Internet
  48 = register.html
  46 = #3276.doc
  45 = #3250.doc
  44 = #3276.docx
  12 = foryou.txt
  43 = Local Disk (C:)
  42 = stuff.txt
  20 = Links.docx
  14 = Local Disk (P:)
  19 = Siamese-Cat-Names.jpg
  41 = adopting-a-cat.jpg
  40 = 4426323.jpg
  21 = Pictures
  39 = cat2.jpg
  38 = f03b7614dfadbbe4c2e8f88b69d12e04.jpg
  37 = cute-kitten-catcute-little-cat-hd-for-desktop-of-cute-white-kitten.jpg
  36 = HP_PCC_md_0130_cat53.jpg
  35 = 1817db9a2a947adc1d1e2ebbdf8dcafd.jpg
  34 = czarny-kot-fakt.jpg
  33 = cat-black-superstitious-fcs-cat-myths-162286659.jpg
  32 = thestuff.zip
  31 = cat-03.jpg
  30 = cat-adult-landing-hero.jpg
  29 = chaton_232339_w620.jpg
  28 = 4-ways-cheer-up-depressed-cat.jpg
  27 = 101438745-cat-conjunctivitis-causes.jpg
  26 = 3385141-cat-images.jpg
  25 = 7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
  24 = e0194eca1c8135636ce0e014341548c3.jpg
  23 = cutest-cat-picture-ever.jpg
  22 = cute-cat.jpg
  0 = windowsupdate
  18 = Applications
  17 = Microsoft.Windows.Computer
  1 = System and Security
  16 = personalization-start
  15 = enjoy.txt
  13 = superman.pdf
  10 = network-ethernet
  9 = #3250.docx
  6 = 32GB-B (D:)
  5 = text.txt
  8 = #3249.docx
  7 = #3247.docx
  3 = ::{8E908FC9-BECC-40F[1]6-915B-F4CA0E70D03D}
  2 = ::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}
""".splitlines()
data = [x.split(' = ')[1] for x in data if len(x) > 0]

doc_types = []
for x in data:
    rex = re.compile(r'(.*)'
                     r'\.'
                     r'([a-z]{3,4})\Z', re.IGNORECASE | re.VERBOSE)
    m = rex.search(x)
    if m:
        file_ext = m.group(2)
        print(file_ext, x, sep='|')
        doc_types.append(file_ext)
c = Counter(doc_types)

print(c)