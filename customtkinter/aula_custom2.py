import customtkinter as ctk

janela = ctk.CTk() #cria a janela principal

#configurando a janela principal 
janela._set_appearance_mode("system")  # muda a cor da janela. se eu colocar cor system ele fica da cor que o sistema operacional estiver

janela.title("Minha Janela") #define o titulo da janela
janela.geometry("900x500") #define o tamanho da janela
janela.maxsize(width=900, height=500) #limites max de abrir a janela
janela.minsize(width=500, height=300) #limite mim de fechar a jenala
janela.resizable(width=False, height=False)


janela.mainloop()
