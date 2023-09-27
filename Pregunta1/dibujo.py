import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = gramaticaVisitor()
    visitor.visit(tree)