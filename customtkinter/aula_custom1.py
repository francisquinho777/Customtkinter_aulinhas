import customtkinter as ctk

janela = ctk.CTk() #cria a janela principal

janela._set_appearance_mode("dark")  # muda a cor da janela. se eu colocar cor system ele fica da cor que o sistema operacional estiver

btn = ctk.CTkButton(janela, text="Clique aqui") #cria um botão na janela
btn.pack(pady=50) #responsavel por mostra na tela o botão, e o pady é a distancia do botão para a borda da janela


janela.mainloop() #abre uma aba de interface grafica, é como se fosse o html

