from tkinter import *
import random

#intialize window
from tkinter import *
import random

root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Jos - Rock, Paper, Scissors')
root.config(bg= 'seashell3')

Label(root,text = 'Rock, Paper Scissors Game', font = 'arial 20 bold', bg = 'seashell2').pack()

user_take = StringVar()

Label(root, text = 'Choose any one: Rock, Paper, Scissors',
font = 'arial 14 bold', bg ='seashell2').place(x=20, y = 70)

Entry(root, font = 'arial 15', textvariable = user_take,bg = 'antiquewhite3').place(x = 90, y = 130)


# computer choice

ComputerChoice = random.randint(1,3)
if ComputerChoice == 1:
    ComputerChoice = 'Rock'
elif ComputerChoice == 2:
    ComputerChoice = 'Paper'
else:
    ComputerChoice= 'Scissors'

Result = StringVar()

def Play():

    user_Pick = user_take.get().title()

    if user_Pick == ComputerChoice:
        Result.set('Tie, You Both Selected Same')
    elif user_Pick == 'Rock':
        if ComputerChoice == 'Paper':
            Result.set('You LOOSE, Computer Select Paper')
        else:
            Result.set('You WIN, Computer Select Scissor')
    elif user_Pick == 'Paper':
        if ComputerChoice == 'Scissor':
            Result.set('You LOOSE, Computer Select Scissor')
        else:
            Result.set('You WIN, Computer Select Rock')
    elif user_Pick == 'Scissor':
        if ComputerChoice == 'Paper':
            Result.set('You LOOSE, Computer Select Rock')
        else:
            Result.set('You WIN, Computer Select Paper')
    else:
        Result.set('Invalid: Choose any one -- Rock, Paper, Scissor')
        
    
def Reset():
    Result.set('')
    user_take.set('')

def Exit():
    root.destroy()

    

Entry(root, font = 'arial 10 bold', textvariable = Result,bg ='antiquewhite2', width = 50).place(x=25, y =250)

Button(root, font = 'arial 10 bold', text = 'PLAY', padx = 5,bg = 'seashell4', command = Play).place(x=150, y =190)

Button(root, font = 'arial 10 bold', text = 'RESET', padx = 5,bg = 'seashell4', command = Reset).place(x=70, y =310)

Button(root, font = 'arial 10 bold', text = 'EXIT', padx = 5,bg = 'seashell4', command = Exit).place(x=230, y =310)

root.mainloop()

           

    
        
    
