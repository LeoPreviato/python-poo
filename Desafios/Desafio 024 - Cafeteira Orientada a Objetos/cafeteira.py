from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    """
    Classe abstrata que representa uma bebida quente.
    Define o template para preparar bebidas quentes, incluindo fervura da água,
    mistura e serviço.
    """

    def preparar(self):
        """
        Método que coordena a preparação da bebida.
        Imprime as etapas de preparação da bebida.
        """
        print("--- Preparando a sua bebida ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Sua bebida está pronta! ---")

    def ferver_agua(self):
        """
        Método que simula a fervura da água.
        Imprime a etapa de fervura da água a 100 graus Celsius.
        """
        print("1 - Fervendo a água em 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        """
        Método abstrato para misturar os ingredientes da bebida.
        Deve ser implementado pelas subclasses.
        """
        pass

    @abstractmethod
    def servir(self):
        """
        Método abstrato para servir a bebida.
        Deve ser implementado pelas subclasses.
        """
        pass

class Cafe(BebidaQuente):
    """
    Classe que representa um café.
    Implementa os métodos de mistura e serviço específicos para café.
    """

    def misturar(self):
        """
        Método que simula a mistura para café.
        Imprime a etapa de passar água pressurizada pelo pó de café.
        """
        print("2 - Passando água pressurizada pelo pó de café moido.")

    def servir(self):
        """
        Método que simula o serviço do café.
        Imprime a etapa de servir em uma xícara pequena.
        """
        print("3 - Servindo em uma xícara pequena.")

class Cha(BebidaQuente):
    """
    Classe que representa um chá.
    Implementa os métodos de mistura e serviço específicos para chá.
    """

    def misturar(self):
        """
        Método que simula a mistura para chá.
        Imprime a etapa de mergulhar o sachê de ervas na água quente.
        """
        print("2 - Mergulhando o sachê de ervas na água quente.")

    def servir(self):
        """
        Método que simula o serviço do chá.
        Imprime a etapa de servir na caneca de porcelana com limão.
        """
        print("3 - Servindo na caneca de porcelana com limão.")

class Leite(BebidaQuente):
    """
    Classe que representa leite aquecido (ex.: para cappuccino).
    Implementa os métodos de mistura e serviço específicos para leite.
    """

    def misturar(self):
        """
        Método que simula a mistura para leite.
        Imprime a etapa de passar vapor pressurizado pelo bico do leite.
        """
        print("2 - Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        """
        Método que simula o serviço do leite.
        Imprime a etapa de servir na caneca grande, já com café.
        """
        print("3 - Servindo na caneca grande, já com café")