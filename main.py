import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from operator import itemgetter
from random import randint
import json

niveles = ("nivel1.json","nivel2.json","nivel3.json","nivel4.json","nivel5.json")

class game:
    def __init__(self):
        self.scores = score("Scores.json")
        self.root = tk.Tk()
        self.__configRoot()
        self.__configMenu()
        self.__configFramePrincipal()
        self.root.mainloop()

    def __configGame(self):
        self.round = 0
        self.scorePlayer = 0
        self.player = self.temp.get()
        self.__question()

    def __question(self):
        self.question =  question(niveles[self.round])
        self.questionRound = self.question.getQuestion()
        self.options = self.question.getOption()
        
    def __configRoot(self):
        self.root.title("Knowledge")
        self.root.iconbitmap("imagenes\\interrogacion.ico")
        self.root.config(background="blue")
        self.root.resizable(False, False) 
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

    def __configMenu(self):
        self.helpMenu = tk.Menu(self.menu, tearoff=0)
        self.helpMenu.add_command(label="Manual", command=self.__manual)
        self.helpMenu.add_command(label="License", command=self.__license)
        self.helpMenu.add_command(label="About of", command=self.__about)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)

    def __manual(self):
        messagebox.showinfo("Manual", "1. Enter your name in the main window.\n2. Press the play button.\n3. Answer the questions.")

    def __license(self):
        messagebox.showinfo("License", "GNU GENERAL PUBLIC LICENSE")

    def __about(self):
        messagebox.showinfo("Davito", "Design by: Davito(Omar Vargas Bonett)\ncontact:omardbonett@gmail.com\nreto tecnico sofka U")

    def __configFramePrincipal(self):
        self.framePrincipal = tk.Frame(self.root, width=480, height= 380)
        self.framePrincipal.grid(row=0, column=0)
        self.__widgetFramePrincipal()

    def __configFrameScores(self):
        self.frameScores = tk.Frame(self.root, width=480, height= 380)
        self.frameScores.grid(row=0, column=0)
        self.__widgetFrameScores()

    def __configFrameGame(self):
        self.__configGame()
        self.frameGame = tk.Frame(self.root,  width=480, height= 380)
        self.frameGame.grid(row=0, column=0)
        self.__widgetFrameGame()  

    def __widgetFrameGame(self):
        self.__labelPlayer()
        self.__labelQuestion()
        self.__buttonResponse()

    def __labelPlayer(self):
        self.labelPlayer = tk.Label(self.frameGame, text=self.player + " - round" + str(self.round+1), font=('comic sans MS', -20))
        self.labelPlayer.place(x=20, y=30)

    def __labelQuestion(self):
        self.labelQuestion = tk.Label(self.frameGame, text=self.questionRound, font=('comic sans MS', -20))
        self.labelQuestion.place(x=20, y=80)

    def __buttonResponse(self):
        self.buttonResponse1 = tk.Button(self.frameGame, text=self.options[0], font=('comic sans MS', -20), command=lambda:self.__response(self.options[0]))
        self.buttonResponse1.place(x=20, y= 150)
        self.buttonResponse2 = tk.Button(self.frameGame, text=self.options[1], font=('comic sans MS', -20), command=lambda:self.__response(self.options[1]))
        self.buttonResponse2.place(x=20, y= 220)
        self.buttonResponse3 = tk.Button(self.frameGame, text=self.options[2], font=('comic sans MS', -20), command=lambda:self.__response(self.options[2])) 
        self.buttonResponse3.place(x=180, y= 150)
        self.buttonResponse4 = tk.Button(self.frameGame, text=self.options[3], font=('comic sans MS', -20), command=lambda:self.__response(self.options[3])) 
        self.buttonResponse4.place(x=180, y= 220)

    def __response(self, response):
        if response == self.question.getCorrectOption(): self.__nextRound()
        else: self.__loser()

    def __loser(self):
        self.scores.addScore(self.player, self.scorePlayer)
        messagebox.showinfo("Loser", "your score is "+ str(self.scorePlayer)+"\nnice try")
        self.scores.writeScore()
        self.frameGame.destroy()

    def __winner(self):
        self.scorePlayer += 1000000
        messagebox.showinfo("Winner!!!!!", "your score is "+ str(self.scorePlayer))
        self.scores.addScore(self.player, self.scorePlayer)
        self.scores.writeScore()
        self.frameGame.destroy()

    def __nextRound(self):
        self.round+=1
        if self.round<5:
            self.scorePlayer += 10**self.round
            self.__question()
            self.__updateLabelsGame()     
        else:
            self.__winner()
    
    def __updateLabelsGame(self):
        self.labelPlayer.config(text=self.player + " - round" + str(self.round+1))
        self.labelQuestion.config(text=self.questionRound)
        self.buttonResponse1.config(text=self.options[0])
        self.buttonResponse2.config(text=self.options[1])
        self.buttonResponse3.config(text=self.options[2])
        self.buttonResponse4.config(text=self.options[3])       

    def __widgetFrameScores(self):
        self.__labelScore()
        self.__printScore()
        self.__buttonBackScore()

    def __labelScore(self):
        self.imageIntro = ImageTk.PhotoImage(Image.open("imagenes\\intro.png").resize((300, 100)))
        self.labelIntro = tk.Label(self.frameScores, image=self.imageIntro)
        self.labelIntro.place(x=100, y=20)
        self.imagenScoresframe = tk.PhotoImage(file="imagenes\\scores.png")
        self.labelScores = tk.Label(self.frameScores, image=self.imagenScoresframe).place(x=50, y=120)

    def __printScore(self):
        scores = self.scores.getScores()
        for i in range(0, len(scores) if len(scores)<=10 else 10):
            tk.Label(self.frameScores, text=str(i+1)+". "+scores[i][0]+"--------->"+str(scores[i][1]), font=('comic sans MS', -15)).place(x=50, y=180+20*i)

    def __buttonBackScore(self):
        self.imagePlay = tk.PhotoImage(file="imagenes\\back.png")
        self.buttonPlay = tk.Button(self.frameScores, text = 'Play!', image=self.imagePlay, relief="flat", command=self.__configFramePrincipal)
        self.buttonPlay.place(x=310, y=240)

    def __widgetFramePrincipal(self):
        self.__introLabel()
        self.__buttonPlay()
        self.__buttonScore()
        self.__buttonExit()
        self.__labelDesign()
        self.__entryPlayerName()

    def __introLabel(self):
        self.imageIntro = ImageTk.PhotoImage(Image.open("imagenes\\intro.png").resize((300, 100)))
        self.labelIntro = tk.Label(self.framePrincipal, image=self.imageIntro)
        self.labelIntro.place(x=100, y=0)

    def __buttonPlay(self):
        self.imagePlay = tk.PhotoImage(file="imagenes\\play.png")
        self.buttonPlay = tk.Button(self.framePrincipal, text = 'Play!', image=self.imagePlay, relief="flat", command=self.__configFrameGame)
        self.buttonPlay.place(x=180, y=180)

    def __buttonScore(self):
        self.imageScore = tk.PhotoImage(file="imagenes\\Score.png")
        self.buttonScore = tk.Button(self.framePrincipal, text="Score!", image=self.imageScore, relief="flat", command=self.__configFrameScores)
        self.buttonScore.place(x=180, y=240)

    def __buttonExit(self):
        self.imageExit = tk.PhotoImage(file="imagenes\\exit.png")
        self.buttonExit =  tk.Button(self.framePrincipal, text="Exit!", image=self.imageExit, relief="flat", command=exit)
        self.buttonExit.place(x=180, y=300)

    def __entryPlayerName(self):
        tk.Label(self.framePrincipal, text="ingresa tu nombre",  font=('comic sans MS', -20), fg="orange").place(x=160, y = 100)
        self.temp = tk.StringVar(value="ia") 
        tk.Entry(self.framePrincipal, textvariable=self.temp, font=('comic sans MS', -20), fg="orange").place(x=120, y= 130)

    def __labelDesign(self):
        self.labelDesign = tk.Label(self.framePrincipal, text="desing by: Davito", width=50 ,font=('comic sans MS', -10), fg="orange")
        self.labelDesign.place(x=280, y=360)

            
#--------------------------------------------------------------------------------------------------#

class question:
    def __init__(self, banco_preguntas):
        self.banco = banco_preguntas
        self.pregunta = None
        self.__takeAQuestion()

    def __takeAQuestion(self):
        preguntas = json.load(open(self.banco))
        index = randint(0,4)
        keys = list(preguntas)
        self.pregunta = (keys[index],preguntas[keys[index]])

    def getQuestionAnswer(self):
        return self.pregunta

    def getOption(self):
        return self.pregunta[1][1]

    def getCorrectOption(self):
        return self.pregunta[1][0]
    
    def getQuestion(self):
        return self.pregunta[0]

class score:
    def __init__(self, path : str):
        self.__path = path
        self.__Scores = json.load(open(path))

    def addScore(self, id, score):
        if id in self.__Scores:
            self.__Scores[id] = score if score>self.__Scores[id] else self.__Scores[id]
        else:
             self.__Scores[id] = score

    def writeScore(self):
        with open(self.__path, 'w') as file:
            json.dump(self.__Scores, file, indent=4)

    def getScores(self):
        score_sort = sorted(self.__Scores.items(), key=itemgetter(1), reverse=True)
        return score_sort

if __name__=='__main__':
    game()
