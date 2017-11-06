import os

data = """
/img_2017-B.dd/Users/computer/Pictures/101438745-cat-conjunctivitis-causes.jpg
/img_2017-B.dd/Users/computer/Pictures/1817db9a2a947adc1d1e2ebbdf8dcafd.jpg
/img_2017-B.dd/Users/computer/Pictures/3385141-cat-images.jpg
/img_2017-B.dd/Users/computer/Pictures/7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
/img_2017-B.dd/Users/computer/Pictures/cat-03.jpg
/img_2017-B.dd/Users/computer/Pictures/cat-adult-landing-hero.jpg
/img_2017-B.dd/Users/computer/Pictures/cat-black-superstitious-fcs-cat-myths-162286659.jpg
/img_2017-B.dd/Users/computer/Pictures/cat2.jpg
/img_2017-B.dd/Users/computer/Pictures/chaton_232339_w620.jpg
/img_2017-B.dd/Users/computer/Pictures/cute-cat.jpg
/img_2017-B.dd/Users/computer/Pictures/cute-kitten-catcute-little-cat-hd-for-desktop-of-cute-white-kitten.jpg
/img_2017-B.dd/Users/computer/Pictures/cute-kittens-30-57b30ad41bc90__605.jpg
/img_2017-B.dd/Users/computer/Pictures/cute-kittens-30-57b30ad41bc90__605.jpg
/img_2017-B.dd/Users/computer/Pictures/cutest-cat-picture-ever.jpg
/img_2017-B.dd/$Recycle.Bin/S-1-5-21-164977783-601896633-895069657-1001/$RXT96AU.jpg
/img_2017-B.dd/Users/computer/Desktop/encrypted
/img_2017-B.dd/Users/computer/Desktop/foryou.txt
/img_2017-B.dd/Users/computer/Documents/thestuff.zip
/img_2017-B.dd/Users/computer/Downloads/TrueCrypt Setup 7.1a.exe
/img_2017-B.dd/Users/computer/Pictures/czarny-kot-fakt.jpg
/img_2017-B.dd/Users/computer/Pictures/e0194eca1c8135636ce0e014341548c3.jpg
/img_2017-B.dd/Users/computer/Pictures/f03b7614dfadbbe4c2e8f88b69d12e04.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/3385141-cat-images.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/3385141-cat-images.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/4-ways-cheer-up-depressed-cat.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/cat-adult-landing-hero.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/cute-cat.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/e0194eca1c8135636ce0e014341548c3.jpg
/img_2017-B.dd/Users/computer/Documents/thestuff.zip/chaton_232339_w620.jpg
/img_2017-B.dd/Users/computer/Pictures/HP_PCC_md_0130_cat53.jpg
/img_2017-B.dd/Users/computer/Downloads/TrueCrypt/TrueCrypt User Guide.pdf
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/4C074A918ACE865639183E88679297964650C2DF
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/B3E5D71B0DDCBAF9F3C9D4EAC16E523B1FB2D678
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/269F3C3F4126B2031D2A144F4EF84D7A14273F90
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/8467BE0D69E7328222CBB79DF53ED078D46F54D8
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/6F3E4A118DAD9D8576803D01883A8D16C5C54E0A
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/0AC84C3118267CA8E9529B3B5EE7CB3FE97A8349
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/3DB7AD8A7467F14EE9041A7E5BB3212DE97CF72D
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/B794BA9708783353C13B56A4FCD91AC8C6BBFE9B
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/384CDE310ADA3D994DBBF6E7DB4E83FC7ADB41FA
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/7475FDC6010B10E9A92F8566A37722CAD23B740A
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/74EC9D0E06EC8CA48429A71B4F63721B9C46A7BE
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/8939CD0573DC670E939B63EE0BB8CF7CBF5D3759
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/E0865112772538A7107E90537AE882A566975C1D
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/5E822275D63B3969B1B1333DA2097A0B4128A952
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/CAE2DE00F17F37E9163C1A92D4A24311BA33CBEF
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/0F5FFD50A319226DEC8C39472F3F0E35497A1649
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/C4B4545713B119E4C08592F0BC6521F161C9978C
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/5ABEF7C3DB2D79AD5D736A7A6D72C07509E449EC
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/E5C1C021B3A9F9E7CC3AD4D252A77A7FA867A123
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/3E6BB475585EDE6ED38F6381D3FB71985B89DA12
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/68690FE1015CF969296B9D2C48106221381209AA
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/4B8CFD2C458C97F2023374C8CEDDCE8C18FFE78E
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/E1880A7470573E3128A1C476500E89D3C2235892
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/3D142110BE3848F161556E84F14DB025729E0ED5
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/A601DAA4FC321A4623A6B619C06790496CA769D6
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/9C74F94A82AE049470B683406D2A84F343E482F5
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/0AF0BE9A999DBCBD3351CC3687B49227C2644E54
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/BA23BD7804FA820A4833B07024384DE24FC1BC49
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/5F5D6630E8B61138D0BEC8E46ED1D28BDDAD1ECE
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/44E71A116A8058C725094237E62946F7981F0C3C
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/09529B15DC6B4F2EC1E416AE783B934E1C4879A1
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/773432A7F9E407F54FB759B177D4E176342DE372
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/395C9F251107BBD62D07C95AA07F596A2C0B24BF
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/CB0FDAAFD566F7970098AF91F1C4922D27625D6E
/img_2017-B.dd/Users/computer/Pictures/cat-black-superstitious-fcs-cat-myths-162286659.jpg
/img_2017-B.dd/Users/computer/Pictures/101438745-cat-conjunctivitis-causes.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_m_a_x_r_e_s_d_e_f_a_u_l_t_._j_p_g_
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/4-ways-cheer-up-depressed-cat.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/cat-adult-landing-hero.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/chaton_232339_w620.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/cute-cat.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/Sent Mail/_t_h_e_s_t_u_f_f_._z_i_p_/e0194eca1c8135636ce0e014341548c3.jpg
/img_2017-B.dd/Users/computer/AppData/Roaming/Thunderbird/Profiles/k71ku0d7.default/ImapMail/imap.gmail.com/[Gmail].sbd/All Mail/_m_a_x_r_e_s_d_e_f_a_u_l_t_._j_p_g_
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/thumbnails/a5e30fd021851bb6f1637fcadbe8fc67.png
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/8F36D78E96FF509F33D9AC6C8055AC15152CAAD6
""".splitlines()

data = [x for x in data if len(x) > 0]

extensions = []
for item in data:
    _, ext = os.path.splitext(item)
    extensions.append(ext)

extensions = list(set(extensions))
for item in extensions:
    print(item)

extensions = [
'.jpg',
'._j_p_g_',
'.zip',
'.exe',
'.txt',
'.png',
'.pdf',
]