from xml.etree.ElementTree import parse

arbol2 = parse("libros.xml")
D = {} #Este diccionario almacena el nombre y el ID
for nodo in arbol2.findall("book"): #Recorre el libro de etiquetas y busca la etiqueta "book"
	ID = nodo.attrib["id"]
	for titulo in nodo.findall("title"): # Se debe ejecutar en nodo "book", Busca la etiqueta title
		D[ID] = titulo.text

for llave in D:
	print(llave,"->",D[llave])