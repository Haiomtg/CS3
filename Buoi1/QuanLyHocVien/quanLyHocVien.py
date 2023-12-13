from hocvien import HocVien

listHocVien = [
    {
        "maHV" : "1",
        "tenHV" : "Nguyen Van A",
        "ngaySinh" : "13/05/2007",
        "listKhoaHoc" : {
            "BackEnd"
        }
    },
    {
        "maHV" : "2",
        "tenHV" : "Nguyen Van B",
        "ngaySinh" : "15/07/2007",
        "listKhoaHoc" : {
            "FrontEnd"
        }
    }
]

listKhoaHoc = [
    {
        "maKhoaHoc" : "001", 
        "tenKhoaHoc" : "FrontEnd",
        "hinhThuc" : "online", 
        "hocPhi" : "80000000"
    },
    {
        "maKhoaHoc" : "002", 
        "tenKhoaHoc" : "BackEnd",
        "hinhThuc" : "online", 
        "hocPhi" : "30000000"
    }
]

def themHocVien():
    flag = True
    maHV = input("Nhap ma Hoc Vien")
    tenHV = input("Nhap ten hoc vien: ")
    ngaySinh = input("Nhap ngay sinh dd/mm/yyyy: ")
    listKH = []
    while flag:
        khoaHoc = input("Nhap ten khoa hoc: ")
        for kHoc in listKhoaHoc:
            if khoaHoc == kHoc["tenKhoaHoc"]:
                flag = False
                listKH.append(khoaHoc)
            else:
                print("Khong tim thay khoa hoc")
    hv = HocVien(maHV, tenHV, ngaySinh, listKH)
        
def dangKiKhoaHocChoHocVien(tenHV):
    for hv in listHocVien:
        if tenHV == hv["tenHV"]:
            khoaHoc = input("Nhap ten khoa hoc: ")
            for kHoc in listKhoaHoc:
                if khoaHoc == kHoc["tenKhoaHoc"]:
                    hv["listKhoaHoc"]+= khoaHoc
                    break


while True:
    print("Quan Ly Hoc Vien Cua Trung Tam:")
    print("Nhap 1: De them hoc vien")
    print("Nhap 2: De dang ky khoa hoc cho Hoc Vien")
    print("Nhap 3: De in thong tin hoc vien")
    print("Nhap 4: De them khoa hoc")
    select = input("Nhap lua chon cua ban")
    match select:
        case "1":
            listHocVien += themHocVien()
        case "2":
            khoaHoc = input("Nhap ten khoa hoc dang ky cho sinh vien: ")
            dangKiKhoaHocChoHocVien(khoaHoc)

