class Cliente:
    def __init__(self, nombre:str, apellido:str, cedula:str, email:str
                 , vip:bool=False, direccion:str=None
                 , telefono:str=None, celular:str=None, edad:int=None):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.email = email
        self.vip = vip
        self.direccion = direccion
        self.telefono = telefono
        self.celular = celular
        self.edad = edad

    def __str__(self):
        return f'Cliente: [{self.__dict__.__str__()}]'
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    @property
    def apellido (self):
        return self._apellido
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido
    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email
    @property
    def vip(self):
        return self._vip
    @vip.setter
    def vip(self, nuevo_vip):
        self._vip = nuevo_vip
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, nuevo_telefono):
        self._telefono = nuevo_telefono
    @property
    def celular(self):
        return self._celular
    @celular.setter
    def celular(self, nuevo_celular):
        self._celular = nuevo_celular
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

if __name__ == '__main__':
    cliente1 = Cliente(nombre='Matias', apellido='Ron', cedula='0930126446'
                        , email='matias.ronv@ug.edu.ec', vip=False
                        , direccion='Norte', telefono = '043593621'
                        , celular = '0984954223', edad = 20)
    print(cliente1)