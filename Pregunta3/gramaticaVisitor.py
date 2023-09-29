# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta2\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
import turtle
from turtle import*

if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    #El inicio del programa
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStat.
    def visitPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#blank.
    #Si el input está en blanco no hace nada
    def visitBlank(self, ctx:gramaticaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#On.
    #Inicializa el puntero en forma de tortuga y "pone abajo el lapiz" para dibujar
    def visitOn(self, ctx:gramaticaParser.OnContext):
        turtle.showturtle()
        turtle.shape("turtle")
        turtle.down()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    #"Levanta el lapiz", de ese modo no dibuja.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        turtle.up()
        #turtle.done()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot.
    # Rota el puntero a un cierto angulo dado por el usuario con la funcion turtle.right()
    # esto es en sentido horario (turtle.right)
    def visitRot(self, ctx:gramaticaParser.RotContext):
        angle = int(ctx.NUMBER().getText())
        turtle.right(angle)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot2.
    # Rota el puntero a una coordenada dada.
    def visitRot2(self, ctx:gramaticaParser.Rot2Context):
        angle = int(ctx.NUMBER(0).getText()) # obtiene el angulo de rotacion
        angle2 = int(ctx.NUMBER(1).getText()) # obtiene el segundo angulo de rotacion 
        turtle.right(angle) # gira a la derecha para el angulo especificado 
        turtle.right(angle2)  

        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by gramaticaParser#Rot3.
    # Se utiliza la base de la funcion mov2 que modifica la orientación del puntero y lo mueve hasta un punto dado
    # por el usuario, luego cambia su orientacion como en la funcion Rot
    def visitRot3(self, ctx:gramaticaParser.Rot2Context):
        #variables utilizadas para la funcion Mov2
        move = int(ctx.NUMBER(0).getText())
        move1 = int(ctx.NUMBER(1).getText())
        #variables utilizadas para la funcion Rot
        angle = int(ctx.NUMBER(2).getText())
        #funcion para mover
        turtle.goto(move,move1)
        #funcion para rotar
        turtle.right(angle)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    # El puntero se desplaza un numero dado por el usuario con la funcion turtle.forward()
    def visitMov(self, ctx:gramaticaParser.MovContext):
        move = int(ctx.NUMBER().getText())
        turtle.forward(move)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    # El puntero se cambia orientación en dirección al punto y luego
    # se desplaza hasta el punto indicado por el usuario
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        angle = int(ctx.NUMBER(0).getText())
        move = int(ctx.NUMBER(1).getText())
        turtle.right(angle)
        turtle.forward(move)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    #Termina la ejecución utilizando la funcion turtle.done()
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done()
        return self.visitChildren(ctx)



del gramaticaParser