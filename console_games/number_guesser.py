import random
import time


def player_input():
    global player_command
    player_command = input("Was sagst du? \n").lower()
    return player_command


def random_number_generator():
    random_number = random.randint(0, 501)
    return random_number


def low_high_check():
    if generated_number > player_guess:
        print("Deine Zahl ist niedriger, als die versteckte Zahl!")
    elif generated_number < player_guess:
        print("Deine Zahl ist höher, als die versteckte Zahl!")
    else:
        pass


def range_check():
    number_distance = abs(generated_number - player_guess)
    if 300 <= number_distance <= 999:
        print("Lösch dich!")
    elif 100 <= number_distance <= 299:
        print("Immer noch Lichtjahre entfernt!")
    elif 50 <= number_distance <= 99:
        print("Du bist wenigstens nicht mehr 3-Stellig entfernt!")
    elif 20 <= number_distance <= 49:
        print("Du kommst näher!")
    elif 10 <= number_distance <= 19:
        print("Du bist nah dran!")
    elif 5 <= number_distance <= 9:
        print("Es fehlt nicht mehr viel! Du hast es fast geschafft!")
    elif generated_number == player_guess:
        print("ES IST UNFASSBAR, DU HAST DIE ZAHL ERRATEN!")
        print("Noch eine Runde (Reset) oder nicht?(Beenden)")
    else:
        print("Oh so knapp, komm schon!")


def write_score():
    pass


def access_score():
    pass


# Alle Spielerkommandos
commands = str("""
Folgende Kommandos sind im Menü verfügbar (Groß-/Kleinschreibung spielt bei den Kommandos keine Rolle!

Hilfe - Gibt die Befehlsliste wieder
Start - Beginnt ein Spiel
Beenden - Verlässt das Programm
Regeln - Präsentiert das Regelwerk
Score - Präsentiert die aktuell Highscoreliste

Folgende Kommandos empfehlen sich nur während eines Spiels:

Reset - Unterbricht das laufende Spiel und setzt alles auf Null zurück
Versuche - Zeigt an, wie oft in dieser Runde bereits geraten wurde
""")

# Enthält alle Spielregeln und die Ranges für das Zahlenraten
rules = str("""

Die Regeln lauten wie folgt:

1. Es muss eine Zahl erraten werden die im Bereich 0 - 1000 liegt. Dabei sind diese Zahlen selbst mit eingeschlossen!
2. Der Computer gibt dir Hinweise, ob die Zahl höher oder niedriger ist und wie weit weg du bist (range):

Range 300 - 999: "Lösch dich!"
Range 100 - 299: "Immer noch Lichtjahre entfernt!"
Range 50 - 99: "Du bist wenigstens nicht mehr 3-Stellig entfernt!"
Range 20 - 49: "Du kommst näher!"
Range 10 - 19: "Du bist nah dran!"
Range 5 - 9: "Es fehlt nicht mehr viel! Du hast es fast geschafft!"
Range 1 - 4: "Oh so knapp, komm schon!"

3. Deine Versuche werden mitgezählt und dir anschließend mitgeteilt.

Viel Spaß beim spielen!
""")


# Beginn der Spiellogik


player_command = ""

print(f"""
Vor dir steht ein Gremlin, eine mythische Kreatur des bösen.
Er fordert dich zu einem Zahlenratespiel heraus!
Wenn du nicht weißt, was du tun sollst, wäre die Frage nach 'Hilfe' eine gute Idee!
""")

# Beginn der Spiellogik

exit_program = False
while not exit_program:
    player_input()
    if player_command == "beenden":
        break

    # ruft die Hilfe auf
    if player_command == "hilfe":
        print(commands)

    # gibt die Regeln aus
    if player_command == "regeln":
        print(rules)

    # Zweig muss noch programmiert werden
    if player_command == "score":
        access_score()

    # Beginn einer aktiven Runde
    if player_command == "start":
        exit_loop = False
        while not exit_loop:
            print('Willkommen in einer Runde Zahlenraten! Deine Zahl wird jetzt generiert...')
            time.sleep(3)
            player_guess = 0
            try_count = 0
            generated_number = random_number_generator()
            print('Deine Zahl wurde nun generiert!')

            while True:
                player_input()
                if player_command.isdigit():
                    try_count += 1
                    player_guess = int(player_command)
                    low_high_check()
                    range_check()

                if player_command == "reset":
                    break

                if player_command == "versuche":
                    print(try_count)

                if player_command == "beenden":
                    exit_program = True
                    exit_loop = True
                    break

















