import xml.etree.ElementTree as ET,sys

class Agenda2:

    def obtener_ruta(self):
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        return root

    def escribir_agenda(self,r,f):
        r.write(f,encoding='UTF-8',xml_declaration=True)

    def iniciar_agenda(self):
        menu = ["   --------- AGENDA ---------","1. Guardar datos de un contacto","2. Modificar datos de un contacto","3. Dar de baja a un contacto (Eliminar)","4. Buscar un contacto","5. Salir de la agenda","   --------------------------"]
        opciones = {'1': self.nuevo_contacto,'2' : self.modificar,'3' : self.eliminar, '4' : self.buscar, '5' : self.cerrar}
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
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        for element in root.findall("contactos"):
            nuevo = ET.SubElement(element, 'contacto')
            node = ET.SubElement(nuevo, 'nombre')
            node.text = str(input("Introduce un nombre : "))

            node = ET.SubElement(nuevo, 'apellido')
            node.text = str(input("Introduce los apellidos : "))

            node = ET.SubElement(nuevo, 'email')
            node.text = str(input("Introduce un email : "))

            node = ET.SubElement(nuevo, 'telefono1')
            numero = str(input("Introduce un número : "))
            self.comprobar_numero(numero)
            node.text = numero

            node = ET.SubElement(nuevo, 'telefono2')
            node.text = str(input("Introduce otro número : "))

            node = ET.SubElement(nuevo, 'direccion')
            node.text = str(input("Introduce la dirección : "))
            self.escribir_agenda(xmlTree,file)

    def comprobar_numero(self,num):
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        for element in root.findall("contactos"):
            for i in element.findall("contacto"):
                    if i.find('telefono1').text == num:
                        print("Lo sentimos, ese número ya existe")
                        self.iniciar_agenda()

    def modificar(self):
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        mod = str(input('Introduce el número de la persona que quieras modificar : '))
        for n in root.findall("contactos"):
            for m in n:
                if m.find('telefono1').text == mod:
                    nombre = str(input('Introduce el nombre : '))
                    m.find('nombre').text = nombre
                    apellidos = str(input('Introduce los apellidos : '))
                    m.find('apellido').text = apellidos
                    email = str(input('Introduce el email : '))
                    m.find('email').text = email
                    t1 = str(input('Introduce un número de teléfono : '))
                    self.comprobar_numero(t1)
                    m.find('telefono1').text = t1
                    t2 = str(input('Introduce otro número de teléfono : '))
                    m.find('telefono2').text = t2
                    direccion = str(input('Introduce la dirección : '))
                    m.find('direccion').text = direccion
                    self.escribir_agenda(xmlTree,file)
                    self.iniciar_agenda()
            print("Ese número no existe")
            self.iniciar_agenda()
                

    def eliminar(self):
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        borrar = str(input('Introduce el número de la persona que deseas eliminar : '))
        for a in root.findall("contactos"):
            for b in a:
                print(b.find('telefono1').text)
                if b.find('telefono1').text == borrar:
                    a.remove(b)
                    self.escribir_agenda(xmlTree,file)
                    self.iniciar_agenda()
        print("Ese número no existe")
        self.iniciar_agenda()

    def buscar(self):
        file = "./contactos.xml"
        xmlTree = ET.parse(file)
        root = xmlTree.getroot()
        buscar = str(input('Introduce el número del la persona que quieres buscar : '))
        for e in root.findall("contactos"):
            for v in e:
                if v.find('telefono1').text == buscar:
                    nombre = v.find('nombre').text
                    apellidos = v.find('apellido').text
                    email = v.find('email').text
                    t1 = v.find('telefono1').text
                    t2 = v.find('telefono2').text
                    direccion = v.find('direccion').text
                    print(nombre +" | "+apellidos+" | "+email+" | "+t1+" | "+t2+" | "+direccion)
                    self.iniciar_agenda()
        print("Ese número no existe")
        self.iniciar_agenda()
    
    def cerrar(self):
        sys.exit()

a2 = Agenda2()
a2.iniciar_agenda()
