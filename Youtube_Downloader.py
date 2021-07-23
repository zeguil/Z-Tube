
from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
# layout
sg.theme('DarkBrown1')
layout = [
    [sg.Text('''ZTUBE''', font='Courier 19', pad=(230, 0))],
    [sg.Text('''\n''')],
    [sg.Text('''Baixe videos direto do Youtube colando o link do video ex: "https://www.youtube.com/video1..."
Depois digite o destino da pasta onde deve ser salvo o video ex: "C:\\Usuarios\Desktop\clipes" 
  ''')],
    [sg.Text("Link: ", font='Courier 12')],
    [sg.Input(key='link', size=(75, 1))],
    [sg.Text("Pasta:", font='Courier 12')],
    [sg.Input(key='diretorio', size=(75, 1))],
    [sg.Text()],
    [sg.Text('''Escolha o formato para download: 
    ''')],
    [sg.Checkbox('.mp4'), sg.Checkbox('.mp3')],
    [sg.Text('''\n''')],
    [sg.Button('Download', pad=(230, 0))],
    [sg.Text('''\n''')],
    [sg.Text('by leanz', font='Courier 9')]
]

# janela
titulo = "Youtube Downloader"
janela = sg.Window(titulo, layout, size=(580, 430), grab_anywhere=True)

# eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Download':
        yt = YouTube(valores['link'])
        path = valores['diretorio']
        ys = yt.streams.get_highest_resolution()
        ys.download(path)
    else:
        print("Link ou Diretorio invalidos")
        break
