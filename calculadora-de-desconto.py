import tkinter as tk
from tkinter import messagebox

produtos = []
descontos_totais = []

def adicionar_produto():
    try:
        preco_original = float(entry_preco_original.get())
        preco_com_desconto = float(entry_preco_com_desconto.get()) if entry_preco_com_desconto.get() else None
        descontos_percentuais = [float(x) for x in entry_descontos_percentuais.get().split(',') if x]
        descontos_fixos = [float(x) for x in entry_descontos_fixos.get().split(',') if x]
        cashback = float(entry_cashback.get()) if entry_cashback.get() else 0
        
        if preco_com_desconto:
            desconto_total = preco_original - preco_com_desconto
            preco_final = preco_com_desconto
        else:
            preco_com_descontos = preco_original
            
            for desconto in descontos_percentuais:
                preco_com_descontos -= (preco_com_descontos * (desconto / 100))
            
            for desconto in descontos_fixos:
                preco_com_descontos -= desconto
            
            preco_com_descontos -= cashback
            
            preco_final = max(preco_com_descontos, 0)
            desconto_total = preco_original - preco_final
        
        produtos.append(preco_final)
        descontos_totais.append(desconto_total)
        
        lista_produtos.insert(tk.END, f'Produto {len(produtos)}: R$ {preco_final:.2f} (Desconto: R$ {desconto_total:.2f})')
        limpar_campos()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_total():
    total_compra = sum(produtos)
    total_descontos = sum(descontos_totais)
    resultado_label.config(text=f'Total da Compra: R$ {total_compra:.2f}\nTotal de Descontos: R$ {total_descontos:.2f}')

def limpar_campos():
    entry_preco_original.delete(0, tk.END)
    entry_preco_com_desconto.delete(0, tk.END)
    entry_descontos_percentuais.delete(0, tk.END)
    entry_descontos_fixos.delete(0, tk.END)
    entry_cashback.delete(0, tk.END)
    lista_produtos.delete(0, tk.END)
    resultado_label.config(text="Total da Compra:\nTotal de Descontos:")

root = tk.Tk()
root.title("Calculadora de Descontos")
root.configure(bg='black')
root.geometry("400x600")

# estilo = {
#     "bg": "#222",
#     "fg": "#fff",
#     "font": ("Arial", 12, "bold"),
#     "relief": "ridge",
#     "bd": 5,
#     "highlightbackground": "#444"
# }

campos = [
    ("Preço Original:", "entry_preco_original"),
    ("Preço com Desconto:", "entry_preco_com_desconto"),
    ("Descontos Percentuais:", "entry_descontos_percentuais"),
    ("Descontos Fixos:", "entry_descontos_fixos"),
    ("Cashback:", "entry_cashback")
]

for i, (label_text, entry_var) in enumerate(campos):
    tk.Label(root, text=label_text).grid(row=i, column=0, pady=5, padx=10, sticky="w")
    globals()[entry_var] = tk.Entry(root)
    globals()[entry_var].grid(row=i, column=1, pady=5, padx=10)

tk.Button(root, text="Adicionar Produto", command=adicionar_produto).grid(row=5, column=0, columnspan=2, pady=10)
lista_produtos = tk.Listbox(root, height=10)
lista_produtos.grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(root, text="Calcular Total", command=calcular_total).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(root, text="Limpar Tudo", command=limpar_campos).grid(row=8, column=0, columnspan=2, pady=10)
resultado_label = tk.Label(root, text="Total da Compra:\nTotal de Descontos:")
resultado_label.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()