"""

KEY: Value
Einträge können nachtröglich eingefügt / entfernt werden.

"""

d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}

print(d["Berlin"])

# nachträglich einfügen

d["Budapest"] = "BUD"

print(d)

# Löschen durch del

del d["Budapest"]
print(d)

# Element in Dict enthalten

if "Helsinki" in d:
    print('Ist enthalten')


# gibt einfach den Wert none aus, falls nicht vorhanden und führt nicht in einen Error
print(d.get("Budapest"))
# mit eckiger Klammer führt es in einen Fehler, ist aber eher zu empfehlen um ungewollte Effekte / Bugs zu vermeiden
print(d["Budapest"])