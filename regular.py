from pprint import pprint
import csv
import re
import decor

@decor.log_decor('hw/pyth')
def names_order(contackts:list) ->list:


  pattern = re.compile(r"(\+7|8)?\s*[\(]*(495)\)*[-\s]*(\d\d\d)+[-\s]*(\d\d)[-\s]*(\d\d)[\s\(]*(доб.)*\s*(\d*)\)*")
  for element in contackts :
    str1 = element[0].split()
    if len(str1) > 1:
      for i in range (len(str1)):
        element[i] = str(str1[i])
    str2 = element[1].split()
    if len(str2) > 1:
      for i in range (1,len(str2)):
        element[i] = str(str2[i-1])
    if element[5]:
      # pprint (element[5]) 
      substitution = r'+7(\2)\3-\4-\5 \6\7'
      element[5] = re.sub(pattern, substitution, element[5])
  
  # проверка дубликатов
  # создаем словарь с уникальными кортежами имени и фамилии в качестве ключей
  # и положением в списке в качестве значения
  
  names = {}
  contackts2 = []
  for (offset,element) in enumerate(contackts) :
    if (element[0],element[1]) in names.keys():
      offs = names[element[0],element[1]]
      for i in range(2,7):
        if element[i] != '' and contackts[offs][i] == '':
          contackts[offs][i] = element[i]
    else:
      names[element[0],element[1]] = offset
      contackts2.append(element)
  
      
      
           
      
  return contackts2
      

if __name__ == '__main__':


  with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  header = []
  header = contacts_list[:1]
  body = []
  body = contacts_list[1:]
  new_body = names_order(body)
  final_list = header 
  final_list.extend(new_body)
  pprint(final_list)

  with open("phonebook.csv", "w") as f:
     datawriter = csv.writer(f, delimiter=',')
     datawriter.writerows(final_list)

  








