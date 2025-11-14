import tkinter as tk
from blackjack import start_blackjack
from roulettes import start_roulette
from slot import start_slot

window = tk.Tk()

window.geometry("500x300")
window.title("Gamble House")

label = tk.Label(window, text="Welcome to the Gamble House")
label.pack()

select = tk.Label(window, text="Select a game")
select.pack(padx=20, pady=20)

blackjack_button = tk.Button(window, text='Blackjack', command=start_blackjack)
blackjack_button.pack()

roulette_button = tk.Button(window, text='Roulette', command=start_roulette)
roulette_button.pack()

slot_button = tk.Button(window, text='Slot', command=start_slot)
slot_button.pack()


window.mainloop()
