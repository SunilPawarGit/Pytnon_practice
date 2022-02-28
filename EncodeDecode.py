class EnChar():
    def __init__(self,chara) -> None:
        self.rev=0
        self.dig=0
        self.actnum=0
        self.chara=chara
        for ch in self.chara:
            if(ord(ch) <= ord('Z')):
                self.actnum =self.actnum +(26-(ord('Z')-ord(ch)))
            if(ord(ch) >= ord('a')):
                self.actnum =self.actnum +(26-(ord('z')-ord(ch)))
        while(int(self.actnum) > 0):
            self.dig= int(self.actnum%10)
            self.rev= self.dig+(self.rev * 10)
            self.actnum/=10
        print(self.rev)
ent=input("Enter String :")
obj = EnChar(ent)