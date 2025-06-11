def a(angka):
    for i in range(len(angka)-1,0,-1):
        pos_max = 0
        for x in range(1,i+1):
            max_sementara = angka[pos_max]
            if max_sementara < angka[x]:
                pos_max = x
        angka[pos_max],angka[i], = angka[i],angka[pos_max]
angka = [5,6,3,4,87,3,0,7]
a(angka)
print(angka)