from math import *

##1:
class triangulo:
    def __init__(self,b1,b2,h):
        self.base = b1
        self.base2 = b2
        self.hipo = h

    def perimetro(self):
        return self.base+self.base2+self.hipo

    def area(self):
        d = self.perimetro()/2
        return sqrt(d*(d-self.hipo)*(d-self.base)*(d-self.base2))

    def angulo(self):
        return (3-2)*180/3

class quadrilatero:
    def __init__(self,l,ln):
        self.lado = l
        self.ladon = ln
    def perimetro(self):
        return (self.lado+self.ladon)*2
    def area(self):
        return self.lado*self.ladon
    def angulo(self):
        return ((4-2)*180)/4

class Pentagono:
    def __init__(self,l):
      self.lado=l
   
    def perimetro(self):
      return 5*self.lado
 
    def area(self):
      ai=(360/5)/2
      apotema=self.lado/(2*tan(ai*pi/180))
      return (self.perimetro()*apotema)/2
 
    def angulos(self):
      return (180*(5-2))/5

class trapezio:
    def __init__(self,b,bn, h):
        self.base = b
        self.basen = bn
        self.altura = h
    def perimetro(self):
        return self.base+self.basen+2*(math.sqrt((self.base-self.basen)**2+(self.altura)**2))
    def area(self):
        return self.base*self.basen
    def angulo(self):
        return ((4-2)*180)/4





class Hexagono:
    def __init__(self,l,ln):
        self.lado = l
    def perimetro(self):
        return 6*self.lado
    def area(self):
        return (3*self.lado**2*math.sqrt(3))/2
    def angulo(self):
        return ((6-2)*180)/6

class octogono:
    def __init__(self,l):
        self.lado = l
    def perimetro(self):
        return self.lado*8
    def area(self):
        return 2*self.lado**2*math.sqrt(3)
    def angulo(self):
        return ((8-2)*180)/8
        
class FigurasGeometricas:
  def __init__(self):
    entrada=input('Escolha a figura geométrica:\n1-Triângulo\n2-Quadrado\n3-Pentágono\n4-Exágono\n5-Octógono\nFigura geométrica:')
    if entrada=='1':
        print('Escolha os lados:')
        h=float(input('hipotenusa:'))
        b1=float(input('lado 1:'))
        b2=float(input('lado 2:'))
        t=triangulo(b1,b2,h)
        print('Perímetro:',t.perimetro(),', área:',t.area(),', ângulos:',t.angulos())
    if entrada=='2':
        l=float(input('Lado 1:'))
        ln=float(input('Lado 2:'))
        q=quadrilatero(l,ln)
        print('Perímetro:',q.perimetro(),', área:',q.area(),', ângulos:',q.angulos())
    if entrada=='3':
        l=float(input('Lado:'))
        p=Pentagono(l)
        print('Perímetro:',p.perimetro(),', área:',p.area(),', ângulos:',p.angulos())
    if entrada=='4':
        l=float(input('Lado:'))
        ln=float(input('Lado 2:'))
        h=Hexagono(l,ln)
        print('Perímetro:',h.perimetro(),', área:',h.area(),', ângulos:',h.angulos())
    if entrada=='5':
        l=float(input('Lado:'))
        o=octogono(l)
        print('Perímetro:',o.perimetro(),', área:',o.area(),', ângulos:',o.angulos())
    if entrada=='6':
        b=float(input('Base 1:'))
        bn=float(input('Base 2:'))
        h=float(input('Altura:'))
        t=trapezio(b,bn,h)
        print('Perimetro:',t.perimetro(),', area:',t.area(),', angulos:',t.angulo())
        
  



##3:
class perimetro:
    def __init__(self,n,t):
        self.nlado = n
        self.tamanho = t

    def __mul__(self):
        return self.nlado*self.tamanho
##p = perimetro(6,6)
##print (perimetro().__mul__())


class outros(perimetro):
    def __init__(self,n,t,h,b1=0,b2=0):
        super().__init__(n,t)
        self.nlado = n
        self.tamanho = t
        self.altura = h
        self.base1 = b1
        self.base2 = b2

    def area(self):
        if self.nlado == 4 and b1!= b2:
            return (self.base1+self.base2)*self.altura/2
        else:
            return self.nlado*(self.tamanho*self.altura)/2

    def anint(self):
        return ((self.nlado-2)*180)/self.nlado

o = outros(6,6,6)
##print (o.area())
##print (o.anint())





##2:        
class padaria:
    def client(self):
        return ("Hello, how can we help you today?")
    def bread(self):
        return ("Very well, your equivalent value of bread will be ready in approximately 10 seconds dear costumer.")
    def over(self):
        return ("I am sorry to inform that all our production for the day has already been sold")
    def closing(self):
        return ("Thank you for using our services, the store will now be closing, we expect to see you starting 6:00 am tomorrow dear costumer.")

p = padaria()
##print (p.closing())


