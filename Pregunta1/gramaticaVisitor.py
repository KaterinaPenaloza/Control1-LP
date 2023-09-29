# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta1\\gramatica.g4 by ANTLR 4.9.2
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
        turtle.showturtle()
        turtle.shape("turtle")
        turtle.down()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        turtle.up()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        move = int(ctx.NUMBER().getText())
        turtle.forward(move)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    # esta funcion permite obtener el angulo y distancia que debe dibujar la tortuga
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        angle = int(ctx.NUMBER(0).getText())
        move = int(ctx.NUMBER(1).getText())
        turtle.right(angle)
        turtle.forward(move)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done() # termina la ejecucion
        return self.visitChildren(ctx)



del gramaticaParser