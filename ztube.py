# versão 2 com opção de download em formato mp4 ou mp3 (não finalizado)

from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
import moviepy.editor as mp
import re
import os

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
    [sg.Radio('.mp3', "RADIO1", default=False, key="-IN2-"),
     sg.Radio('.mp4', "RADIO1", default=True)],
    [sg.Text('''\n''')],
    [sg.Button('Download', pad=(130, 0)), sg.Button('Sair', size=(5, 1))],
    [sg.Text('''\n''')],
    [sg.Text('by leanz', font='Courier 9')]
]

# janela
titulo = "Ztube "
janela = sg.Window(titulo, layout, size=(580, 430), grab_anywhere=True)

# eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
        break
    elif eventos == 'Download':
        yt = YouTube(valores['link'])
        path = valores['diretorio']
        ys = yt.streams.get_highest_resolution()
        ys.download(path)
        if valores["-IN2-"] == True:
            for file in os.listdir(path):
                if re.search('mp4', file):

                    mp4_path = os.path.join(path, file)
                    mp3_path = os.path.join(
                        path, os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)

    else:
        print("Link ou Diretorio invalidos")
        break
