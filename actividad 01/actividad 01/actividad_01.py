import os
class Paquete():
    id_=0
    origen=0
    destino=0
    peso=0
    def __init__(self,id,origen,destino,peso):
        self.id_=id
        self.origen=origen
        self.destino=destino
        self.peso=peso
    #id getter setter
    def id_setter(self,id):
        self.id_=id
    def id_getter(self):
        return str(self.id_)
    #origen getter setter
    def origen_setter(self,origen):
        self.origen=origen
    def origen_getter(self):
        return self.origen
    #destino getter setter
    def destino_setter(self,destino):
        self.destino=destino
    def destino_getter(self):
        return self.destino
    #peso getter setter
    def peso_setter(self,peso):
        self.peso=peso
    def peso_getter(self):
        return str(self.peso)


class Paqueteria():
    paquetes=list()

    def insertar_inicio(self,id_,origen,destino,peso):
        p=Paquete(id_,origen,destino,peso)
        l=[p]
        self.paquetes=l+self.paquetes
    def eliminar_inicio(self):
        self.paquetes.pop(0)
    def Mostrar(self):
        for i in range(len(self.paquetes)):
            print(self.paquetes[i].id_getter(),self.paquetes[i].origen_getter(),self.paquetes[i].destino_getter(),self.paquetes[i].peso_getter())
            print('\n')
    def Guardar(self):
        f = open ('paquetes.txt','a')
        for i in range(len(self.paquetes)):
            self.paquetes.pop()
            f.write(self.paquetes[i].id_getter()+',')
            f.write(self.paquetes[i].origen_getter()+',')
            f.write(self.paquetes[i].destino_getter()+',')
            f.write(self.paquetes[i].peso_getter()+'\n')
        f.close()
    def Recuperar(self):
        f=open('paquetes.txt','r')
        F=f.readlines()
        for i in F:
            i=i.split(',')
            self.insertar_inicio(i[0],i[1],i[2],i[3])
        f.close()


def menu():
    paqueteria=Paqueteria()
    while(True):
        os.system("CLS")
        print('menu paqueteria \n')
        print('elige una opcion \n')
        print('1 agregar paquete\n')
        print('2 eliminar paquete\n')
        print('3 mostrar paquetes\n')
        print('4 guardar respaldo\n')
        print('5 cargar respaldo\n')
        opc=int(input())
        if(opc==1):
            print('ingresa id\n')
            id=int(input())
            print('ingresa origen\n')
            origen=input()
            print('ingresa destino\n')
            destino=input()
            print('ingresa peso\n')
            peso=input()
            paqueteria.insertar_inicio(id,origen,destino,peso)
        elif(opc==2):
            paqueteria.eliminar_inicio()
        elif(opc==3):
            paqueteria.Mostrar()
        elif(opc==4):
            paqueteria.Guardar()
        elif(opc==5):
            paqueteria.Recuperar()


menu()