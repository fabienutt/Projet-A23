import tkinter as tk
from tkinter import messagebox
import csv
import os

class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Enregistreur de données")

        # Créer le fichier data.csv s'il n'existe pas
        if not os.path.exists('data.csv'):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Écrire l'en-tête du fichier CSV
                writer.writerow(['Texte', *self.choices])

        # Zone de texte
        self.label_text = tk.Label(self, text="Saisissez votre texte:")
        self.label_text.pack(pady=10)

        self.text_input = tk.Text(self, height=5, width=50)
        self.text_input.pack(pady=10)

        # Liste des choix
        self.choices = [
            "Pince",
            "Verin",
            "Haut_parleur",
            "Pompe",
            "Ecran",
            "Electroaimant",
            "Tapis_roulant"
        ]

        # Checkboxes
        self.check_vars = []
        for choice in self.choices:
            check_var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self, text=choice, variable=check_var)
            checkbox.pack(anchor='w')
            self.check_vars.append(check_var)

        # Bouton Enregistrer
        self.save_btn = tk.Button(self, text="Enregistrer", command=self.save_data)
        self.save_btn.pack(pady=20)

    def save_data(self):
        text_data = self.text_input.get("1.0", 'end-1c')  # Récupérer le texte
        choices_data = [1 if var.get() else 0 for var in self.check_vars]  # Récupérer les choix sous forme 1 ou 0

        # Sauvegarder les données en CSV
        try:
            with open('C:/Users/FireF/OneDrive/Documents/GitHub/Projet-A23/blog/programs/datas/data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([text_data, *choices_data])

            
            # Effacer le contenu de la zone de texte
            self.text_input.delete("1.0", tk.END)

            # Décocher toutes les checkboxes
            for check_var in self.check_vars:
                check_var.set(False)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()