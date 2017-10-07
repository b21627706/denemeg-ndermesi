b=3.14
int(b)		#burada sadece 3 kısmı cıkar


len(str(3.14))	#burada 3.14 u stringe çevirdik ve uzunlugunu aldık 4 cıktı 
				#cunku nokta da bır strıng degerı sayılıyor
				
print(35,45,3.14,"sayı")	#burada bastırmak istediğimiz seyleri virgül
							#virgül ile ayırarak bastırabiliriz 
							
							
print(3,5,8,"sayı",3.14,sep="/")	'''burada bastırmak istedigimiz seyler arasına
									istedigimiz karakteri koymak için sep parametresi kulllanılır'''
									
									
print(*"fatih")	#burada fatih kelimesini birer satır bosluk bırakarak yazar 

print(*"fatih", sep ="/")	#burada fatih kelimesini birer satır bosluk bırakarak yazar 
							#ve aralarına / işaretini koyar
							
							
							
							
							
a=5
b=8

print("{}+ {}= {}".format(a,b,a+b))		'''burada format fonksıyonu bır strıngı bıcımlendırme 

yontemidir suslu parantezler ile yazılır ve .format denılerek parantezler içine yazılacak seyler 
sırasıyla yazılır '''