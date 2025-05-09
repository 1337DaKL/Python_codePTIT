class Restaurent:
    a = 1
    def __init__ (self , restaurent_name , resturent_type):
        Restaurent.a += 1
        self.restaurent_name = restaurent_name
        self.restaurent_type = resturent_type
    def decscription_restaurent(self):
        return f"Ten cau nha hang la: {self.restaurent_name} Kieu nha hang la: {self.restaurent_type}"
    def open_restaurent(self):
        return "Nha hang dang mo cua! Chuc quy khach ngon mieng"
if __name__ == "__main__":
    nha_hang = Restaurent(input() , input())
    print(nha_hang.decscription_restaurent())
    print(nha_hang.open_restaurent())
    print(nha_hang.a)
    nha = Restaurent("ok" , "ok")
    print(nha.a)
    print(nha.__init__("ok" , "ok"))