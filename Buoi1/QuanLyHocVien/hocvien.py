from khoahoc import KhoaHoc

class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, listKhoaHoc):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.listKhoaHoc = listKhoaHoc

    def dangKyKhoaHoc(self, khoaHoc):
        self.listKhoaHoc.append(khoaHoc)

    def hienThiThongTinHocSinh(self):
        print("Ma Hoc Vien:   ", self.maHV)
        print("Ten Hoc Vien:  ", self.tenHV)
        print("Ngay Sinh:     ", self.ngaySinh)
        print("Nhung khoa hoc dang ky")
        for khoaHoc in self.listKhoaHoc:
            khoaHoc = KhoaHoc()
            KhoaHoc.thongTinKhoaHoc
            print("----------------------------------------")
    

