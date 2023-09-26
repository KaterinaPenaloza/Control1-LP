# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
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


    # Visit a parse tree produced by gramaticaParser#On.
    def visitOn(self, ctx:gramaticaParser.OnContext):
        print("Hola mundo")
        
        skk = turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
     
        turtle.done()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Off.
    def visitOff(self, ctx:gramaticaParser.OffContext):
        print(1+1)
        setup(450, 150, 0, 0)
        screensize(300, 150)

        goto(100, 0)

        exitonclick()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by gramaticaParser#Mov.
    def visitMov(self, ctx:gramaticaParser.MovContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Dib.
    def visitDib(self, ctx:gramaticaParser.DibContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        return self.visitChildren(ctx)



del gramaticaParser