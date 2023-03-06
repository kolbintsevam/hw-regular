from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
#Регулярка для отлова телефона и доп телефона
pattern = r'(8|\+7)?[\s-]?[-\s(]?(\d{3})[-\s)]?[-\s)]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?[(]?(доб.)?\s?(\d{4})?'
re_pattern = r'+7(\2)\3-\4-\5 \6\7'

#Забиваем в переменную lst переработанные элементы списка
lst = []
for i in contacts_list:
     all = i[0].split() + i[1].split() + i[2].split() + i[3:]
     lst.append(all)

#Проходимся регуляркой по всем элементам списка
for i in lst:
     try:
          match = re.findall(pattern, i[-2])
          result = ''.join(match[0])
          re_logick = re.sub(pattern, re_pattern, result)
          i[-2] = re_logick
     except:
          pass

#Создаем навый список чтобы корректно обьеденить дублированных людей в телефонной книге
last = [['test']]
#Промежуточная переменная w для удобства работы
w = []
for i in lst:
     for i2 in last:
          w.append(i2[0])
     if i[0] not in w:
          last.append(i)
          w.clear()
     #Если у нас находится повторение то начинается процесс обьеденения списков
     else:
          for i3 in last:
               if i3[0] in i:
                    count = 0
                    ww = []
                    while count <= 8:
                         try:
                              if len(i3[count]) > 1 or len(i[count]) < 1:
                                   if i3[count] not in ww:
                                        ww.append(i3[count])
                         except:
                              pass
                         try:
                              if len(i3[count]) < 1 or len(i[count]) > 1:
                                   if i[count] not in ww:
                                        ww.append(i[count])
                         except:
                              pass
                         count += 1
          #Удаляем старый список и записываем новый обьедененный
          for i4 in last:
               if i[0] == i4[0]:
                    last.remove(i4)
                    last.append(ww)
last.pop(0)
last.pop(0)
pprint(last)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(last)

