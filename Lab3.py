import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def draw_cards(self, num_cards):
        self.cards = [random.randint(1, 9) for _ in range(num_cards)]

    def play_card(self):
        return self.cards.pop() if self.cards else None

    def add_card(self, card):
        self.cards.insert(0, card)

    def __str__(self):
        return f"{self.name}: {self.cards}"


def print_state(player1, player2, table):
    print(f"STATE: {player1} --- {player2} --- Table: {table}")


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    player1.draw_cards(5)
    player2.draw_cards(5)

    table = []
    transfer_count = 0
    turn = 0

    print("Initial situation:")
    print_state(player1, player2, table)
    print("\nStarting the game...\n")

    while True:
        current_player = player1 if turn == 0 else player2
        played_card = current_player.play_card()

        if played_card is None:
            print(f"{current_player.name} has no cards left!")
            break

        print(f"{current_player.name} put {played_card}")
        table.append(played_card)

        if len(table) > 1 and played_card == table[-2]:
            print(f"{current_player.name} takes {played_card}")
            transfer_count += 1
            if turn == 0:
                player2.add_card(played_card)
            else:
                player1.add_card(played_card)

        print_state(player1, player2, table)

        if table.count(9) == 3:
            print("Game ends: There are three cards with the number 9 on the table.")
            break
        if len(table) == 8:
            print("Game ends: 8 cards on the table.")
            break
        if played_card == 7:
            print("Game ends: Played card is 7.")
            break
        if len(table) > 1 and played_card == table[-2] + 1:
            print("Game ends: Played card is 1 greater than the previous.")
            break
        if len(table) > 1 and played_card == table[-2] - 1:
            print("Game ends: Played card is 1 less than the previous.")
            break
        if all(card % 2 == 0 for card in current_player.cards):
            print(f"Game ends: {current_player.name} has only even cards.")
            break
        if all(card % 2 != 0 for card in current_player.cards):
            print(f"Game ends: {current_player.name} has only odd cards.")
            break
        if sum(table) == 20:
            print("Game ends: The sum of points on the table is 20.")
            break
        if transfer_count == 2:
            print("Game ends: Card transfer has happened twice.")
            break

        turn = 1 - turn

    if player1.cards == [] and player2.cards == []:
        print("Game ended without a clear winner.")
    elif player1.cards == []:
        print(f"Winner: {player2.name}")
    elif player2.cards == []:
        print(f"Winner: {player1.name}")
    else:
        print("Game ended without a winner.")

if __name__ == "__main__":
    main()