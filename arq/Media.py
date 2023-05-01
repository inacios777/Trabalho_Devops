def media_aritmetica(valores):
        """ Calcula a média aritmética de uma lista de números passada em
        `valores`, retorna a média ou então None caso não a lista esteja
        vazia. """
        quantidade = len(valores)
        if quantidade:
            return sum(valores) / quantidade
        else:
            return False

# teste