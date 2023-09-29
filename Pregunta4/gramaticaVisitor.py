# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta4\\gramatica.g4 by ANTLR 4.9.2
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
        turtle.right(angle) # gira a la derecha para el angulo especificado 
        turtle.right(angle2)  

        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by gramaticaParser#Rot2.
    def visitRot3(self, ctx:gramaticaParser.Rot2Context):
        move = int(ctx.NUMBER(0).getText())
        move1 = int(ctx.NUMBER(1).getText())
        angle = int(ctx.NUMBER(2).getText())
        
        turtle.goto(move,move1)
        turtle.right(angle)


        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        move = int(ctx.NUMBER().getText())
        turtle.forward(move)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mov2.
    def visitMov2(self, ctx:gramaticaParser.Mov2Context):
        angle = int(ctx.NUMBER(0).getText())
        move = int(ctx.NUMBER(1).getText())
        turtle.right(angle)
        turtle.forward(move)

        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by gramaticaParser#Rep.    
    def visitRep(self, ctx:gramaticaParser.RepContext):
        num = int(ctx.NUMBER().getText())  # Obtener el número de repeticiones
        stat = ctx.stat(0)  # Obtener la sentencia a repetir
        
        for _ in range(num-1):
            self.visit(stat)  # Visitar la sentencia la cantidad especificada de veces
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done()
        return self.visitChildren(ctx)



del gramaticaParser