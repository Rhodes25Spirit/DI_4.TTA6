'''author = "Anna Spirit LEVY"'''

from tkinter import *
from random import randint
from functools import partial

class GameYams:

    options = ["1", "2", "3", "4", "5", "6", "One_Pair", "Two_Pairs", "Three_of_king", "Straight", "Full", "Four_of_king", "Yams"]
    points  = [1]*6 + [25 + k*5 for k in range(6)] + [100]

    def __init__(self, master):

        self.master = master
        
        self.choices = {}
        for option in self.options:
            self.choices[option]=False
        
        self.current_turn = 1
        self.throw_this_turn = 0

        self.gains = []

        self.turn = StringVar()
        self.turn.set("Turn #1")

        self.score = StringVar()
        self.score.set("Score: 0")

        self.frame_header = Frame(master, width=700)

        self.label_score = Label(self.frame_header, textvariable=self.score, font=("Courier", 14, "bold"))
        self.label_turn = Label(self.frame_header, textvariable=self.turn, font=("Courier", 14, "bold"))

        self.button_throw_dices = Button(master, text="Throw dices", fg="BLUE", pad_x=10, pad_y=10, command=self.throw_dices)

        self.frame_dices = Frame(master)
        self.dice_values = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        self.dice_labels = [Label(self.frame_dices, textvariable=self.dice_values[i], width=11, borderwidth=2, relief="groove", height=5, justify=CENTER, font=("Courier", 13, "bold")) for i in range(5)]
        
        self.dices_selected = [True] *5

        self.dices_can_be_clicked = False

        for label in self.dice_labels
        :
            label.bind("<Button-1>", self.toggle_dice_selection)

        self.frame_buttons_end_of_turn = Frame(master)
        self.frame_buttons_end_of_turn_left = Frame(self.frame_buttons_end_of_turn)
        self.frame_buttons_end_of_turn_right = Frame(self.frame_buttons_end_of_turn)

        self.buttons_choice_end_of_turn = []
        for i, choice in enumerate(self.options[:-1]):
            self.buttons_choice_end_of_turn.append(Button(self.frame_buttons_end_of_turn_left if i < 6 else self.frame_buttons_end_of_turn_right, width=10,text=choice, font=("Courier", 10), command=partial(self.choose_and_start_new_turn, i)))

        self.buttons_choice_end_of_turn.append(Button(master, text="YAMS!", width=22, font=("Courier", 10)))

        self.init_user_interface()


    @property
    def dices(self):
        return [self.dice_values[i].get() for i in range(5)]
    

    def throw_dices(self):
        self.throw_this_turn += 1
        for i in range(5):
            if self.dices_selected[i]:
                self.dice_values[i].set(randint(1,6))
                self.dice_labels[i].config(fg="BLACK")

        self.button_throw_dices.config(state=DISABLED)
        self.dices_can_be_clicked = True
        self.dices_selected = [False]*5
        print(self.dices)
        self.compute_choices()


    def choose_and_start_new_turn(self, option):
        self.choices[self.options[option]] = None
        self.gains.append(self.points[option])
        self.score.set("Score: {}".format(sum(self.gains)))
        self.current_turn += 1
        self.turn.set("Turn #{}".format(self.current_turn))
        self.init_dices_for_new_turn()


    def toggle_dice_selection(self, event):
        
        if self.dices_can_be_clicked and self.throw_this_turn < 3:

            dice_clicked = [ event.widget == self.dice_labels[i] for i in range(5) ].index(True)

            self.dices_selected[dice_clicked] = not self.dices_selected[dice_clicked]

            if self.dices_selected[dice_clicked]: event.widget.config(fg="BLUE")
            else: event.widget.config(fg="BLACK")

            if True in self.dices_selected: self.button_throw_dices.config(state=NORMAL)

    def compute_choices(self):

        occurrence = [self.dices.count(i) for i in range(1,7)]

        if 5 in occurrence and self.choices["Yams"] is not None: self.choices["Yams"] = True
        if 4 in occurrence and self.choices["Four_of_king"] is not None: self.choices["Four_of_king"] = True
        if 2 in occurrence and 3 in occurrence and self.choices["Full"] is not None : self.choices["Full"] = True
        if 3 in occurrence and 1 in occurrence and self.choices["Three_of_king"] is not None : self.choices["Three_of_king"] = True
        if occurrence.count(2) == 2 and self.choices["Two_Pairs"] is not None : self.choices["Two_Pairs"] = True
        if occurrence.count(2) == 1 and self.choices["One_Pair"] is not None : self.choices["One_Pair"] = True
        if occurrence.count(1) == 5 and self.choices["Straight"] is not None and (occurrence[0]==0 or occurrence[-1]==0): self.choices["Straight"] = True
        
        for i in range(6):
            if occurrence[i] > 0 and self.choices[str(i+1)] is not None: self.choices[str(i+1)] = True

        print(self.choices)

        for i, option in enumerate(self.options):
            self.buttons_choice_end_of_turn[i].config(state=NORMAL) if self.choices[option] else self.buttons_choice_end_of_turn[i].config(state=DISABLED)


    def init_user_interface(self):
        
        self.frame_header.pack(pad_y="20")
        self.label_score.pack()
        self.label_turn.pack()

        self.frame_dices.pack()
        for i in range(5):self.dice_labels[i].pack(side=LEFT)

        self.button_throw_dices.pack(pad_y=10)

        self.init_dices_for_new_turn()

        self.frame_buttons_end_of_turn.pack()
        self.frame_buttons_end_of_turn_left.pack(side=LEFT)
        self.frame_buttons_end_of_turn_right.pack(side=RIGHT)


        for button in self.buttons_choice_end_of_turn:
            button.pack(pad_x=2, pad_y=1)

    def init_dices_for_new_turn(self):
        print("\n{}".format(self.turn.get()))
        for i in range(5):
            self.dice_values[i].set(0)
            self.dice_labels[i].config(fg="BLUE")
            self.button_throw_dices.config(state=NORMAL)
        self.throw_this_turn = 0
        self.dices_can_be_clicked = False
        self.dices_selected = [True] *5


root = Tk()
root.wm_title("Yams_Game")
root.resizable(width=False, height=False)
app = GameYams(root)
root.mainloop()