from tkinter import *
from tkinter import ttk, messagebox
import string
import random

# Cores Predefinidas
cor_preta = "#444466"
cor_branca = "#feffff"
cor_vermelha = "#f05a43"

# Configuração da janela
janela = Tk()
janela.title('Password Generator')
janela.geometry('295x360')
janela.configure(bg=cor_branca)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Frames
frame_cima = Frame(janela, width=295, height=40, bg=cor_branca, relief="flat")
frame_cima.grid(row=0, column=0, sticky="NSEW")

frame_baixo = Frame(janela, width=295, height=310, bg=cor_branca, relief="flat")
frame_baixo.grid(row=1, column=0, sticky="NSEW")



# Título
app_nome = Label(frame_cima, text="Password Generator", font=("Ivy 16 bold"), bg=cor_branca, fg=cor_preta)
app_nome.place(x=2, y=0)



# Linha separadora
app_linha = Label(frame_cima, text="", width=295, height=1, bg=cor_vermelha)
app_linha.place(x=0, y=35)



# Label da senha gerada
app_senha = Label(frame_baixo, text="- - - -", width=21, height=2, relief="solid",
                  font=("Ivy 12 bold"), bg=cor_branca, fg=cor_preta)
app_senha.grid(row=0, column=0, columnspan=1, sticky="NSEW", padx=3, pady=10)



# Label "Total characters"
app_info = Label(frame_baixo, text="Total characters", font=("Ivy 10 bold"), bg=cor_branca, fg=cor_preta)
app_info.grid(row=1, column=0, columnspan=2, sticky="NSEW", padx=5, pady=1)




# Spinbox para definir o tamanho da senha
var = IntVar(value=8)
spin = Spinbox(frame_baixo, from_=1, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky="NW", padx=5, pady=8)




# Frame para os checkboxes
frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor_branca)
frame_caracteres.grid(row=3, column=0, sticky="NSEW", columnspan=3)




# Checkboxes e Labels
estado_check_upper = BooleanVar(value=True)
estado_check_lower = BooleanVar(value=True)
estado_check_numbers = BooleanVar(value=True)
estado_check_simbols = BooleanVar(value=True)




Checkbutton(frame_caracteres, text="ABC Uppercase", var=estado_check_upper, bg=cor_branca).grid(row=0, column=0, sticky="W")
Checkbutton(frame_caracteres, text="abc Lowercase", var=estado_check_lower, bg=cor_branca).grid(row=1, column=0, sticky="W")
Checkbutton(frame_caracteres, text="123 Numbers", var=estado_check_numbers, bg=cor_branca).grid(row=2, column=0, sticky="W")
Checkbutton(frame_caracteres, text="!@# Symbols", var=estado_check_simbols, bg=cor_branca).grid(row=3, column=0, sticky="W")



# Função para gerar senha
def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = "123456789"
    simbolos = "!@#$%&*+-=_-?"
    combinar = ""

    # Verificar quais checkboxes estão marcados
    if estado_check_upper.get():
        combinar += alfa_maior
    if estado_check_lower.get():
        combinar += alfa_menor
    if estado_check_numbers.get():
        combinar += numeros
    if estado_check_simbols.get():
        combinar += simbolos

    # Se nenhum checkbox estiver marcado, exibir alerta
    if not combinar:
        messagebox.showwarning("Erro", "Selecione pelo menos um tipo de caractere!")
        return

    # Definir comprimento da senha
    comprimento = int(spin.get())



    # Gerar a senha garantindo que o comprimento seja respeitado
    senha = "".join(random.choices(combinar, k=comprimento))



    # Atualizar a label com a senha gerada
    app_senha['text'] = senha

    # Botão para copiar senha
    def copiar_senha():
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo("Sucesso", "Senha copiada!")

    button_copiar = Button(frame_baixo, text="Copy", command=copiar_senha, width=7, height=2, relief="raised",
                            font=("Ivy 10 bold"), bg=cor_branca, fg=cor_preta)
    button_copiar.grid(row=0, column=1, sticky="NW", padx=5, pady=10, columnspan=1)

# Botão de gerar senha
button_generate = Button(frame_caracteres, text="Generate", command=criar_senha, width=34, height=1, relief="flat",
                         font=("Ivy 10 bold"), bg=cor_vermelha, fg=cor_branca)
button_generate.grid(row=5, column=0, sticky="NSEW", padx=5, pady=15, columnspan=5)

# Loop principal
janela.mainloop()
