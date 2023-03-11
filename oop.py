class Animals:
    def __init__(self,name,type,habitat):
        self.myname=name
        self.mytype=type
        self.myhabitat=habitat
    def lesson(self):
     print("This is a "+self.myname+" it is a "+self.mytype+" it lives in/on "+self.myhabitat)

class Cow(Animals):
    def __init__(self,name,type,habitat,birth_date):
        super().__init__(name,type,habitat)
        self.mybirthday=birth_date
        self.mytype=type
        self.myhabitat=habitat
    def lesson(self):
        super().lesson()
        print("It is a "+self.mytype+" it lives on"+self.myhabitat)

myname=Cow("Ng'ombe","mammal","land,","17/03/2022")
myname.lesson()