import csv,sys


class Agenda: 

    def __init__(self):
        self.lista_contactos= []

    def abrir_agenda(self):
        with open('contactos.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for contacto in reader:
                con = Contacto(contacto['Nombre'],contacto['Apellidos'],contacto['Email'],contacto['Tel1'],contacto['Tel2'],contacto['Direccion'])
                self.lista_contactos.append(con)
            self.lista_contactos.sort(key=lambda x:x.nombre)
            for cont in self.lista_contactos:
                print(cont.get_datos())
        self.borrar_datos()
        self.iniciar_agenda()


    def cerrar_agenda(self):
        fieldnames=['Nombre','Apellidos','Email','Tel1','Tel2','Direccion']
        with open('contactos.csv', "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for a in self.lista_contactos:
                writer.writerow({'Nombre':a.get_nombre(),'Apellidos':a.get_apellidos(),'Email':a.get_email(),'Tel1':a.get_tel1(),'Tel2':a.get_tel2(),'Direccion':a.get_direccion()})

    def iniciar_agenda(self):
        menu = ["   --------- AGENDA ---------","1. Guardar datos de un contacto","2. Modificar datos de un contacto","3. Dar de baja a un contacto (Eliminar)","4. Buscar un contacto","5. Mostrar la lista de contactos ordenada","6. Salir de la agenda","   --------------------------"]
        opciones = {'1': self.nuevo_contacto,'2' : self.modificar,'3' : self.eliminar, '4' : self.buscar, '5' : self.abrir_agenda, '6' : self.cerrar}
        for i in menu:
            print(i,end="\n")
        while True:
            try:
                opcion = int(input())
                if opcion > 6 or opcion < 1:
                    print("Introduce una opción válida, por favor.\n")
                    self.iniciar_agenda()
                else : 
                    opciones[str(opcion)]()
            except ValueError:
                print("Eso no es un número válido\n")
                self.iniciar_agenda()
    
    def nuevo_contacto(self):
        nombre = str(input('Introduce el nombre : '))
        apellidos = str(input('Introduce los apellidos : '))
        email = str(input('Introduce el email : '))
        t1 = str(input('Introduce un número de teléfono : '))
        t2 = str(input('Introduce otro número de teléfono : '))
        direccion = str(input('Introduce la dirección : '))
        c = Contacto(nombre,apellidos,email,t1,t2,direccion)
        for m in self.lista_contactos:
            if m == c:
                print("Lo siento ese número ya existe, por favor introduce los datos correctos")
                self.nuevo_contacto()
        self.lista_contactos.append(c)
        self.iniciar_agenda()
       
    def modificar(self):
        mod = str(input('Introduce el número de la persona que quieras modificar : '))
        for n in self.lista_contactos:
            if n.get_tel1() == mod:
                nombre = str(input('Introduce el nombre : '))
                apellidos = str(input('Introduce los apellidos : '))
                email = str(input('Introduce el email : '))
                t1 = str(input('Introduce un número de teléfono : '))
                t2 = str(input('Introduce otro número de teléfono : '))
                direccion = str(input('Introduce la dirección : '))
                n.cambiar_datos(nombre,apellidos,email,t1,t2,direccion)
            else:
                print("Ese número no existe")
                self.iniciar_agenda()
                

    def eliminar(self):
        borrar = str(input('Introduce el número de la persona que deseas eliminar : '))
        for e in self.lista_contactos:
            if e.get_tel1() == borrar:
                self.lista_contactos.remove(e)
                self.iniciar_agenda()
        print("Ese número no existe")
        self.iniciar_agenda()

    def buscar(self):
        buscar = str(input('Introduce el número del la persona que quieres buscar : '))
        for b in self.lista_contactos:
            if b.get_tel1() == buscar:
                print(b.get_datos())
                self.iniciar_agenda()     
        print("Ese número no existe")
        self.iniciar_agenda()
    
    def cerrar(self):
        self.cerrar_agenda()
        sys.exit()

    def borrar_datos(self):
        file = open("contactos.csv", "w")
        file.close()


class Contacto:

    def __init__(self,nombre,apellidos,email,tel1,tel2,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.tel1 = tel1
        self.tel2 = tel2
        self.direccion = direccion

    def __eq__(self,otro):
        return self.tel1 == otro.tel1

    def get_datos(self):
        return self.nombre+' | '+self.apellidos+' | '+self.email+' | '+self.tel1+' | '+self.tel2+' | '+self.direccion
    
    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos
    
    def get_email(self):
        return self.email

    def get_tel1(self):
        return self.tel1

    def get_tel2(self):
        return self.tel2

    def get_direccion(self):
        return self.direccion

    def cambiar_datos(self,nombre,apellidos,email,tel1,tel2,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.tel1 = tel1
        self.tel2 = tel2
        self.direccion = direccion
        