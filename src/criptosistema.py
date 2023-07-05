#!/usr/bin/env python3
#
#
#       Copyright 2022 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Criptosistema:

    def __init__(self):
        self.signo = lambda x: x and (1,-1)[x<0]

    def euclides(self,a,b):
        m, n = int(a), int(b)
        while n:
            m, n = n, m % n
        return m * self.signo (m)

    def xeuclides(self,a,b):
        m, n = int(a), int(b)
        u0, u1 = 1, 0
        v0, v1 = 0, 1
        while n:
            q = m // n
            m, n = n, m % n
            u0, u1 = u1, u0 - q * u1
            v0, v1 = v1, v0 - q * v1
        sg = self.signo (m)
        return m * sg, u0 * sg, v0 * sg

    def xeuclidesRed(self,a,b):
        """
        xeuclidesRed(a,b) proporciona (a,b) y s tales que
        a * s = (a,b) (mod b). Si (a,b) = 1, entonces s es 
        el inverso de a módulo b.
        """
        m, n = int(a), int(b)
        u0, u1 = 1, 0
        while n:
            q = m // n
            m, n = n, m % n
            u0, u1 = u1, u0 - q * u1
        sg = self.signo (m)
        return m * sg, u0 * sg

    # Criptosistema Afín
    def cifraAfinGen(self,alfabeto, a, b, m):
        codificado = [alfabeto[(a*alfabeto.index(i)+b) % len(alfabeto)] for i in m]
        return "".join(codificado)

    def llaveDescifradoAfinGen(self,alfabeto, a, b):
        def inversoMod(x,y):
            return self.xeuclidesRed(self,x,y)[1]
        x = inversoMod(a,len(alfabeto))
        return alfabeto, x, -x*b % len(alfabeto)

    # Ataque Criptosistema Afin a fuerza bruta
    def ataqueCAFuerzaBruta(self,alfabeto,cifra):
        file = open('resultados.txt','a')
        for i in xrange(len(alfabeto)):
            for j in xrange(len(alfabeto)):
                descifrado = cifraAfinGen(alfabeto, i, j, cifra)
                file.write(str(i)+','+str(j)+'\n' + descifrado+'\n')
        file.close()

if __name__ == "__main__":
    alfabeto = " abcdefghijklmnopqrstuvwxyz0123456789,.;:"
    recado = "el poder desgasta a quien no lo tiene"
    cifra = "2.eh9p27ep2fnrfsrereu5:2wew9e.9es:2w2"

    c1 = Criptosistema()
    
    print(c1.cifraAfinGen(alfabeto,13,5,recado))
    #print(c1.llaveDescifradoAfinGen(alfabeto,13,5))
    print(c1.cifraAfinGen(alfabeto,19,28,cifra))
    
    # 27=18 ---> imposible llevar a cabo la operacion. demasiada vigilancia
    cifra = '0ofi.0gr;mrr;2j mjmdjgimrjmif; jd0ilvma;oj.0jajm2060rjld0j'
    # 9=20 | 50=20 ---> mensaje para su superior: 77ztz4i:4i:o.ys,rh45z4t,fh4y4s,.,r,4,y4f,osy79ys
    #cifra = 'vlmighlp9grgpi5pi59lrqdryp..1 1xqyxqydb,ikrzxo1x kczx,xikbkrkxk,xckdi,.t,i'
    cifra = '77ztz4i:4i:o.ys,rh45z4t,fh4y4s,.,r,4,y4f,osy79ys'
    
    #print(len(cifra)/2)
    #print(c1.cifraAfinGen(alfabeto,29,38,cifra))
    for num1 in range(0,len(cifra)):
        for num2 in range(0,len(alfabeto)):
            print(str(num1)+'='+str(num2)+" ---> "+c1.cifraAfinGen(alfabeto,num1,num2,cifra))
