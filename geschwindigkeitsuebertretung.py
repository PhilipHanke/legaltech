
def geschwindigkeitsuebertretung():
    location = input("Wo bist Du gefahren? (innerorts, ausserorts, Autobahn)")
    geschwindigkeit = input("Wie schnell bist Du gefahren? ")
    geschwindigkeit = int(geschwindigkeit)

    if (((50 <= geschwindigkeit <= 70) and (location == "innerorts")) or ((120 <= geschwindigkeit < 150) and (location == "Autobahn"))) or ((80 < geschwindigkeit <= 105) and (location == "ausserorts")):
        print("Du bekommst eine Busse!")
    elif ((geschwindigkeit > 105) and (location == "ausserorts")) or ((geschwindigkeit > 150) and (location == "Autobahn")):
        print("Führerausweis wird entzogen")    
    elif (geschwindigkeit > 70) and (location == "innerorts"):
        print("Führerausweis wird entzogen")
    elif ((geschwindigkeit < 50) and (location == "innerorts")) or ((geschwindigkeit < 80) and (location == "ausserorts")) or ((geschwindigkeit < 120) and (location == "Autobahn")):
        print("Alles gut.")


geschwindigkeitsuebertretung()
