for n in range(1,10+1):
    with open ("archivo "+str(n)+ ".txt","w",n) as file:
        file.write("Hola mundo")