class  A :  pass

class B(A) :  pass

class  C(A): pass

class  D(C,B):pass

print("mro of a class", A.mro())
print("mro of b class", B.mro())
print("mro of C class", C.mro())
print("mro of d class",D.mro())
