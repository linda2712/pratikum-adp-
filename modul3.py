#input jumalah partisi
n=int(input("masukkan jumlah partisi n="))

#batas atas dan batas bawah
a=1 #batas bawah
b=3 #batas atas

#menghitung deltas x
delta_x=(b-a)/n
luas_daerah=0

for i in range(n):
    x = a+i*delta_x #rumus mencari nilai x
    fungsi=x**2 +2*x
    luas_daerah += fungsi * delta_x #rumus mencari luas daerah
#hasilnya    
print ("Luas Daerah dari fungsi x**2 +2*x dengan batas daerah x=1 dan x=3 dan jumlah partisi n = ",n," adalah ",luas_daerah)
