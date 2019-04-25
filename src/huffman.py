# -*- coding: utf-8 -*-

from os import path
import argparse
from huffmantree import HuffmanTree
import pickle as pkl

parser = argparse.ArgumentParser('Algoritmo da Árvore de Huffman')
parser.add_argument('file', help='Arquivo de entrada', nargs='?', default=None)
parser.add_argument(
    'pickle_file', help='Arquivo com o objeto', nargs='?', default=None)
parser.add_argument(
    '-d', '--decode', help='Usado para realizar o decode', action='store_true')
args = parser.parse_args()

if __name__ == '__main__':
    try:
        # verifica se é uma arquivo
        if args.file:
            with open(args.file, 'r') as in_file:
                text = in_file.read()

                # verifica se é para realizar o decode
                if args.decode:
                    tree = pkl.load(open(args.pickle_file, 'rb'))
                    print(tree.decode(text))

                else:
                    # realiza o encode do texto e salva o objeto
                    tree = HuffmanTree()
                    tree.add_text(text)
                    tree.mount()

                    print(tree.encode(text))

                    # salva o objeto
                    pkl.dump(tree, open(
                        path.splitext(args.file)[-2] + '.code', 'wb'))
        else:
            # modo interativo
            while True:
                text = input()

                if len(text) > 0:
                    characters = list(text)
                    tree = HuffmanTree()
                    tree.add_text(text)
                    tree.mount()
                    # print(tree.dict)
                    code = tree.encode(text)
                    print(code)
                    # print(tree.decode(code))

                else:
                    raise EOFError
    except EOFError:
        pass
