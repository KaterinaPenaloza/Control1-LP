# Generated from c://Users//Kzwy//Desktop//Control1-LP//Pregunta4//gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
import turtle
from turtle import*

if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        turtle.showturtle()
        turtle.shape("turtle")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStat.
    def visitPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#blank.
    def visitBlank(self, ctx:gramaticaParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#On.
    def visitOn(self, ctx:gramaticaParser.OnContext):
        turtle.down()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        turtle.up()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot.
    def visitRot(self, ctx:gramaticaParser.RotContext):
        angle = int(ctx.NUMBER().getText())
        turtle.right(angle)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot2.
    def visitRot2(self, ctx:gramaticaParser.Rot2Context):
        angle = int(ctx.NUMBER(0).getText()) # obtiene el angulo de rotacion
        angle2 = int(ctx.NUMBER(1).getText()) # obtiene el segundo angulo de rotacion 
        cordenada = turtle.towards(angle,angle2) # calula el angulo hacia la coordenada indicada 
        turtle.setheading(cordenada)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Rot3.
    def visitRot3(self, ctx:gramaticaParser.Rot3Context):
        #variables utilizadas para la funcion Mov2
        move = int(ctx.NUMBER(0).getText())
        #variables utilizadas para la funcion Rot
        move1 = int(ctx.NUMBER(1).getText())
        #variables utilizadas para la funcion Rot
        angle = int(ctx.NUMBER(2).getText())
        #funcion para mover
        turtle.goto(move,move1)
        #funcion para rotar
        turtle.right(angle)
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        move = int(ctx.NUMBER().getText()) # obtiene la distancia 
        turtle.forward(move) # se mueve la distancia especificada
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        angle = int(ctx.NUMBER(0).getText()) 
        move = int(ctx.NUMBER(1).getText())
        turtle.goto(angle,move)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gramaticaParser#Rep.
    def visitRep(self, ctx:gramaticaParser.RepContext):
        num = int(ctx.NUMBER().getText())  # Obtener el número de repeticiones
        stat = ctx.stat()  # Obtener el bloque de código a repetir
        for _ in range(num):
            self.visit(stat)  # Visitar el bloque de código la cantidad especificada de veces
            print(_)

        return self.visitChildren(ctx)

    
    # Visit a parse tree produced by gramaticaParser#FR.
    # Es un delimitador para terminar el bucle, pero no ha funcionado
    # ya que si se pone algo luego no se hace el bucle.
    def visitFR(self, ctx:gramaticaParser.FRContext):
        print("Bucle finalizado")
        turtle.done()
        return None
    
    
    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done()
        return self.visitChildren(ctx)

del gramaticaParser