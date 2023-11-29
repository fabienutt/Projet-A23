import tkinter as tk
from tkinter import messagebox
import csv
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enregistreur de données")
        self.init_ui()
        self.create_csv_file_if_not_exists()

    def init_ui(self):
        # Initialiser l'interface utilisateur
        self.init_text_input()
        self.init_choices()
        self.init_checkboxes()
        self.init_save_button()

    def init_text_input(self):
        # Initialisation de la zone de texte
        self.label_text = tk.Label(self, text="Saisissez votre texte:")
        self.label_text.pack(pady=10)
        self.text_input = tk.Text(self, height=5, width=50)
        self.text_input.pack(pady=10)

    def init_choices(self):
        # Initialisation des choix
        self.choices = [
            "Moteur", "Servomoteur", "Gripper", "LED", "Verin"
        ]

    def init_checkboxes(self):
        # Initialisation des checkboxes
        self.check_vars = []
        for choice in self.choices:
            check_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self, text=choice, variable=check_var)
            checkbox.pack(anchor='w')
            self.check_vars.append(check_var)

    def init_save_button(self):
        # Initialisation du bouton Enregistrer
        self.save_btn = tk.Button(self, text="Enregistrer", command=self.save_data)
        self.save_btn.pack(pady=20)

    def create_csv_file_if_not_exists(self):
        # Création du fichier CSV s'il n'existe pas
        if not os.path.exists('data.csv'):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Texte', *self.choices])

    def save_data(self):
        # Sauvegarder les données dans le fichier CSV
        try:
            text_data = self.text_input.get("1.0", 'end-1c')
            choices_data = [int(var.get()) for var in self.check_vars]
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([text_data, *choices_data])
            self.reset_ui()
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")

    def reset_ui(self):
        # Réinitialiser l'interface utilisateur
        self.text_input.delete("1.0", tk.END)
        for check_var in self.check_vars:
            check_var.set(False)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
