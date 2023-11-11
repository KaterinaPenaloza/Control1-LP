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
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStat.
    def visitPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#blank.
    def visitBlank(self, ctx:gramaticaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#On.
    def visitOn(self, ctx:gramaticaParser.OnContext):
        turtle.showturtle() # hacer visible la tortuga 
        turtle.shape("turtle") # dar forma de tortuga
        turtle.down() # baja el lapiz para dibujar

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        turtle.up() # levanta el lapiz para no dibujar aunque se mueva

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot.
    def visitRot(self, ctx:gramaticaParser.RotContext):
        angle = int(ctx.NUMBER().getText()) # obtiene el angulo de rotacion
        turtle.right(angle) # gira a la derecha para el angulo especificado

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot2.
    def visitRot2(self, ctx:gramaticaParser.Rot2Context):
        angle = int(ctx.NUMBER(0).getText()) # obtiene el angulo de rotacion
        angle2 = int(ctx.NUMBER(1).getText()) # obtiene el segundo angulo de rotacion 
        #turtle.right(angle) # gira a la derecha para el angulo especificado 
        #turtle.right(angle2)
        cordenada = turtle.towards(angle,angle2) # calula el angulo hacia la coordenada indicada 
        turtle.setheading(cordenada) # orienta a la tortuga en esa direccion 

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        move = int(ctx.NUMBER().getText()) # obtiene la distancia 
        turtle.forward(move) # se mueve la distancia especificada

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    # esta funcion permite obtener el angulo y distancia que debe dibujar la tortuga
    # al usar goto se mueve a la coordenada indicada 
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        angle = int(ctx.NUMBER(0).getText()) 
        move = int(ctx.NUMBER(1).getText())
        #turtle.right(angle)
        #turtle.forward(move)
        turtle.goto(angle,move)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    #Termina la ejecución utilizando la funcion turtle.done()
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done() # termina la ejecucion
        return self.visitChildren(ctx)




del gramaticaParser