products = ["cat", "banana", "obama", "car", "cow", "alibaba"]

def timTuCanNhap(wordList, words):
    for i in wordList:
        if words in i:
            print(i)

tuCanTim = input("Nhap tu can tim")
timTuCanNhap(products, tuCanTim)