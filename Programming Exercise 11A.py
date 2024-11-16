import random

# Card and Deck classes as defined in Section 11.5
class Card:
    """Represents a standard playing card."""

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a human-readable string representation."""
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"


class Deck:
    """Represents a deck of cards."""

    def __init__(self):
        """Initialize the deck with 52 cards."""
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def deal(self, num):
        """Deal num cards from the deck."""
        if num > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal.")
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards


# Poker Hand Game
def poker_hand_game():
    # Initialize and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal a hand of 5 cards
    hand = deck.deal(5)
    print("Initial Hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")

    # Prompt the user for cards to replace
    replace_indices = input(
        "\nEnter the numbers of the cards you want to replace (comma-separated, e.g., 1,3,5): "
    )
    try:
        indices = [int(x.strip()) - 1 for x in replace_indices.split(",") if x.strip().isdigit()]
        if any(idx < 0 or idx >= 5 for idx in indices):
            raise ValueError("Indices out of range. Please choose between 1 and 5.")
    except ValueError as e:
        print("Invalid input:", e)
        return

    # Replace the selected cards
    for idx in indices:
        if len(deck.cards) > 0:
            hand[idx] = deck.deal(1)[0]

    # Print the updated hand
    print("\nFinal Hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")

poker_hand_game()
