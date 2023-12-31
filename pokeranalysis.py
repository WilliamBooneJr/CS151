import stdrandom
import stdstats
import stdarray
import stddraw
import stdio

card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def gen_hand():
    #The gen_hand Function will create a deck of 52 cards and shuffle them. Will then draw 5 cards from the deck and return them as a hand.
    deck = stdarray.create1D(52, 0)
    for i in range (52):
        deck[i] = i
    stdrandom.shuffle(deck)
    hand = deck[:5]
    return hand


def hand_ranks(hand):
    # The hand_rank function will take the hand and determine what type it is. Then returns its type.
    ranks = [card % 13 for card in hand]
    suits = [card // 13 for card in hand]
    rank_counts = [ranks.count(rank) for rank in ranks]
    suit_counts = [suits.count(suit) for suit in suits]
    if 4 in rank_counts:
        return "Four of a kind"
    elif 3 in rank_counts and 2 in rank_counts:
        return "Full house"
    elif 3 in rank_counts:
        return "Three of a kind"
    elif rank_counts.count(2) == 2:
        return "One pair"
    elif rank_counts.count(1) == 1:
        return "Two pair"
    elif 5 in suit_counts:
        return "Flush"
    else:
        return "High card"



def simulate(num_trials):
    # The simulate function will take the number of trials and simulate that many hands. It will then return the counts of each type of hand.
    counts = {"High card": 0, "One pair": 0, "Two pair": 0, "Three of a kind": 0, "Full house": 0, "Four of a kind": 0, "Flush": 0}
    for i in range(num_trials):
        hand = gen_hand()
        rank = hand_ranks(hand)
        counts[rank] += 1
    return counts


def calc_prob(counts, num_trials):
    # The calc_Prob will take the counts of each type of hand and the number of trials and calculate the probability of each hand.
    probabilities = {}
    for rank, count in counts.items():
        probabilities[rank] = count / num_trials
    return probabilities


# The Test Client
def main(num_trials):
    counts = simulate(num_trials)
    probabilities = calc_prob(counts, num_trials)
    for rank, probability in probabilities.items():
        print(f"{rank}: {probability:.4f}")
    pure_values = [value for value in probabilities.values()]
    stdstats.plotBars(pure_values)
    stddraw.show()
    
if __name__ == "__main__":
    main(1000)