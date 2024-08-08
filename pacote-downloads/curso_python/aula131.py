# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_all(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

c1 = Conection()
c1.set_user('Ste')
c1.set_password('278')
print(c1.user)
print(c1.password)
print()
c2 = Conection.create_all('Bizu', 'M278')
print(c2.user)
print(c2.password)


