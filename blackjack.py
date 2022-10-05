import random

# deck of cards / player dealer hand
class game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    player_hand = []
    dealer_hand = []
    player_in = True
    dealer_in = True

# deal the cards
    def dealCard(self, turn):
        self.turn = turn
        card = random.choice(game.deck)
        self.card = card
        self.turn.append(card)
        game.deck.remove(card)

    # calculate the total of each hand
    def total(self, turn):
        self.turn = turn
        total_var = 0
        for card in self.turn:
            total_var += card
        return total_var

    # check for winner
    def revealDealerHand(self):
        if len(game.dealer_hand) == 2:
            return game.dealer_hand[0]
        elif len(game.dealer_hand) > 2:
            return game.dealer_hand[0], game.dealer_hand[1]

    def deal(self):
        for _ in range(2):
            game.dealCard(self, game.dealer_hand)
            game.dealCard(self, game.player_hand)

    def gameLoop(self):
        player_in = True
        dealer_in = True
        while player_in or dealer_in:
            print(f"Dealer has {game.revealDealerHand(self)} and X")
            print(f"You have {game.player_hand} for a total of {game.total(self, game.player_hand)}")
            if game.total(self, game.player_hand) == 21:
                print("BLACK JACK! YOU WIN!")
                break
            if game.total(self, game.player_hand) > 21 and game.total(self, game.dealer_hand) <= 21:
                print("You busted on the deal. Dealer wins.")
                break
            if game.total(self, game.player_hand) > 21 and game.total(self, game.dealer_hand) > 21:
                print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
                print("Double bust on the deal! Try again!")
            if player_in:
                stay_or_hit = input("1: Stand\n2: Hit\n")
            if game.total(self, game.dealer_hand) > 16:
                game.dealer_in = False
            if dealer_in:
                game.dealCard(self, game.dealer_hand)
            if stay_or_hit == '1':
                player_in = False
            else:
                game.dealCard(self, game.player_hand)
            if game.total(self, game.player_hand) > 21:
                break
            elif game.total(self, game.dealer_hand) > 21:
                dealer_in = False
                break

    def determineWinner(self):
        if game.total(self, game.player_hand) == 21 and game.total(self, dealer_hand) != 21:
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("You win!")
        elif game.total(self, game.dealer_hand) == 21 and game.total(self, game.player_hand) != 21:
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("Dealer wins.")
        elif game.total(self, game.dealer_hand) > 21 and game.total(self, game.player_hand) > 21:
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("Double bust! Try again!")
        elif game.total(self, game.player_hand) > 21:
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("You bust! Dealer wins.")
        elif game.total(self, game.dealer_hand) > 21:
            print(f"\nYou have {game.player_hand} for a total of {game.total(self,game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("Dealer busts! You Win!")
        elif 21 - game.total(self, game.dealer_hand) < 21 - game.total(self, game.player_hand):
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("Dealer wins.")
        elif 21 - game.total(self, game.dealer_hand) > 21 - game.total(self, game.player_hand):
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("You win!")
        elif game.total(self, game.dealer_hand) == game.total(self, game.player_hand):
            print(f"\nYou have {game.player_hand} for a total of {game.total(self, game.player_hand)} and the dealer has {game.dealer_hand} for a total of {game.total(self, game.dealer_hand)}")
            print("Game tied. Try again!")

blackjack = game()

def run():
    print("Welcome to Black Jack!")
    blackjack.deal()
    blackjack.gameLoop()
    blackjack.determineWinner()

run()
