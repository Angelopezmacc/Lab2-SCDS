def type_input(text):
    datatype = type(text)
    if datatype == str:
        try:
            a = input("INGRESE EL COMANDO QUE DESEA EJECUTAR: ")
            exec(a)
        except:
            print(text)
        
    elif datatype == int or datatype == float:
        print(text)
        
type_input("test")
"""

Comando vulnerable: __import__('os').system("comando_deseado")

"""
