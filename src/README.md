# Codificação de Huffman

## Dependências

- Python 3.x

## Execução

```sh
usage: huffman.py [-h][-d] [file][pickle_file]

positional arguments:
file Arquivo de entrada
pickle_file Arquivo com o objeto

optional arguments:
-h, --help show this help message and exit
-d, --decode Usado para realizar o decode
```

### Interativo

```sh
    $ python huffman.py
    abcdef
    0100110000011011
```

### Codificação por arquivo

```sh
    $ python huffman.py file.txt > file_cod.txt
```

### Decodificação por aquivo

```sh
    $ python huffman.py -d file_cod.txt file.code > out.txt
```
