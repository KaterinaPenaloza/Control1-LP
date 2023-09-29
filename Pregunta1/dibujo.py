import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor

#Codigo base del programa para su funcionamiento
if __name__ == '__main__':
    #Maneja los argumentos dados, si es un archivo o por input en la linea de comandos
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

#Definiciones de los archivos (lexer, los tokens a partir del analizador léxico y el parser)
    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)
#Se realiza el análisis sintáctico con el parser y se obtiene el AST
#Luego el arbol generado se pasa a string en formato lisp
    tree = parser.prog()
    lisp_tree_str = tree.toStringTree(recog=parser)
    print(lisp_tree_str)
#Se realiza la visita de los nodos para la ejecucion
    visitor = gramaticaVisitor()
    visitor.visit(tree)