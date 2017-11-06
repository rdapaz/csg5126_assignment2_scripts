import os.path

data = """
HP_PCC_md_0130_cat53.jpg
e0194eca1c8135636ce0e014341548c3.jpg
czarny-kot-fakt.jpg
cutest-cat-picture-ever.jpg
cute-cat.jpg
chaton_232339_w620.jpg
cat-adult-landing-hero.jpg
cat-03.jpg
7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
3385141-cat-images.jpg
1817db9a2a947adc1d1e2ebbdf8dcafd.jpg
101438745-cat-conjunctivitis-causes.jpg
cat-black-superstitious-fcs-cat-myths-162286659.jpg
foryou.txt
stuff.txt
thestuff.zip
#3840.doc
#3295.doc
#3276.doc
Links.docx
#3250.docx
#3249.docx
#3247.docx
""".splitlines()

data = list(set([os.path.splitext(x)[1] for x in data if len(x) > 1 ]))

for item in data:
    print (item)
