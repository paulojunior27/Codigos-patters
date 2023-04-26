class Subject:
    def __init__(self):
        self._observers = []

    def anexar(self, observer):
        self._observers.append(observer)

    def separar(self, observer):
        self._observers.remove(observer)

    def notificar(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class Observador1(Observer):
    def update(self):
        print("Observador1: Reagiu ao evento.")

class Observador2(Observer):
    def update(self):
        print("Observador2: Reagiu ao evento.")

class Assunto(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        self.notificar()

# Example usage:
subject = Assunto()
observer1 = Observador1()
observer2 = Observador2()

subject.anexar(observer1)
subject.anexar(observer2)

subject.set_state("Novo status")