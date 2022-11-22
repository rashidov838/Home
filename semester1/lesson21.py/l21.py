class Marker:
    def __init__(self,company,color,price):
        self.company=company
        self.color=color
        self.price=price

marker1=Marker("Marker inc", "Red", 123)

marker2=Marker("Polo inc", "Black", 543)

marker3=Marker("LAcoste inc", "White", 456)

print(marker2.company,marker2.color,marker2.price,sep="\t") 

print(marker1.company,marker1.color,marker1.price,sep="\t")
 
print(marker3.company,marker3.color,marker3.price,sep="\t") 