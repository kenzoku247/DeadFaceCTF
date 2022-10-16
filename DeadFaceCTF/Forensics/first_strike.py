p = 1049
q = 2063
n = q * p
e = 777887

def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;

    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers; 

def phiN(list,n):
    phi = 1
    for i in list:
        phi = phi * (i-1) / i 
    return int(phi*n)
def timD(phi,e):
    for i in range(1,phi):
        if((i*e)%phi) == 1:
            return i

#listNumbers = phanTichSoNguyen(n);

#def Tim_TSNT(n):

#print(phiN(phanTichSoNguyen(n),n))

print(timD(phiN(phanTichSoNguyen(n),n),e))
