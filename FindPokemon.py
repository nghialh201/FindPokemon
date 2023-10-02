import requests
res = requests.get("https://moonani.com/PokeList/index.php") #lấy dữ liệu link

import bs4
soup = bs4.BeautifulSoup(res.text,"lxml")

# print(*soup,sep="\n")

title_tag = soup.select('tbody tr td')
 
# print(*title_tag,sep="\n")

mang =[]
n = 100



for i in range(len(title_tag)//15):
    # print(i, title_tag[1+15*i].getText(), title_tag[2+15*i].getText(), title_tag[3+15*i].getText(), title_tag[5+15*i].getText(), title_tag[12+15*i].getText(), title_tag[13+15*i].getText())
    mang2 = []
    mang2.append(i)
    mang2.append(title_tag[1+15*i].getText())
    mang2.append(int(title_tag[2+15*i].getText()))
    mang2.append(title_tag[3+15*i].getText())
    mang2.append(int(title_tag[5+15*i].getText()))
    mang2.append(title_tag[12+15*i].getText()[11::])
    mang2.append(title_tag[13+15*i].getText())        
    mang.append(mang2)


# mang.sort()

print(*mang,sep="\n")
# print(type(mang[0][1]))

ListCatchToMega = [
    # {'key': 359, 'value': 'Absol'},
    {'key': 361, 'value':'Snorunt -> Glalie CP <=24'},
    # {'key': 302, 'value': 'Sableye CP max'},
    {'key': 477, 'value': 'Riolu -> Lucario CP <=32'},
    {'key': 448, 'value': 'Lucario CP <=32'},
    # {'key': 443, 'value': 'Gible -> Garchomp CP <= 21'},
    # {'key': 444, 'value': 'Gabite -> Garchomp CP <= 21'},
    # {'key': 445, 'value': 'Garchomp CP <= 21'},
    # {'key': 280, 'value': 'Ralt -> Gallade CP <= 16, CP <= 28'},
    # {'key': 281, 'value': 'Kirlia ->  Gallade CP <= 16, CP <= 28'},
    # {'key': 282, 'value': 'Gallade CP <= 16, CP <= 28'},
    # {'key': 318, 'value': 'Carvanha -> Sharpedo CP <=24'},
    # {'key': 319, 'value': 'Sharpedo CP <=24'},
    # {'key': 258, 'value': 'Mudkip -> Swampert, CP <=17'},
    # {'key': 259, 'value': 'Marshtomp -> Swampert, CP <=17'},
    # {'key': 260, 'value': 'Swampert, CP <=17'},
    # {'key': 607, 'value': 'Litwick -> Chandelure, CP <=15, CP max'},
    # {'key': 608, 'value': 'Lampent -> Chandelure, CP <=15, CP max'},
    # {'key': 609, 'value': 'Chandelure, CP <=15, CP max'}

]

# print(ListCatchToMega[0]['key'])



def TimMega(mang, ListCatchToMega):
    result = []
    for i in range(len(ListCatchToMega)):
        check = 0
        for j in range(len(mang)):
            # print(mang[j][2])
            if (ListCatchToMega[i]['key'] == mang[j][2]):
                if (check == 0):{
                    result.append(ListCatchToMega[i])
                }
                check = 1
                result.append(mang[j])

    print("\n\n"+"Kết quả tìm kiếm Mega:")
    print("https://moonani.com/PokeList/index.php")
    print(*result,sep="\n")


def TimThuong(mang, number):
    result = []
    for j in range(len(mang)):
        # print(mang[j][2])
        if (mang[j][2] == number):
            result.append(mang[j])

    print("\n\n"+"Kết quả tìm kiếm thường:")
    
    print(*result,sep="\n")


TimMega(mang,ListCatchToMega)
# TimThuong(mang,258)