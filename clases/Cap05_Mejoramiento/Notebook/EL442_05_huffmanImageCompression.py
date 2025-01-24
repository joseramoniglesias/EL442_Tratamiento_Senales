import time, pickle, codecs
import numpy as np
import Tkinter
from PIL import ImageDraw
import Image
import ImageTk
from os import stat
from sys import argv

class Node:
    def __init__(self, symbol, nodeLeft, nodeRight, frequency):
        self.label = ''
        self.symbol = symbol
        self.nodeLeft = nodeLeft
        self.nodeRight = nodeRight
        self.frequency = frequency
        return

    def __repr__(self):
        return '( %s ) [%s] %d' % (self.label, str(self.symbol), self.frequency)

    def name(self, prefix):
        self.label = prefix
        if self.nodeLeft is not None:
            self.nodeLeft.name('%s1' % self.label)
        if self.nodeRight is not None:
            self.nodeRight.name('%s0' % self.label)
        return

    def decode(self, binary):
        if self.symbol is not None:
            return (self.symbol, binary)
        else:
            assert(self.nodeLeft is not None)
            assert(self.nodeRight is not None)
            bit = binary[0]
            binary = binary[1:]
            if bit == '1':
                return self.nodeLeft.decode(binary)
            elif bit == '0':
                return self.nodeRight.decode(binary)
            else:
                print 'Something is wrong.'
        return

    def insert(self, dictionary):
        if self.nodeLeft is not None:
            self.nodeLeft.insert(dictionary)
        if self.nodeRight is not None:
            self.nodeRight.insert(dictionary)
        if self.symbol is not None:
            dictionary[self.symbol] = self.label
        return

def main():
    #Ask for your selection compress or decompress or cancel
    opcion = raw_input("--> Desea comprimir o descomprimir? comprimir / descomprimir / cancelar (cancel) >")
    #Ask for your file to compress or decompress
    nombre_de_archivo = raw_input("--> Ingrese el nombre del archivo >")
    
    if opcion == "comprimir":
        #open the image
        archivo = Image.open(nombre_de_archivo)
        #we work with gray scale
        archivo = archivo.convert('L')
        #extract the matrix of the file
        matriz = np.array(archivo)
        #get the size
        renglones, columnas = matriz.shape
        #DEBUG
        print renglones, columnas
        #create a dictionary 
        pixeles = dict()
        #iterate the matrix
        for r in xrange(renglones):
            for c in xrange(columnas):
                #debug
                print matriz[r,c]
                #save the frequencies of each pixel value
                if matriz[r,c] in pixeles.keys():
                    pixeles[matriz[r,c]] += 1
                else:
                    pixeles[matriz[r,c]] = 1
        print pixeles
        #create a node that will represent a three
        node_list = list()
        for p in pixeles.keys():
            #save each pixel and his value as a node of the three
            node_list.append(Node(p, None, None, pixeles[p] ))
        #order the three by using as a reference the frequency
        while len(node_list) > 1:
            node_list.sort(key=lambda n: n.frequency)
            min1 = node_list.pop(0)
            min2 = node_list.pop(0)
            node_list.append(Node(None, min1, min2, min1.frequency + min2.frequency)) 
        #remove a node empty
        root = node_list.pop(0)
        root.name('')
        code = dict()
        #extract the three in a dictionary
        root.insert(code)
        #sabe the object of the three
        archivo_del_objeto = open('%s.objeto'%(nombre_de_archivo),'w')
        pickle.dump(root, archivo_del_objeto)
        archivo_del_objeto.close()
        #Create a binary content by using the three
        binary = ''
        for s in pixeles:
            binary = '%s%s' % (binary, code[s])
        print binary
        binary = binary[1:]
        #save the content binary
        nuevo_archivo = open("%s.compress"%(nombre_de_archivo),'w')
        nuevo_archivo.write(binary)
        nuevo_archivo.close()
        print binary
        statusFile = stat(nombre_de_archivo)
        #we print out the time and size of the file
        print "time: %s size: %s"%(time.clock(),statusFile.st_size) 
        archivo_del_objeto.close()
        
    elif opcion == "descomprimir":
        #open the file object
        archivo_del_objeto = open('%s.objeto'%(nombre_de_archivo),'r')
        root = pickle.load(archivo_del_objeto)
        archivo_del_objeto.close()
        #create a dictionary
        code = dict()
        #extract all the references of the three
        root.insert(code)
        #open the file comprress
        nuevo_archivo = open("%s.compress"%(nombre_de_archivo),'r')
        binary = nuevo_archivo.read()
        nuevo_archivo.close()
        print binary
        recovered = ''
        #recurvibly decode the content compress by
        #usign the object extracted before
        while len(binary) > 0:
            (symbol, binary) = root.decode(binary)
            recovered = '%s,%s' % (recovered, symbol)
        #create a new file in gray scale
        archivo = Image.open(nombre_de_archivo)
        archivo = archivo.convert('L')
        matriz = np.array(archivo)
        print matriz.shape
        renglones, columnas = matriz.shape
        new_img = Image.new(mode='L', size=(columnas, renglones))
        img = new_img.load()
        #split all the values
        recovered = recovered.split(',')
        recovered = recovered[1:]
        print len(recovered)
        print recovered
        #iterate the image
        for r in xrange(renglones):
            for c in xrange(columnas):
                    #we pute the value of the pixel recovered
                    img[r, c] = int(recovered.pop(0))
        img = Image.fromarray(np.array(new_img))
        #save the image
        img.save('%s.decompress.png'%(nombre_de_archivo))

    elif opcion == "cancelar":
        print "--> BYE."

main()