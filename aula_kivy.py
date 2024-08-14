from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random

class lights_out(App):

    lenx = 10
    leny = 10
    dificuldade = 30

    def build(self):
        self.layout = GridLayout(cols=self.lenx)
        self.gerar_matriz()
        return self.layout
    

    def criar_botao(self,x,y):
        botao = Button()
        botao.bind(on_press=self.on_button_press)
        botao.valor = (x,y)
        botao.ativado = True
        botao.background_color = (0, 1, 0, 1)
        self.layout.add_widget(botao)
        return botao


    def lout(self,x,y):
        if y < len(self.matriz) and x < len(self.matriz[0]):
            self.switch(x+1,y)
            self.switch(x,y+1)
            self.switch(x,y)
            self.switch(x-1,y)
            self.switch(x,y-1)


    def switch(self,x,y):
        if y in range(len(self.matriz)) and x in range(len(self.matriz[0])):
            if self.matriz[y][x].ativado:
                self.matriz[y][x].background_color = (1, 0, 0, 1)
            else:
                self.matriz[y][x].background_color = (0, 1, 0, 1)
            
            self.matriz[y][x].ativado = not self.matriz[y][x].ativado


    def ativar_matriz(self):
        for i in range(self.dificuldade):
            self.lout(random.randint(0,self.lenx-1),random.randint(0,self.leny-1))
    

    def gerar_matriz(self):
        self.matriz = [[self.criar_botao(x,y) for x in range(self.lenx)] for y in range(self.leny)]
        self.ativar_matriz()
    

    def on_button_press(self, instance):
        x = instance.valor[0]
        y = instance.valor[1]
        self.lout(x,y)


lights_out().run()