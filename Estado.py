class Estado:
    """
    Classe padrão de estados.
    """
    numero = None
    proximo = None

    def __init__(self, nome=None, numero=None, proximo=None, tabular=""):
        """
        Inicialização da classe estado.
        :param nome: String contendo o nome deste estado.
        :param numero: Integer contendo o número deste estado.
        :param proximo: String nomeando o próximo estado.
        """
        if nome:
            self.nome = nome
        else:
            self.nome = self.__class__.__name__
        if numero:
            self.numero = numero
        if proximo:
            self.proximo = proximo

        self.tabular = tabular

    def __str__(self):
        return self.nome

    def executa(self, **kwargs):
        """
        Executa o estado atual de acordo com parametros passados e retorna o próximo.
        :param kwargs: dicionário de parametros.
        :return:
        """
        pass
