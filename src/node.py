# -*- coding: utf-8 -*-


class Node():
    '''
        Nó da árvore

        attr:
            label(str): label do nó
            value(int): valor ou frequência do nó
            right(Node): filho da direita
            left(Node): filho da esquerda 
    '''
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return str((self.label, self.value, self.left, self.right))
