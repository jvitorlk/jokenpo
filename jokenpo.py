import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def pedra():
    jokenpo('Pedra')

def papel():
    jokenpo('Papel')
    
def tesoura():
    jokenpo('Tesoura')

def jokenpo(player):
    computer = random.choice(['Pedra', 'Papel', 'Tesoura'])
    
    if player == computer:
        message = f'''
            Jogador: {player.upper()}
            Computador: {computer.upper()}
            
            Resultado: EMPATE!
        '''
    elif (player == 'Pedra' and computer == 'Tesoura') or \
        (player == 'Papel' and computer == 'Pedra') or \
        (player == 'Tesoura' and computer == 'Papel'):
        message = f'''
            Jogador: {player.upper()}
            Computador: {computer.upper()}
            
            Resultado: JOGADOR GANHOU!
        '''
    else:
        message = f'''
            Jogador: {player.upper()}
            Computador: {computer.upper()}
            
            Resultado: COMPUTADOR GANHOU!
        '''
        
    result.config(text=message)

window = tk.Tk()

frame = LabelFrame(window, text='Qual é a sua jogada?', padx=10, pady=10)
frame.pack()

iconePedra = PhotoImage(file='images/pedra.png')
iconePapel = PhotoImage(file='images/papel.png')
iconeTesoura = PhotoImage(file='images/tesoura.png')

Button(frame, text=' Pedra', command=pedra, image=iconePedra, compound=tk.LEFT).grid(column=0, row=1)
Button(frame, text='Papel', command=papel, image=iconePapel, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Tesoura', command=tesoura, image=iconeTesoura, compound=tk.LEFT).grid(column=2, row=1)

result = Label(frame, pady=10, padx=10, justify=tk.LEFT)
result.grid(column=0,row=2, columnspan=3)


window.title('Pedra, Papel e Tesoura')
window.geometry('500x200+500+200')
window.mainloop()