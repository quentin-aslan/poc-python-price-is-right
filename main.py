# Init global variables
import random
import time

playerName1 = ""
playerName2 = ""

Dialogue = ["",
            "voix-off : Bonjour et bienvenue au Prix Juste, avec pour présentateur, Vincent FAIGAF !",
            "Vincent Faigaf : BIP BIP",
            "Le public : OUAIIIIIIS !",
            "Vincent Faigaf : Et on commence tout de suite avec nos premiers candidats !",
            "Notre premier candidat est : ",
            "Il affrontera : ",
            "Nous allons tout de suite commencer avec le premier produit."
            ]

Products = {"Ecran": {
    "name": "Ecer Gaming",
    "price": random.randint(180, 230)},
    "Console": {
        "name": "Nantendo Swatch", "price": random.randint(250, 320)
    },
    "Unité centrale": {
        "name": "NSA Gaming",
        "price": random.randint(1000, 1200)},
    "Télévision": {
        "name": "Somsing QLED",
        "price": random.randint(1000, 1500)},
    "Enceinte": {
        "name": "JPL PoomPox",
        "price": random.randint(100, 180)
    },
}


def main():
    askPlayersName()
    registerPlayers()
    # storyTeller()
    product = chooseRandomProduct()
    print("Vous devez trouver le prix de ce produit : ", product.get("name"))
    gameLoop(product)


def gameLoop(product):
    price = product.get("price")

    player1choice = int(input(playerName1 + ", please enter your choice: "))
    playerTurnVerification(player1choice, price, playerName2)
    if player1choice == price:
        print(playerName1 + ", you win !")
        return

    player2choice = int(input(playerName2 + ", please enter your choice: "))
    if player2choice == price:
        print(playerName2 + ", you win !")
        return

    playerTurnVerification(player2choice, price, playerName1)

    if player1choice != price and player2choice != price:
        gameLoop(product)


def playerTurnVerification(valuePlayer, price, nextPlayerName):
    if valuePlayer < price:
        print("C'est plus ! Au tour de " + nextPlayerName)
    elif valuePlayer > price:
        print("C'est moins ! Au tour de " + nextPlayerName)


# Ask the players for their name
def askPlayersName():
    global playerName1
    global playerName2

    while not isValidUsername(playerName1):
        playerName1 = input("Player 1, please enter your name: ")

    while not isValidUsername(playerName2):
        playerName2 = input("Player 2, please enter your name: ")


# Check if the username is valid
def isValidUsername(username):
    if 3 < len(username) < 20:
        return True


# Add players name to the dialogue
def registerPlayers():
    Dialogue[5] = Dialogue[5] + "" + playerName1
    Dialogue[6] = Dialogue[6] + "" + playerName2


# Print text when delay is over
def printText(text, delay):
    time.sleep(delay)
    print(text)


# Print dialogue
def storyTeller():
    printText(Dialogue[1], 0)
    printText(Dialogue[2], 2)
    printText(Dialogue[3], 2)
    printText(Dialogue[4], 2)
    printText(Dialogue[5], 2)
    printText(Dialogue[6], 2)
    printText(Dialogue[7], 2)


def chooseRandomProduct():
    randomProductName = random.choice(list(Products.keys()))
    return Products.get(randomProductName)


main()
