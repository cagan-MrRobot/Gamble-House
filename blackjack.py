

import tkinter as tk
import random


def start_blackjack():
    blackjack_window = tk.Toplevel()
    blackjack_window.title("Welcome to Blackjack")
    blackjack_window.geometry("800x600")

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def create_deck():
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(
                    {'suit': suit, 'rank': rank, 'value': values[rank]})

        return deck
    game_deck = create_deck()
    random.shuffle(game_deck)

    def play_again():
        blackjack_window.destroy()

        start_blackjack()

    player_hand = []
    dealer_hand = []

    def deal_card(hand):
        card = game_deck.pop()
        hand.append(card)

    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)

    def calculate_value(hand):
        total = 0
        ace_count = 0

        for card in hand:
            total += card['value']
            if card['rank'] == 'Ace':
                ace_count += 1

            while total > 21 and ace_count > 0:
                total -= 10
                ace_count -= 1

        return total
    player_score = calculate_value(player_hand)
    dealer_score = calculate_value(dealer_hand)

    dealer_frame = tk.Frame(blackjack_window)
    dealer_frame.pack(pady=20)

    dealer_label = tk.Label(
        dealer_frame, text="Dealer's Hand", font=('Arial', 14))
    dealer_label.pack()

    player_frame = tk.Frame(blackjack_window)
    player_frame.pack(pady=20)

    player_label = tk.Label(
        player_frame, text="Player's Hand", font=('Arial', 14))
    player_label.pack(pady=20)

    dealer_score_label = tk.Label(dealer_frame, text='', font=('Arial', 12))
    dealer_score_label.pack()

    dealer_cards_label = tk.Label(dealer_frame, text='', font=("Arial", 20))
    dealer_cards_label.pack()

    player_score_label = tk.Label(player_frame, text='', font=('Arial', 12))
    player_score_label.pack()

    player_cards_label = tk.Label(player_frame, text='', font=("Arial", 20))
    player_cards_label.pack()

    def update_display():
        player_card_text = ''
        for card in player_hand:
            player_card_text += f"{card['rank']} of {card['suit']}\n"

        player_cards_label.config(text=player_card_text)
        player_score_label.config(text=f"Score: {player_score}")

        dealer_card_text = f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}\n"
        dealer_card_text += '???\n'

        dealer_cards_label.config(text=dealer_card_text)
        dealer_score_label.config(text=f'Score:{dealer_hand[0]['value']}')

    update_display()

    button_frame = tk.Frame(blackjack_window)

    hit_button = tk.Button(blackjack_window, text='HIT', font=("Arial", 15))
    stand_button = tk.Button(
        blackjack_window, text='STAND', font=('Arial', 15))
    hit_button.pack()
    stand_button.pack()

    status_label = tk.Label(blackjack_window, text="",
                            font=('Arial', 16, 'bold'))
    status_label.pack(pady=20)

    play_again_button = tk.Button(
        blackjack_window, text='Play Again?', font=("Arial", 14), command=play_again)
    play_again_button.pack(pady=20)
    play_again_button.pack_forget()

    def player_hit():
        nonlocal player_score
        deal_card(player_hand)
        player_score = calculate_value(player_hand)
        update_display()

        if player_score > 21:
            status_label.config(
                text=f'Score: {player_score} - BUST! DEALER WINS')
            hit_button.config(state='disabled')
            stand_button.config(state='disabled')
            play_again_button.pack()

    hit_button.config(command=player_hit)

    def dealer_play():
        nonlocal dealer_score
        dealer_score = calculate_value(dealer_hand)

        while dealer_score < 17:
            deal_card(dealer_hand)
            dealer_score = calculate_value(dealer_hand)

        return dealer_score

    def player_stand():

        nonlocal dealer_score

        hit_button.config(state='disabled')
        stand_button.config(state='disabled')

        dealer_score = dealer_play()

        dealer_card_text = ""
        for card in dealer_hand:
            dealer_card_text += f'{card['rank']} of {card['suit']}\n'

        dealer_cards_label.config(text=dealer_card_text)
        dealer_score_label.config(text=f'Score:{dealer_score}')

        dealer_play()

        if dealer_score > 21:
            result_text = "DEALER BUSTS! PLAYER WINS!"
        elif dealer_score > player_score:
            result_text = "DEALER WINS!"
        elif dealer_score < player_score:
            result_text = "PLAYER WINS!"
        else:
            result_text = "TIE"
        status_label.config(text=result_text)
        play_again_button.pack()

    stand_button.config(command=player_stand)

