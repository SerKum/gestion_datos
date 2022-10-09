import xml.etree.ElementTree as ET
import csv

with open('contactos.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    root = ET.Element('agenda') 
    contactos = ET.SubElement(root, 'contactos')
    for line in csv_reader:
	    ent = ET.SubElement(contactos, 'contacto')
	    node = ET.SubElement(ent, 'nombre')
	    node.text = line['Nombre']

	    node = ET.SubElement(ent, 'apellido')
	    node.text = line['Apellidos']

	    node = ET.SubElement(ent, 'email')
	    node.text = line['Email']

	    node = ET.SubElement(ent, 'telefono1')
	    node.text = line['Tel1']

	    node = ET.SubElement(ent, 'telefono2')
	    node.text = line['Tel2']

	    node = ET.SubElement(ent, 'direccion')
	    node.text = line['Direccion']

with open('contactos.xml', 'w') as f:
    xml_str = ET.tostring(root)
    f.write(xml_str.decode("utf8"))




