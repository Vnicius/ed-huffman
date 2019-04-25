# -*- coding: utf-8 -*-

from node import Node
from collections import Counter


class HuffmanTree():
    '''
        Classe com a Árvore de Huffman

        attr:
            nodes(Node[]): lista de nós
            head(Node): nó raíz
            dict(dict): dicionário com os códigos
            reversed_dict(dict): dicionário invertido
    '''

    def __init__(self):
        '''
            Construtor
        '''
        self.nodes = []
        self.head = None
        self.dict = {}
        self.reversed_dict = {}

    def add_text(self, text):
        count = Counter(list(text))
        for key in count:
            self.add_node(Node(key, count[key]))

    def add_node(self, node):
        '''
            Adiciona um nó na lista

            params:
                node(Node): novo nó a ser adicionado
        '''
        self.nodes.append(node)

        # ordena inversamente pelo valor do nó
        self.nodes.sort(key=lambda x: x.value, reverse=True)

    def mount(self):
        '''
            Contrói a Árvore de Huffman
        '''
        while len(self.nodes) > 1:

            # pegar nó da esquerda e direita
            # que são os dois úlitmos da lista
            node_left = self.nodes[-2]
            node_right = self.nodes[-1]

            # novo nó que será o pai dos dois anterires
            node = Node(node_left.label + node_right.label,
                        node_left.value + node_right.value)

            # atribuir os nós filhos ao pai
            node.left = node_left
            node.right = node_right

            # remover os dois último nós
            self.nodes = self.nodes[:-2]

            # adicionar o novo nó
            self.add_node(node)

        # salva a raiz
        self.head = self.nodes[0]

        # criar o dicionário das letras
        self.__mount_dict()

        # criar dicionário invertido
        self.__reverse_dict()

    def __mount_dict(self):
        '''
            Cria o dicionário das letras com
            o repectivo código
        '''
        self.__nav_tree(self.head, '')

    def __nav_tree(self, node, code):
        '''
            Navega pela ávore e adiciona o código ao dicionário
        '''

        # se for um nó folha
        if node.left == node.right:
            self.dict[node.label] = code
        else:

            # olhar nó da esquerda
            if node.left:
                self.__nav_tree(node.left, code + '0')

            # olhar nó da direita
            if node.right:
                self.__nav_tree(node.right, code + '1')

    def __reverse_dict(self):
        '''
            Cria o dicionário revertido
        '''
        self.reversed_dict = {self.dict[key]: key for key in self.dict}

    def encode(self, text):
        '''
            Realiza o encode em um texto, usando o dicionário criado

            params:
                text(str): texto original
        '''
        result = ''

        for letter in list(text):

            # verifica se a letra está no dicionário
            if self.dict.get(letter):
                result += self.dict[letter]
            else:
                result += '?'

        return result

    def decode(self, code):
        '''
            Decodificar o códido em texto

            params:
                code(str): código
        '''
        result = ''
        acc = ''

        code = [c for c in code if c.isdigit()]

        for number in code:
            acc += number

            # verifica se está no dicionário
            if self.reversed_dict.get(acc):
                result += self.reversed_dict[acc]
                acc = ''

        return result
