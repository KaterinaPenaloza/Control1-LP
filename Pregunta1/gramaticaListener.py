# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\Pregunta1\\gramatica.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#prog.
    def enterProg(self, ctx:gramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by gramaticaParser#prog.
    def exitProg(self, ctx:gramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStat.
    def enterPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStat.
    def exitPrintStat(self, ctx:gramaticaParser.PrintStatContext):
        pass


    # Enter a parse tree produced by gramaticaParser#blank.
    def enterBlank(self, ctx:gramaticaParser.BlankContext):
        pass

    # Exit a parse tree produced by gramaticaParser#blank.
    def exitBlank(self, ctx:gramaticaParser.BlankContext):
        pass


    # Enter a parse tree produced by gramaticaParser#On.
    def enterOn(self, ctx:gramaticaParser.OnContext):
        pass

    # Exit a parse tree produced by gramaticaParser#On.
    def exitOn(self, ctx:gramaticaParser.OnContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Off.
    def enterOff(self, ctx:gramaticaParser.OffContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Off.
    def exitOff(self, ctx:gramaticaParser.OffContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Mov.
    def enterMov(self, ctx:gramaticaParser.MovContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Mov.
    def exitMov(self, ctx:gramaticaParser.MovContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Mov2.
    def enterMov2(self, ctx:gramaticaParser.Mov2Context):
        pass

    # Exit a parse tree produced by gramaticaParser#Mov2.
    def exitMov2(self, ctx:gramaticaParser.Mov2Context):
        pass


    # Enter a parse tree produced by gramaticaParser#fin.
    def enterFin(self, ctx:gramaticaParser.FinContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fin.
    def exitFin(self, ctx:gramaticaParser.FinContext):
        pass



del gramaticaParser