# mengonversi string ke dalam array.array

import array
B = array.array('c')
B.fromstring("Python")
B
for karakter in B:
    print("%c " % karakter, end='')