# list內的資料可變動，tuple內的資料不可變動
# grades = [60, 50, 70, 100, 30]
# print(grades)
# print(len(grades))
# print(grades[0:2])
# grades[0:2] = []  # 連續刪除
# print(grades)
# print(len(grades))

# data = [[1, 2, 3], [4, 5, 6]]
# print(data)  # 2
# data[0][0:2] = [1, 1, 1, 1]
# print(data)  #

data = (1, 2, 3)
# data[0] = 5  # 會報錯 tuple內資料不可變動
