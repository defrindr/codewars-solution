#sum sequence
import time
awal=time.time()
def hitung(a,b,c):
	r = []
	while a <= b:
		r.append(a)
		a+=c
	print sum(r)

hitung(1,1000000,3)
akhir=time.time()

print "kecepatan : "+str(akhir-awal)