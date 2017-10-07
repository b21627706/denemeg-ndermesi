# Döngüde i değerlerini ekrana yazdırma

i = 0 

while (i < 10):
    print("i'nin değeri",i)
    i += 1 
	# Koşulun bir süre sonra False olması için gerekli - Unutmayalım
	
# Bu kodu çaıştırmayalım. Jupyter sıkıntı çıkarabilir :)
i = 0 
#while (i < 10):
    #print(i)
    # i değişkenini artırma işlemi yapmadığımız için i değişkeninin değeri sürekli 0 kalıyor 
    # ve döngü koşulu sürekli True kalıyor.	
	

# Liste üzerinde indeks ile gezinme
liste = [1,2,3,4,5]

a = 0 

while (a < len(liste)):
    print("Indeks:",a,"Eleman:",liste[a])
    a +=1	