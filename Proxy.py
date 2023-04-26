class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("Solicitação de tratamento.")

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Verificando o acesso antes de disparar uma solicitação real.")
        return True

    def log_access(self):
        print("Registrando a hora da solicitação.")

real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()