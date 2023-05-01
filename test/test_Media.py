def media_aritmetica(valores):
        """ Calcula a média aritmética de uma lista de números passada em
        `valores`, retorna a média ou então None caso não a lista esteja
        vazia. """
        quantidade = len(valores)
        if quantidade:
            return sum(valores) / quantidade
        else:
            return False
class TestMedias:
    def test_media_com_lista_numerica(self):
        """ Valida o cálculo da média. """
        assert media_aritmetica([1, 1]) == 1.0