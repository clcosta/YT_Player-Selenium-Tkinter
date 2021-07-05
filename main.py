import tkinter as tk
from funcoes import *

# Instanciando a Classe

app = AppYt()


# Funções para interativas com a Interce 


def buscar1():
    if musica.get():
        app.iniciar_videos(musica.get())
    else:
        return

def buscar2():
    if musicas.get("1.0","end"):
        label_aviso['text'] = 'Rodando....'
        texto = musicas.get("1.0","end").split('\n')
        texto.remove("")
        app.iniciar_vario_videos(texto)
        label_aviso['text'] = 'Finalizado'
    else:
        label_aviso['text'] = "Digite alguma coisa!"
    return

def pausar():
    app.PausePlay()
    botao_pause_play['text'] = app.textopause
    botao_pause_play.config(bg = app.corplaypause)

### Criando Interface

root = tk.Tk()
root.configure(bg='#FFD4DB')
root.title('Pesquisar musicas no youtube')


############ | DIGITE UMA UNICA MUSICA | ##########

root.columnconfigure([0,1,2,3], weight=1)
root.rowconfigure([0,1,2,3,4,5,6,7], weight=1)

label_titulo1 = tk.Label(text='Buscar uma musica', relief='solid', borderwidth=1, fg='black', bg='#D3B5E5')
label_titulo1.grid(row=0, column=0, padx=20, pady=25, sticky='nswe', columnspan=4)

label_musica = tk.Label(text='Digite sua musica', bg='#FFD4DB', anchor='w')
label_musica.grid(row=1, column=0, padx=20, pady=5, sticky='nswe')

musica = tk.Entry(bd=3)
musica.grid(row=2, column=0, padx=20, columnspan=4, pady=10, sticky='nswe')

botao_buscar1 = tk.Button(text='Buscar', fg='white', bg='red', bd=3 , command=buscar1)
botao_buscar1.grid(row=3, column=3, padx=15, pady=10, sticky='nswe')

botao_proxima= tk.Button(text="Proxima", fg='white', bg='red', bd=3 , command=app.Proxima)
botao_proxima.grid(row=3, column=1, padx=15, pady=10, sticky='nswe')

botao_pause_play = tk.Button(text=app.textopause, fg='white', bg=app.corplaypause, bd=3 , command=pausar)
botao_pause_play.grid(row=3, column=2, padx=15, pady=10, sticky='nswe')

####### | DIGITE MAIS DE UMA UNICA MUSICA | ##########

label_titulo2 = tk.Label(text='Buscar mais de uma musica', relief='solid', borderwidth=1, fg='black', bg='#D3B5E5')
label_titulo2.grid(row=4, column=0, padx=20, pady=10, sticky='nswe', columnspan=4)

label_musica = tk.Label(text='Digite suas musicas (separe cada busca por uma linha)', bg='#FFD4DB', anchor='w')
label_musica.grid(row=5, column=0, padx=20, pady=5, sticky='nswe')

musicas = tk.Text(width=10, height=5, bd=3)
musicas.grid(row=6, column=0, padx=20, columnspan=4, pady=10, sticky='nswe')

label_aviso = tk.Label(text='', bg='#FFD4DB', anchor='w')
label_aviso.grid(row=7, column=0,columnspan=2, padx=20, pady=5, sticky='nswe')

botao_buscar2 = tk.Button(text='Buscar', fg='white', bg='red', bd=3, command=buscar2)
botao_buscar2.grid(row=7, column=3, padx=20, pady=10, sticky='nswe')

botao_cancelar = tk.Button(text='Fechar APP', fg='white', bg='red', command=root.quit, bd=3)
botao_cancelar.grid(row=7, column=2, padx=20, pady=10, sticky='nswe')

root.mainloop()