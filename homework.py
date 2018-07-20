import random

from copy import deepcopy

import random
 


class Matrix():

    def __init__(self,name, nrows, ncols):
        self.name = name
        self.nrows = nrows
        self.ncols = ncols
        self.matrix = []
        self.matrix1 = []
        
        print(self.name)
        x= int(input('Enter  matrics row:'))
        y= int(input('Enter  matrics col:'))

        for a in range(0,x):
            m = []
            for b in range(0,y):
                buffer = random.randint(1, 9)
                m.append(buffer)
                self.matrix1.append(buffer)
                print(buffer,end="")
            self.matrix.append(m)
            print ('')
        #print(self.matrix)
        #print(self.matrix1)


    def add(self,m):
       #"""return a new Matrix object after summation"""
        self.add1 = list(map(lambda x :x[0]+x[1] ,zip([A.matrix1[0],A.matrix1[1],A.matrix1[2]],[B.matrix1[0],B.matrix1[1],B.matrix1[2]])))
        self.add2 = list(map(lambda y :y[0]+y[1] ,zip([A.matrix1[3],A.matrix1[4],A.matrix1[5]],[B.matrix1[3],B.matrix1[4],B.matrix1[5]])))
        self.add3 = list(map(lambda z :z[0]+z[1] ,zip([A.matrix1[6],A.matrix1[7],A.matrix1[8]],[B.matrix1[6],B.matrix1[7],B.matrix1[8]])))
        
    def sub(self, m):
        #"""return a new Matrix object after substraction"""
        self.sub1 = list(map(lambda x :x[0]-x[1] ,zip([A.matrix1[0],A.matrix1[1],A.matrix1[2]],[B.matrix1[0],B.matrix1[1],B.matrix1[2]])))
        self.sub2 = list(map(lambda y :y[0]-y[1] ,zip([A.matrix1[3],A.matrix1[4],A.matrix1[5]],[B.matrix1[3],B.matrix1[4],B.matrix1[5]])))
        self.sub3 = list(map(lambda z :z[0]-z[1] ,zip([A.matrix1[6],A.matrix1[7],A.matrix1[8]],[B.matrix1[6],B.matrix1[7],B.matrix1[8]])))

    def mul(self, m):
        #"""return a new Matrix object after multiplication"""
        self.MUL0 =[ A.matrix1[0]*B.matrix1[0]+ A.matrix1[1]*B.matrix1[3]+ A.matrix1[2]*B.matrix1[6], A.matrix1[0]*B.matrix1[1]+A.matrix1[1]*B.matrix1[4]+ A.matrix1[2]*B.matrix1[7], A.matrix1[0]*B.matrix1[2]+ A.matrix1[1]*B.matrix1[5]+ A.matrix1[2]*B.matrix1[8]]
        self.MUL1 =[ A.matrix1[3]*B.matrix1[0]+ A.matrix1[4]*B.matrix1[3]+ A.matrix1[5]*B.matrix1[6], A.matrix1[3]*B.matrix1[1]+A.matrix1[4]*B.matrix1[4]+ A.matrix1[5]*B.matrix1[7], A.matrix1[3]*B.matrix1[2]+ A.matrix1[4]*B.matrix1[5]+ A.matrix1[5]*B.matrix1[8]]
        self.MUL2 =[ A.matrix1[6]*B.matrix1[0]+ A.matrix1[7]*B.matrix1[3]+ A.matrix1[8]*B.matrix1[6], A.matrix1[6]*B.matrix1[1]+A.matrix1[7]*B.matrix1[4]+ A.matrix1[8]*B.matrix1[7], A.matrix1[6]*B.matrix1[2]+ A.matrix1[7]*B.matrix1[5]+ A.matrix1[8]*B.matrix1[8]]

    def transpose(self,m):
        #"""return a new Matrix object after transpose"""

        self.tran1 =[ A.matrix1[0]*B.matrix1[0]+ A.matrix1[1]*B.matrix1[3]+ A.matrix1[2]*B.matrix1[6], A.matrix1[3]*B.matrix1[0]+ A.matrix1[4]*B.matrix1[3]+ A.matrix1[5]*B.matrix1[6], A.matrix1[6]*B.matrix1[0]+ A.matrix1[7]*B.matrix1[3]+ A.matrix1[8]*B.matrix1[6]]
        self.tran2 =[ A.matrix1[0]*B.matrix1[1]+ A.matrix1[1]*B.matrix1[4]+ A.matrix1[2]*B.matrix1[7], A.matrix1[3]*B.matrix1[1]+ A.matrix1[4]*B.matrix1[4]+ A.matrix1[5]*B.matrix1[7], A.matrix1[6]*B.matrix1[1]+ A.matrix1[7]*B.matrix1[4]+ A.matrix1[8]*B.matrix1[7]]
        self.tran3 =[ A.matrix1[0]*B.matrix1[2]+ A.matrix1[1]*B.matrix1[5]+ A.matrix1[2]*B.matrix1[8], A.matrix1[3]*B.matrix1[2]+ A.matrix1[4]*B.matrix1[5]+ A.matrix1[5]*B.matrix1[8], A.matrix1[6]*B.matrix1[2]+ A.matrix1[7]*B.matrix1[5]+ A.matrix1[8]*B.matrix1[8]]

    def display(self):
        
        print('===','A+B','===')
        print(self.add1)
        print(self.add2)
        print(self.add3)

        print('===','A-B','===')
        print(self.sub1)
        print(self.sub2)
        print(self.sub3)
        
        print('===','A*B','===')
        print(self.MUL0)
        print(self.MUL1)
        print(self.MUL2)

        print('the transpose of A*B')
        print(self.tran1)
        print(self.tran2)
        print(self.tran3)

  
A = Matrix('matrixA',3,3)  
B = Matrix('matrixB',3,3)
C = A.add(B)
D = A.sub(B)
E = A.mul(B)
F = A.transpose(B)
G = A.display()