

def selamla():

	print("merhaba")
	print("nasılsınız")
	
def selamla2(isim):
		print("isminiz: ", isim)
		
		
def toplama(a,b,c):
	print("toplamları ",a+b+c)
	

def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)	