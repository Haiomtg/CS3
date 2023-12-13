class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def hienThongTinKhoaHoc(self):
        print("Ma Khoa Hoc :  ", self.maKhoaHoc)
        print("Ten Khoa Hoc : ", self.tenKhoaHoc)
        print("Hinh Thuc :    ", self.hinhThuc)
        print("Hoc Phi :      ", self.hocPhi)
        print("------------------------------")