import random
import tkinter as tk


class NumberGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adivinhe o número!")

        self.guess_label = tk.Label(
            self.root, text="Digite um número entre 1 e 100:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.hint_label = tk.Label(self.root, text="")
        self.hint_label.pack()

        self.score_label = tk.Label(self.root, text="Pontuação: 10")
        self.score_label.pack()

        self.submit_button = tk.Button(
            self.root, text="Enviar palpite", command=self.check_guess)
        self.submit_button.pack()

        self.play_again_button = tk.Button(
            self.root, text="Jogar novamente", state=tk.DISABLED, command=self.new_game)
        self.play_again_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.new_game()

    def run(self):
        self.root.mainloop()

    def new_game(self):
        self.number = random.randint(1, 100)
        self.score = 10
        self.hint_label.config(text="")
        self.score_label.config(text="Pontuação: {}".format(self.score))
        self.submit_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.result_label.config(text="")

    def check_guess(self):
        guess = self.guess_entry.get()

        if not guess.isdigit():
            self.result_label.config(
                text="Por favor, insira um número válido.")
            return

        guess = int(guess)

        if guess < 1 or guess > 100:
            self.result_label.config(
                text="Por favor, insira um número entre 1 e 100.")
            return

        if guess == self.number:
            self.result_label.config(text="Você acertou!")
            self.submit_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)
        elif guess < self.number:
            self.result_label.config(text="Tente um número maior.")
            self.hint_label.config(
                text="Dica: o número é ímpar." if self.number % 2 else "Dica: o número é par.")
            self.score -= 1
            self.score_label.config(text="Pontuação: {}".format(self.score))
        else:
            self.result_label.config(text="Tente um número menor.")
            self.hint_label.config(
                text="Dica: o número é ímpar." if self.number % 2 else "Dica: o número é par.")
            self.score -= 1
            self.score_label.config(text="Pontuação: {}".format(self.score))

        if self.score == 0:
            self.result_label.config(
                text="Sua pontuação chegou a zero. O número era {}.".format(self.number))
            self.submit_button.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)


game = NumberGuessingGame()
game.run()
