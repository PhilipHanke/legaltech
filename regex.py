import re

with open('bvger.txt', 'r') as file:
    fall_bvger = file.read().replace('\n', '') 

with open('bvger2.txt', 'r') as file:
    fall_bvger2 = file.read().replace('\n', '') 

with open('bger.txt', 'r') as file:
    fall_bger = file.read().replace('\n', '') 

suche1 = re.findall('[0-9]{1,2}\. \w+ [0-9]{4}', fall_bvger)
print(suche1[0])

bvger_faelle = [fall_bvger, fall_bvger2]

for fall in bvger_faelle:
  suche2 = re.findall('[A-Z]-\d{1,4}/\d{4}', fall)
  print(suche2[0])

suche3 = re.findall('\d[A-Z]_\d{1,4}/\d{4}', fall_bger)
print(suche3[0])

if "Urteil" in fall_bvger:
  print("Deutsch")

gesetze = re.findall('Art. \d{1,3} Abs. \d{1,3} [A-Za-z]{1,100}G', fall_bvger)
print(set(gesetze))


betrag = re.findall("Fr. \d{0,3}[']{0,1}\d{1,3}", fall_bvger)
print(set(betrag))
