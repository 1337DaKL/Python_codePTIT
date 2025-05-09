def chuyen_sang_phut(time: str) -> int:
    h , m = time.split(":")
    return int(h) * 60 + int(m)
class TramMua:
    def __init__(self , name : str , start : str , end : str , water : int):
        self.name = name
        self.water = water
        self.time = chuyen_sang_phut(end) - chuyen_sang_phut(start)
if __name__ == "__main__":
    dict_tram_mua = dict()
    t = int(input())
    id = 1
    for _ in range(t):
        tram_mua = TramMua(input() , input() , input() , int(input()))
        if dict_tram_mua.get(tram_mua.name) == None:
            tram_mua.code = "T" + str(id).zfill(2)
            id += 1
            dict_tram_mua[tram_mua.name] = tram_mua
        else:
            dict_tram_mua[tram_mua.name].time += tram_mua.time
            dict_tram_mua[tram_mua.name].water += tram_mua.water
    for item in dict_tram_mua.values():
        print("{} {} {:.2f}".format(item.code , item.name , item.water / (item.time / 60) ))