import random
import time


# function to get the player input
def player_input():
    global player_command
    player_command = input("Was sagst du? \n").lower()
    return player_command


# creates the random number within a specified range
def random_number_generator():
    random_number = random.randint(0, 501)
    return random_number


# checks if the guessed number is below or above the "hidden" number and hints it to the player
def check_low_high():
    if generated_number > player_guess:
        print("Deine Zahl ist niedriger, als die versteckte Zahl!")
    elif generated_number < player_guess:
        print("Deine Zahl ist höher, als die versteckte Zahl!")
    else:
        pass


# this function calculates the difference between the guessed number and the "hidden" number and gives out range hint
def check_range():
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


# logic for scoreboard still needs to be implemented, therefore this function is still empty
def write_score():
    pass


# logic for scoreboard still needs to be implemented, therefore this function is still empty
def access_score():
    pass


# a list of all available player commands
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

# contains all game rules and ranges for number guessing
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


# game logic starts here
player_command = ""

print(f"""
Vor dir steht ein Gremlin, eine mythische Kreatur des bösen.
Er fordert dich zu einem Zahlenratespiel heraus!
Wenn du nicht weißt, was du tun sollst, wäre die Frage nach 'Hilfe' eine gute Idee!
""")

class GuessingGame:

    def __init__(self):

        self.player_guess = 0
        self.try_count = 0
        self.generated_number = random_number_generator()
        print('Deine Zahl wurde nun generiert!')

    def check_guess(self, guess:int) -> bool:
        self.try_count += 1
        self.player_guess = int(guess)
        self.check_low_high()
        return self.check_range()

    def check_low_high(self):
        if self.generated_number > self.player_guess:
            print("Deine Zahl ist niedriger, als die versteckte Zahl!")
        elif self.generated_number < self.player_guess:
            print("Deine Zahl ist höher, als die versteckte Zahl!")
        else:
            pass

    # function calculates the difference between the guessed number and the "hidden" number and gives out range hint
    def check_range(self):
        number_distance = abs(self.generated_number - self.player_guess)
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
        elif self.generated_number == self.player_guess:
            print("ES IST UNFASSBAR, DU HAST DIE ZAHL ERRATEN!")
            print("Noch eine Runde (Reset) oder nicht?(Beenden)")
            return True
        else:
            print("Oh so knapp, komm schon!")
        return False


exit_program = False
while not exit_program:
    player_input()
    if player_command == "beenden":
        exit_program = True

    # shows help
    if player_command == "hilfe":
        print(commands)

    # prompts the rules
    if player_command == "regeln":
        print(rules)

    # Path still needs to be programmed
    if player_command == "score":
        access_score()

    # start of a new round
    if player_command == "start":
        print('Willkommen in einer Runde Zahlenraten! Deine Zahl wird jetzt generiert...')
        game_state = GuessingGame()
        # sleep time is just added to give impression to player there is some calculation done to generate the number, just for "immersion" reasons
        time.sleep(3)

        while True:
            player_input()
            if player_command.isdigit():
                if game_state.check_guess(player_command):
                    print("you won the gmae, press reset to start again.")
                else:
                    print("more luck next time.")

            if player_command == "reset":
                game_state = GuessingGame()

            if player_command == "versuche":
                print(game_state.try_count)

            if player_command == "beenden":
                exit(0)


















