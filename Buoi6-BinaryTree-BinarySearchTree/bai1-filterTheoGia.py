iphoneList = [{"price": 3000, "name" : "iphon12"},
              {"price": 4000, "name" : "iphon13"}, {"price": 5000, "name" : "iphon14"},
              {"price": 1000, "name" : "iphon11"}]

def filterTheoGia(giaNho, giaLon):
    print("Danh sach dien thoai tu", giaNho, "den", giaLon)
    for i in iphoneList:
        if i["price"] >= giaNho and i["price"] <= giaLon:
            print(i["name"])
giaNho = int(input("Nhap so nho: "))
giaLon = int(input("Nhap so lon: "))
filterTheoGia(giaNho, giaLon)