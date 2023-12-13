# Hãy xây dựng một list sinh viên với các thuộc tính sau: mã sinh viên, tên sinh viên, điểm toán, điểm văn, điểm hóa.

# + Tạo list gồm 5 sinh viên

# + In thông tin các sinh viên có điểm trung bình lớn hơn 5

# + In ra các sinh viên có điểm hoá dưới 5

# Điền đường link nộp bài tập tại ô này:
def tinhDTB(toan, van, hoa):
    if((toan + van + hoa)/3 >= 5):
        return True
    else:
        return False

listSinhVien = [
    {
        "msv" : 1,
        "tenSV" : "Nguyen Van A",
        "diemToan" : 6,
        "diemVan" : 7,
        "diemHoa" : 8
    },
    {
        "msv" : 2,
        "tenSV" : "Nguyen Van B",
        "diemToan" : 6,
        "diemVan" : 7,
        "diemHoa" : 7
    },
    {
        "msv" : 3,
        "tenSV" : "Nguyen Van C",
        "diemToan" : 8,
        "diemVan" : 7,
        "diemHoa" : 8
    },
    {
        "msv" : 4,
        "tenSV" : "Nguyen Van D",
        "diemToan" : 4,
        "diemVan" : 5,
        "diemHoa" : 5
    },
    {
        "msv" : 5,
        "tenSV" : "Nguyen Van E",
        "diemToan" : 6,
        "diemVan" : 7,
        "diemHoa" : 5
    }
]



listSVtrenNam = []
listSVduoiNam = []

for sv in listSinhVien:
    toan = sv["diemToan"]
    van = sv["diemVan"]
    hoa = sv["diemHoa"]
    if(tinhDTB(toan, van, hoa)):
        listSVtrenNam.append(sv["tenSV"])
    else:
        listSVduoiNam.append(sv["tenSV"])

print("Sinh Vien co diem trung binh tren 5:")
for sv in listSVtrenNam:
    print(sv)

print("Sinh Vien co diem trung binh duoi 5:")
for sv in listSVduoiNam:
    print(sv)

