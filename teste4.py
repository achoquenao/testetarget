import tkinter as tk
from tkinter import ttk

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

def criar_interface():
    root = tk.Tk()
    root.title("Percentual de Faturamento por Estado")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

    tree = ttk.Treeview(root, columns=("Estado", "Percentual"), show="headings")
    tree.heading("Estado", text="Estado")
    tree.heading("Percentual", text="Percentual (%)")

    for estado, percentual in percentuais.items():
        tree.insert("", "end", values=(estado, f"{percentual:.2f}"))

    tree.pack(fill="both", expand=True)

    root.mainloop()

criar_interface()
