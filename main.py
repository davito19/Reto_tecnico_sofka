import tkinter as tk
from typing import Text
from PIL import Image, ImageTk
from operator import itemgetter
from random import randint
import json

class game:
    def __init__(self):
        self.scores = score("Scores.json")
        self.player = "IA"
        self.question =  question("nivel1.json")
        self.root = tk.Tk()
        self.__configRoot()
        self.__configMenu()
        self.__configFramePrincipal()
        #self.__configFrameScores()
        #self.__configFrameGame()
        self.root.mainloop()

    def __configRoot(self):
        self.root.title("Knowledge")
        self.root.iconbitmap("imagenes\\interrogacion.ico")
        self.root.config(background="blue")
        self.root.resizable(False, False) 
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

    def __configMenu(self):
        self.helpMenu = tk.Menu(self.menu, tearoff=0)
        self.helpMenu.add_command(label="Manual")
        self.helpMenu.add_command(label="License")
        self.helpMenu.add_command(label="About of")
        self.menu.add_cascade(label="Help", menu=self.helpMenu)

    def __configFramePrincipal(self):
        self.framePrincipal = tk.Frame(self.root, width=480, height= 380)
        self.framePrincipal.grid(row=0, column=0)
        self.__widgetFramePrincipal()

    def __configFrameScores(self):
        self.frameScores = tk.Frame(self.root, width=480, height= 380)
        self.frameScores.grid(row=0, column=0)
        self.__widgetFrameScores()

    def __configFrameGame(self):
        self.frameGame = tk.Frame(self.root,  width=480, height= 380)
        self.frameGame.grid(row=0, column=0)
        self.__widgetFrameGame()  

    def __widgetFrameGame(self):
        self.__labelPlayer()
        self.__labelQuestion()
        self.__buttonResponse()

    def __labelPlayer(self):
        self.labelPlayer = tk.Label(self.frameGame, text=self.player, font=('comic sans MS', -20)).place(x=20, y=30)

    def __labelQuestion(self):
        self.labelQuestion = tk.Label(self.frameGame, text="1. hola como tas?", font=('comic sans MS', -20)).place(x=20, y=80)

    def __buttonResponse(self):
        self.buttonResponse1 = tk.Button(self.frameGame, text="opcion A", font=('comic sans MS', -20)).place(x=20, y= 150)
        self.buttonResponse2 = tk.Button(self.frameGame, text="opcion B", font=('comic sans MS', -20)).place(x=20, y= 220)
        self.buttonResponse3 = tk.Button(self.frameGame, text="opcion C", font=('comic sans MS', -20)).place(x=120, y= 150)
        self.buttonResponse4 = tk.Button(self.frameGame, text="opcion D", font=('comic sans MS', -20)).place(x=120, y= 220)



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

    def __introLabel(self):
        self.imageIntro = ImageTk.PhotoImage(Image.open("imagenes\\intro.png").resize((300, 100)))
        self.labelIntro = tk.Label(self.framePrincipal, image=self.imageIntro)
        self.labelIntro.place(x=100, y=20)

    def __buttonPlay(self):
        self.imagePlay = tk.PhotoImage(file="imagenes\\play.png")
        self.buttonPlay = tk.Button(self.framePrincipal, text = 'Play!', image=self.imagePlay, relief="flat", command=self.__configFrameGame)
        self.buttonPlay.place(x=180, y=140)

    def __buttonScore(self):
        self.imageScore = tk.PhotoImage(file="imagenes\\Score.png")
        self.buttonScore = tk.Button(self.framePrincipal, text="Score!", image=self.imageScore, relief="flat", command=self.__configFrameScores)
        self.buttonScore.place(x=180, y=200)

    def __buttonExit(self):
        self.imageExit = tk.PhotoImage(file="imagenes\\exit.png")
        self.buttonExit =  tk.Button(self.framePrincipal, text="Exit!", image=self.imageExit, relief="flat", command=exit)
        self.buttonExit.place(x=180, y=260)

    def __labelDesign(self):
        self.labelDesign = tk.Label(self.framePrincipal, text="desing by: Davito", font=('comic sans MS', -10), fg="orange")
        self.labelDesign.place(x=395, y=360)

            
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

class player():
    def __init__(self):
        root=tk.Tk()
        self.name=tk.StringVar()
        tk.Label(root, text='enter your name').pack()
        tk.Entry(root, textvariable=self.name).pack()
        tk.Button(root, text='Enter', command=root.destroy).pack()
        root.mainloop()

    def getName(self):
        return self.name.get()
    
class score:
    def __init__(self, path : str):
        self.__path = path
        self.__Scores = json.load(open(path))

    # def getPlayers(self):
    #     return list(self.__Scores)

    # def getScoresOnly(self):
    #     return list(self.__Scores.values())

    def addScore(self, id, score):
        self.__Scores[id] = score

    def writeScore(self):
        with open(self.__path, 'w') as file:
            json.dump(self.__Scores, file, indent=4)

    def getScores(self):
        score_sort = sorted(self.__Scores.items(), key=itemgetter(1), reverse=True)
        return score_sort



if __name__=='__main__':
    game()
    #print(player().getName())
    # b = question("noobcategory.json")
    # print(b.getQuestionAnswer())
    # print(b.getQuestion())
    # print(b.getOption())
    # print(b.getCorrectOption())