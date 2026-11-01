class book:
    def __init__(self, title, writer, year):
        self.title=title
        self.writer=writer
        self.year=year
        self.oduncmu= False
    def odüncver(self):
        self.oduncmu=True
    def iadeet(self):
        self.oduncmu=False
    def __str__(self):
        if self.oduncmu==True:
           x= ("ödünçte")
        else:
           x= ("rafta")
        return f"{self.title} -{self.writer} ({self.year}) {x}"              
class library:
    def __init__(self):
        self.books=[]
    def addbook(self,book):
        self.books.append(book)  
    def bookfind(self, title):
        for i in self.books:
            if i.title.lower()==title.lower():
                return i
        return None
    def search(self,word):
        result=[]
        for i in self.books:
            if word.lower() in i.title.lower():
                result.append(i)    
        return result
    def oduncver(self, title):
        book=self.bookfind(title)
        if book:
         book.odüncver()
         print(f"{book.title} ödünç verildi")
        else:
            print("book not found") 
    def iadeal(self, title):
        book=self.bookfind(title)
        if book:
            book.iadeet()
            print(f"{book.title} iade alindi")
        else:
            print("book not found")            
    def listele(self):
        if not self.books:
            print("kütüphane de kitap yok")
        for b in self.books:
            print(b)
lib= library()
while True:
    print("1. kitap ekle")
    print("2. kitaplari listele")
    print("3. ödünçver")
    print("4. iade al")
    print("5. kitap ara")
    print("6. exit")
    secim= input("seçiminiz ")
    if secim=="1":
        title=input("kitap adi ")
        writer=input(" yazar ")
        year=input("basim yili")
        yenikitap=book(title, writer, year)
        lib.addbook(yenikitap)
        print("kitap eklendi")
    elif secim=="2":
        lib.listele()
    elif secim=="3":
        title=input("ödünç verilecek kitap")
        lib.oduncver(title)
    elif secim=="4":
        title=input("iade alinacak kitap adi") 
        lib.iadeal(title)
    elif secim=="5":
        word=input("aranacak kelime")
        sonuclar=lib.search(word)
        if sonuclar:
            for k in sonuclar:
                print(k)
        else:
            print("kitap bulunamadi")
    elif secim=="6":
        print("exit")
    else:
        print("yanliş seçim")                                              













