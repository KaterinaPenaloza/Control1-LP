# Generated from c:\\Users\\miap7\\Documents\\GitHub\\Control1-LP\\gramatica.g4 by ANTLR 4.9.2
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


    # Enter a parse tree produced by gramaticaParser#Dib.
    def enterDib(self, ctx:gramaticaParser.DibContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Dib.
    def exitDib(self, ctx:gramaticaParser.DibContext):
        pass



del gramaticaParser