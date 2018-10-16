''' Das folgende Programm fragt das Alter und den Kanton des Nutzers/der Nutzerin ab 
und gibt Auskunft, ob er/sie Zigaretten kaufen darf '''

# Fragt das Alter ab.
alter = input("Wie alt bist Du? ")

# Konvertiert das Alter von Text ("String") zu Zahl ("Integer").
# Die Funktionen int() und str() machen solche Konversionen.
alter = int(alter)

# Frage nach dem Kanton
location = input("Wo wohnst Du? (Kantonsabkürzung)")

# Liste der Kantone, in denen das zulässige Alter 16 Jahre ist.
sechzehn = ["ZH", "AR", "SG", "TG", "AG", "UR", "SZ", "VD"]

# Liste der Kantone ohne Altersbeschränkung
ohne_alterslimit = ["GE", "AI", "GL"]

# Wir definieren eine Funktion, die für ein jeweiliges Alter 
# und den massgeblichen Kanton Auskunft gibt, ob der Kauf von Zigaretten gestattet ist.
def zigaretten_check(alter, location):
    if (alter >= 16) and (location in sechzehn):
        print("Du darfst Zigaretten kaufen.")
    elif (alter < 16) and (location in ohne_alterslimit):
        print("Du darfst Zigaretten kaufen.")
    elif alter >= 18:
        print("Du darfst Zigaretten kaufen.")
    else:
        print("Zu jung!")
# Hinweis: Dieser Code könnte effizienter geschrieben werden (tatsächlich wiederholt er sich etwas). 
# Dafür wären der sogenannte "or"-Operator notwendig. Bisher haben wir nur "and" verwendet.


# Schliesslich müssen wir die Funktion auch noch abrufen, damit sie ausgeführt wird.
zigaretten_check(alter, location)
