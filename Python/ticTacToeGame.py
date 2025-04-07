import tkinter as tk
from tkinter import messagebox

# Variables globales
current_player = "X"  # Le joueur qui commence
score_x = 0
score_o = 0
board = [""] * 9  # La grille du jeu

# Fonction pour vérifier si un joueur a gagné
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
            return board[combination[0]]
    return None

# Fonction pour vérifier si la grille est pleine (match nul)
def check_draw():
    return "" not in board

# Fonction pour mettre à jour le score
def update_score(winner):
    global score_x, score_o
    if winner == "X":
        score_x += 1
    elif winner == "O":
        score_o += 1
    label_score.config(text=f"Score - X: {score_x} | O: {score_o}")

# Fonction de gestion du clic sur les boutons de la grille
def button_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        winner = check_winner()
        if winner:
            update_score(winner)
            messagebox.showinfo("Gagnant", f"Le joueur {winner} a gagné !")
            disable_buttons()
        elif check_draw():
            messagebox.showinfo("Match nul", "Le jeu est un match nul !")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"

# Fonction pour désactiver les boutons après la fin du jeu
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Fonction pour réinitialiser le jeu
def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for i in range(9):
        buttons[i].config(text="", state="normal")
    
# Fonction pour démarrer une nouvelle partie
def new_game():
    global current_player, board, score_x, score_o
    score_x, score_o = 0, 0
    update_score(None)  # Remettre à zéro le score
    reset_game()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu Tic-Tac-Toe")

# Zone de score
label_score = tk.Label(root, text=f"Score - X: {score_x} | O: {score_o}", font=("Arial", 14))
label_score.grid(row=0, column=0, columnspan=3)

# Grille de boutons pour le Tic-Tac-Toe
buttons = []
for i in range(9):
    button = tk.Button(root, text="", width=10, height=3, font=("Arial", 24), command=lambda i=i: button_click(i))
    button.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(button)

# Boutons de contrôle pour "New Game" et "Reset"
button_new_game = tk.Button(root, text="New Game", width=10, height=2, font=("Arial", 14), command=new_game)
button_new_game.grid(row=4, column=0)

button_reset = tk.Button(root, text="Reset", width=10, height=2, font=("Arial", 14), command=reset_game)
button_reset.grid(row=4, column=1)

# Lancement de l'application
root.mainloop()
