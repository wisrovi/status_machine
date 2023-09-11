import time

import __main__


class Maquina:
    """
    Máquina de Estados.
    """

    def __init__(self, estados, inicial, tabular=""):
        """
        Estados deve ser um dicionário, inicial deve ser o primeiro estado.
        :param estados: lista de estados.
        :param inicial: estado inicial.
        """
        self.estados = self.inicializa(estados)
        self.atual = self.estados[inicial]
        self.tabular = tabular

    def get_estado(self):
        return self.atual

    def set_estado(self, estado):
        self.atual = self.estados[estado]

    def get_proximo(self):
        proximo = self.atual.proximo
        if proximo:
            if proximo in self.estados:  # Se não existe o estado retorna nada. TODO: Subir erro?
                return self.estados[self.atual.proximo]
            else:
                print(f'{self.tabular}[{__main__.__file__}]: Próximo estado: {proximo}, no existe!!!')
                return None
        return None

    def to_proximo(self):
        self.atual = self.get_proximo()

    @staticmethod
    def inicializa(estados):
        """
        Recebe uma lista de Estados e converte para um dicionário com o nome e objeto instanciado da classe.
        :param estados: lista ou dicionário de dados.
        :return: dicionario dos estados e nome.
        """
        if isinstance(estados, dict):
            return estados
        if isinstance(estados, list):
            estados_adecuados = {}
            for i, estado in enumerate(estados):
                estado.numero = i
                estados_adecuados[estado.nome] = estado
            return estados_adecuados

        iniciados = dict()
        for estado in estados:
            name = estado.nome
            iniciados[name] = estado
        return iniciados

    def executa(self, **kwargs):
        """
        Executa o estado atual e vai para o próximo.
        :return: None.
        """
        return self.atual.executa(**kwargs)

    def ciclo(self, **kwargs):
        """
        Percorre cada um dos estados, executa eles, até que o próximo seja None.
        :param kwargs:
        :return:
        """
        error = ""
        while self.atual is not None:
            try:
                kwargs = self.executa(**kwargs)
            except Exception as e:
                kwargs[f"error {self.atual}: "] = e.__str__()
                print(f'{self.tabular}[{self.atual}]: Error: {e.__str__()}')
                break
            self.to_proximo()
        return kwargs


if __name__ == '__main__':

    class Analizar(Estado):
        numero = 1

        def executa(self, **kwargs):
            time.sleep(1)
            print('Executando estado: {}'.format(self.nome), kwargs.get("x"))


    class CrearModelo(Estado):
        numero = 2

        def executa(self, **kwargs):
            time.sleep(1)
            print('Executando estado: {}'.format(self.nome), kwargs.get("y"))


    class Entrenar(Estado):
        numero = 3

        def executa(self, **kwargs):
            time.sleep(1)
            try:
                print('Executando estado: {}'.format(self.nome), kwargs["z"])
            except KeyError:
                return "Error"


    class Predecir(Estado):
        numero = 4

        def executa(self, **kwargs):
            time.sleep(1)
            print('Executando estado: {}'.format(self.nome), kwargs.get("w"))


    # estados = {
    #    '1_analizar': Analizar('1_analizar', 1, '2_crearModelo'),
    #    '2_crearModelo': CrearModelo('2_crearModelo', 2, '3_entrenar'),
    #    '3_entrenar': Entrenar('3_entrenar', 3, '4_predecir'),
    #    '4_predecir': Predecir('4_predecir', 4, "queso"),
    # }

    # crear estado en lista
    estados = [
        Analizar(proximo="CrearModelo"),
        CrearModelo(proximo="Entrenar"),
        Entrenar(proximo="Entrenar2"),
        Entrenar(nome="Entrenar2", proximo="Analizar2"),
        Analizar(nome="Analizar2", proximo="Predecir"),
        Predecir(proximo=None)
    ]
    maquina = Maquina(estados, 'Analizar')

    data = {
        "x": "hola",
        "y": "mundo",
        "z": "que tal",
        "w": "estas?"
    }
    maquina.ciclo(**data)

    # Executando estado: 1_analizar
    # Executando estado: 2_crearModelo
    # Executando estado: 3_entrenar
    # Executando estado: 4_predecir
