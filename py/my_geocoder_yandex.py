from geocoder import yandex
import os

adresses = input("Введите путь до csv файла с адресами: ")
adress_file = open(adresses, encoding="UTF8")
adress_coord_file = open(adresses[:-3] + 'txt', 'w', encoding="UTF8")
adresses_list = adress_file.readlines()
adress_coord = []
print(len(adresses_list))

for i in range(len(adresses_list)):
    adresses_list[i] = adresses_list[i].split(';')
    print(adresses_list[i][1])
    adress_coord.append(yandex(adresses_list[i][5]).latlng)
    adress_coord_file.write((str(adresses_list[i]) + ';' + str(adress_coord[i])).replace("['", '').replace("']", '').replace("', '", ';'))


adress_coord_file.close()




