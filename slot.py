import tkinter as tk
import random


def start_slot():
    slot_window = tk.Toplevel()
    slot_window.title("Welcome to Slot")
    slot_window.geometry("400x400")

    frame = tk.Frame(slot_window)
    frame.pack(pady=20)

    slot_symbols = ['🍒', '🍇', '🍉', '7️⃣']

    label1 = tk.Label(frame, text='?', font=('Arial', 60))
    label1.pack(side='left', padx=30)

    label2 = tk.Label(frame, text='?', font=('Arial', 60))
    label2.pack(side='left', padx=30)

    label3 = tk.Label(frame, text="?", font=('Arial', 60))
    label3.pack(side='left', padx=30)

    result_label = tk.Label(slot_window, text='', font=('Arial', 30))
    result_label.pack(pady=10)

    def spin_slot():
        finished = 0
        result_label.config(text='')
        counts = [10, 15, 20]

        def animate(label, count):
            nonlocal finished

            if count > 0:
                label.config(text=random.choice(slot_symbols))
                slot_window.after(100, animate, label, count-1)
            else:
                finished += 1
                if finished == 3:
                    check_results()

        animate(label1, counts[0])
        animate(label2, counts[1])
        animate(label3, counts[2])

    spin_button = tk.Button(slot_window, text='SPIN!',
                            font=('Arial', 40), command=spin_slot)
    spin_button.pack(pady=40)

    def check_results():
        result1 = label1.cget('text')
        result2 = label2.cget('text')
        result3 = label3.cget('text')

        if result1 == result2 == result3:
            result_label.config(text="🎉 YOU WIN 🎉", fg='green')
        else:
            result_label.config(text='💀 YOU LOST 💀', fg='red')

    slot_window.after(3000, check_results)
