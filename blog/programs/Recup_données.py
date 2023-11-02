import tkinter as tk
from tkinter import messagebox
import json
import os

class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Enregistreur de données")

        # Créer le fichier data.json s'il n'existe pas
        if not os.path.exists('data.json'):
            with open('data.json', 'w') as file:
                file.write("")

        # Zone de texte
        self.label_text = tk.Label(self, text="Saisissez votre texte:")
        self.label_text.pack(pady=10)

        self.text_input = tk.Text(self, height=5, width=50)
        self.text_input.pack(pady=10)

        # Liste des choix
        self.choices = [
            "Caméra RGB (visualisation normale)",
            "Caméra Infrarouge (visualisation nocturne)",
            "Caméra thermique (visualisation chaleur)",
            "Caméra profondeur (visualisation normale + profondeur)",
            "Capteurs ultrasons (detection distance peu précis)",
            "LED (éclairage pour environnement sombre)",
            "Laser télémètre (mesure distance précise)"
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
        data = {
            'text': self.text_input.get("1.0", 'end-1c'),  # Récupérer le texte
            'choices': [choice for var, choice in zip(self.check_vars, self.choices) if var.get()]  # Récupérer les choix cochés
        }

        # Sauvegarder les données en JSON
        try:
            with open('data.json', 'a') as file:
                json.dump(data, file)
                file.write('\n')  # Nouvelle ligne pour chaque entrée

            messagebox.showinfo("Succès", "Les données ont été sauvegardées avec succès!")
            
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
