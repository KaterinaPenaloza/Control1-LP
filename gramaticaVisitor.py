# Generated from c:\\Users\\Kzwy\\Desktop\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
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
        value = self.visit(ctx.stat())
        print(value)
        return 0


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
        #turtle.done()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Dib.
    def visitDib(self, ctx:gramaticaParser.DibContext):
        
        turtle.goto(100,50)
        #turtle.forward(100)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#fin.
    def visitFin(self, ctx:gramaticaParser.FinContext):
        turtle.done()
        return 0



del gramaticaParser