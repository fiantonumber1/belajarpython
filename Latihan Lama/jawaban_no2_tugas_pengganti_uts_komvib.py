import numpy as np
import calfem.core as cfc


Edof = np.array([
    [1,2,5,6],   #element 1
    [1,2,7,8],   #element 2
    [3,4,7,8],   #element 3
    [5,6,7,8],   #element 4
    [5,6,9,10],  #element 5
    [7,8,9,10],  #element 6
    [7,8,11,12], #element 7
    [9,10,11,12], #element 8
])

K = np.matrix(np.zeros((12,12))) # matrix 12 x 12
f = np.matrix(np.zeros((12,1))) # there are 6 node. 1 node has x and y so there are 12 point

E = 10**(7)       # psi -> pound / square inc
A = 1.5           # square inc
ep1 = [E,A]   # element properties element 1
ep2 = [E,A]   # element properties element 2
ep3 = [E,A]   # element properties element 3
ep4 = [E,A]   # element properties element 4
ep5 = [E,A]   # element properties element 5
ep6 = [E,A]   # element properties element 6
ep7 = [E,A]   # element properties element 7
ep8 = [E,A]   # element properties element 8


ex1 = np.array([0., 40])     # element cordinat (x) for element 1
ex2 = np.array([0, 40])    # element cordinat (x) for element 2
ex3 = np.array([0., 40])     # element cordinat (x) for element 3
ex4 = np.array([40, 40])     # element cordinat (x) for element 4
ex5 = np.array([40, 80])     # element cordinat (x) for element 5
ex6 = np.array([80, 40])     # element cordinat (x) for element 6
ex7 = np.array([40, 80])     # element cordinat (x) for element 7
ex8 = np.array([80, 80])     # element cordinat (x) for element 8

ey1 = np.array([0., 0.])      # element cordinat (y) for element 1
ey2 = np.array([0., 40])     # element cordinat (y) for element 2
ey3 = np.array([40, 40])     # element cordinat (y) for element 3
ey4 = np.array([0., 40])     # element cordinat (y) for element 4
ey5 = np.array([0., 0.])     # element cordinat (y) for element 5
ey6 = np.array([40, 0.])     # element cordinat (y) for element 6
ey7 = np.array([40, 40])     # element cordinat (y) for element 7
ey8 = np.array([0, 40])     # element cordinat (y) for element 8



Ke1 = cfc.bar2e(ex1,ey1,ep1) #Element stiffness matrices for element 1
Ke2 = cfc.bar2e(ex2,ey2,ep2) #Element stiffness matrices for element 2
Ke3 = cfc.bar2e(ex3,ey3,ep3) #Element stiffness matrices for element 3
Ke4 = cfc.bar2e(ex4,ey4,ep4) #Element stiffness matrices for element 4
Ke5 = cfc.bar2e(ex5,ey5,ep5) #Element stiffness matrices for element 5
Ke6 = cfc.bar2e(ex6,ey6,ep6) #Element stiffness matrices for element 6
Ke7 = cfc.bar2e(ex7,ey7,ep7) #Element stiffness matrices for element 7
Ke8 = cfc.bar2e(ex8,ey8,ep8) #Element stiffness matrices for element 8


cfc.assem(Edof[0,:],K,Ke1)   #Assemble Ke1 into K
cfc.assem(Edof[1,:],K,Ke2)   #Assemble Ke2 into K
cfc.assem(Edof[2,:],K,Ke3)   #Assemble Ke3 into K
cfc.assem(Edof[3,:],K,Ke4)   #Assemble Ke4 into K
cfc.assem(Edof[4,:],K,Ke5)   #Assemble Ke5 into K
cfc.assem(Edof[5,:],K,Ke6)   #Assemble Ke6 into K
cfc.assem(Edof[6,:],K,Ke7)   #Assemble Ke7 into K
cfc.assem(Edof[7,:],K,Ke8)   #Assemble Ke8 into K

print("Stiffness matrix K:")
print(K)


bc = np.array([1,2,3,4]) ## there is no effect about displacement for 4 node
f[5] = -2000    #force input in U6
f[8] =  2000    #force input in U9
f[10] = 4000    #force input in U11
f[11] = 6000    #force input in U12

a, r = cfc.solveq(K,f,bc)

print("Displacements a:")
print(a)

print("Reaction forces r:")
print(r)

ed1 = cfc.extractEldisp(Edof[0,:],a);
N1 = cfc.bar2s(ex1,ey1,ep1,ed1)
ed2 = cfc.extractEldisp(Edof[1,:],a);
N2 = cfc.bar2s(ex2,ey2,ep2,ed2)
ed3 = cfc.extractEldisp(Edof[2,:],a);
N3 = cfc.bar2s(ex3,ey3,ep3,ed3)
ed4 = cfc.extractEldisp(Edof[3,:],a);
N4 = cfc.bar2s(ex4,ey4,ep4,ed4)
ed5 = cfc.extractEldisp(Edof[4,:],a);
N5 = cfc.bar2s(ex5,ey5,ep5,ed5)
ed6 = cfc.extractEldisp(Edof[5,:],a);
N6 = cfc.bar2s(ex6,ey6,ep6,ed6)
ed7 = cfc.extractEldisp(Edof[6,:],a);
N7 = cfc.bar2s(ex7,ey7,ep7,ed7)
ed8 = cfc.extractEldisp(Edof[7,:],a);
N8 = cfc.bar2s(ex8,ey8,ep8,ed8)

print("N1=",N1) #Element forces in element 1
print("N2=",N2) #Element forces in element 2
print("N3=",N3) #Element forces in element 3
print("N4=",N4) #Element forces in element 4
print("N5=",N5) #Element forces in element 5
print("N6=",N6) #Element forces in element 6
print("N7=",N7) #Element forces in element 7
print("N8=",N8) #Element forces in element 8