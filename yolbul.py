import sys # komut satırından ifade alınması için gerekli kütüphanedir.
##Labirentin matris formatında listeye eklenmesi kısmıdır
def MAZEdosyaOku(MAZE): 
    dosya=open(sys.argv[1],"r") #labirentin olduğu dosya uzantısının komut satırından alınması ve dosyanın açılması işlemi
    for satir in dosya: #dosya satır satır okunur
        gecici=[] #satır içerikleri için boş liste oluşturulur.
        for i in range(len(satir)): 
            gecici.append(satir[i]) #bütün satır geçici listeye eklenir.
        if "\n" in gecici: # gecici içinde \n kodu varsa
            gecici.remove("\n") ##\n silinir.
        MAZE.append(gecici)       #Labirent listesi içine geçici listesi eklenir.
    dosya.close() #dosya kapatılır.
#Labirent çözümünün metin dosyasına yazdırılması işlemi bu bölümde yapılmaktadır.
def MAZEdosyaYaz(cozumYolu): 
    dosya=open(sys.argv[2],"w") #Komut satırı üzerinden çıktının dosya adı alma işlemi
    duraklar=["S","F","H"] # Oluşturulacak çıktıda başlangıç bitiş vb değerleri listeye alınır. bkz: line 20,25
    for x in range(0,len(MAZE)): #Labirentin [x]
        for y in range(0,len(MAZE[0])): #[y] kordinatları gezilerek
            if MAZE[x][y] not in duraklar: # Duraklar haricindeki tüm noktalar;
                MAZE[x][y]=0       #sıfır değeri alır.
    for i in cozumYolu: #Labirentin liste halindeki çözümü for döngüsü ile açılır;
        xy=i.split(',') # virgül baz alınarak string ifadedeki kordinat:
        if MAZE[int(xy[0])][int(xy[1])] not in duraklar: #Durakların isminin değişmemesi için duraklar dışındaki çözüm adımlar;
            MAZE[int(xy[0])][int(xy[1])]=1 # 1 değeri alır
    for i in range(len(MAZE)): #Labirentin artık dosyaya yazdırılma işlemi başlamıştır:
        for j in range(len(MAZE[0])): #İki boyutlu listelerde x,y çiftini bu şekilde iki for ile alırız:
            dosya.write(str(MAZE[i][j])+" ") #String ifadeye çevrilip satır satır yazma işlemi
            print(f"{str(MAZE[i][j])} ",end="") # Çözüm yolu aynı zamanda ekrana yazdırılır.
        print("")
        dosya.write("\n")   #Her satırdan sonra alt satıra geçmek için bir enter atılır.
#Burdaki amaç oluşturulan Labirentin komşuları buldurularak dictionary kullanarak ağırlıksız graf yapısı oluşturulmasıdır.
def MAZEtoGraph():
    x=0 #x,y değerleri Labirentin komşularının bulunmasında fayda sağlayacaktır.
    y=0
    noktalar=["P","S","F","H"]   ##Labirentte komşularının bulunacağı noktalar bunlardır.
    for i in MAZE:   #Labirent listesi döngü ile açılır
        y=0 #y sıfırlandı
        for j in i: #teker teker tüm noktalar gezdirilir.
            komsuluk=[] #komsuların tutulacağı listedir.       
            if j in noktalar: # noktalar listesinin her hangi eleman j de varsa
                if j in noktalar and j!="P": # S,F,H kontrol
                    MAZEsetup.append([j,str(x)+","+str(y)]) #S,F,H değerlerinin kordinatları eklenir
                if x+1!=len(MAZE) and MAZE[x+1][y] in  noktalar: #yukarı çıkılabiliyor ve mevcut konum için komşu ise
                    komsuluk.append(str(x+1)+","+str(y))       #komşuluk listesine eklenir
                if x-1!=-1 and MAZE[x-1][y] in noktalar: #aşağı inilebiliyor ve mevcut konum için komşu ise
                    komsuluk.append(str(x-1)+","+str(y))        #komşuluk listesine eklenir
                if y+1!=len(MAZE[0]) and MAZE[x][y+1] in noktalar: #sağa gidilebiliyor ve mevcut konum için komşu ise
                    komsuluk.append(str(x)+","+str(y+1))        #komşuluk listesine eklenir
                if y-1!=-1 and MAZE[x][y-1] in noktalar: #sola gidilebiliyor ve mevcut konum için komşu ise
                    komsuluk.append(str(x)+","+str(y-1)) #komşuluk listesine eklenir
                MAZEgraph[f"{x},{y}"]=komsuluk      #hiç bir durum kalmadığında key(mevcut konum)=komsular şeklinde sözlüğe eklenir.
            y+=1 #y 1 artırılır
        x+=1 #x 1 artırılır
    MAZEsetup.sort(reverse=True) #s,h,f sıralaması bozulmaması için gerekli olan sıralamadır.   
#Tüm komşuların graf yapısından okunarak karşılaştırıldığı daha sonra uygun çözümün bir listeye eklenip rekursif yapıda çalışan fonksiyondur.
def MAZEyolBul(S, F, yol = []):
    yol = yol + [S] ## Yol listesine başlangıç değeri eklenir.
    if S == F: ##Başlangıç ve Bitiş değerleri aynı olduğında;
        return yol ##Oluşan yol listesi return edilir
    enKisaYol = [] #Karşılaştırma yapılabilmesi için boş liste oluşturulur
    for komsu in MAZEgraph[S]: #okunan keyin valuesinde komşular okunur
        if komsu not in yol: #komşu değeri yolda ekli değilse;
            yeniYollar = MAZEyolBul(komsu, F , yol) ##yeniYollar listesine rekursif yapıdaki liste döndüren fonksiyon çağırılır ve:
            if yeniYollar != None: #yeniYollar boş değilse :
                if not enKisaYol or len(yeniYollar) < len(enKisaYol): #yeniyollar listesinin uzunluğu enkisayol listesinden küçükse :
                    if MAZEsetup[1][1] in yeniYollar: #aynı zamanda H güçlü girdisi içide ise:
                        enKisaYol = yeniYollar #enkisayol listesi güncellenir
    return enKisaYol #enKisayol listesi return edilir
##MAIN KISMI:
MAZE=[] #boş labirent listesi oluşturulur.
MAZEgraph={} #boş sözlük oluşturulur
MAZEsetup=[] #başlangıç,bitiş,Güçlendirme Hücre kordinatlarının tutulduğu listedir.
MAZEdosyaOku(MAZE) #İstenen labirent okutulur
MAZEtoGraph() #Labirentin grafı oluşturulur
print("Başlangıç Bitiş Güçlendirme Hücre Noktaları : ",MAZEsetup,"\n")
if(MAZEsetup[1][0]=="H"): ##Güçlendirilmiş Hücre ise ,başlangıç,bitiş hedef değerleri 
    cozumYolu=MAZEyolBul(MAZEsetup[0][1], MAZEsetup[2][1]) #H ise
else:
    cozumYolu=MAZEyolBul(MAZEsetup[0][1], MAZEsetup[1][1]) #klasik ise
MAZEdosyaYaz(cozumYolu) ##Çözüm hem ekrana hemde istenilen metin dosyasına yazdırılır.