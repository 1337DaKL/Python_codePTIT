def demThuong(string):
    dem = 0
    for i in range(0 , len(string) , 1) :
        if(string[i].islower()) :
            dem += 1
    return  dem
def demChan(string):
    dem = 0
    for i in range(0 , len(string) , 1) :
        if(string[i].isupper()) :
            dem += 1
    return  dem

if __name__ == "__main__":
    s = input()
    if(demChan(s) > demThuong(s)) :
        print(s.upper())
    else:
        print(s.lower())