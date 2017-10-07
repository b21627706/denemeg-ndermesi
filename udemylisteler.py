liste1 =  [1,2,3,4,5]
liste2 =  [6,7,8,9,10]
liste1 + liste2	#listeleri birlestiriyoruz

liste=list("merhaba")	#burada merhaba kelimesinin harfleriyle liste olusturduk

liste1*3	#liste1 i 3 defa bastırıyoruz
			#ama orjınal liste1 i degistirmiyoruz
			
liste1[:2]	


liste1.pop()	#listenin son elemanını atar

liste1.pop(1)	#1. indexteki elemanı atar

liste1.sort()	#listedeki elemanları kucukten buyuge  sıralar

liste1.sort(reverse=True)	#listedeki elemanları buyukten kucuge sıralar
			





s =  "Merhaba"
lst =  list(s)
print(lst)