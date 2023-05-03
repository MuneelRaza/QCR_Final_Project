import csv
import numpy as np
import operator
from sklearn.preprocessing import normalize
with open("Gapminder_clean.csv", "r", encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    gapminder = []
    for sublist in reader:
        gapminder.append(sublist)
gapminder = np.array(gapminder)
gapminder = gapminder[:, [0, 2, 8, 10, 12, 13, 15, 18, 42]]
arr_con = gapminder[:, 0]
arr_uni = np.unique(arr_con)
gapminder_N = gapminder[1:3578, 1:9]
list1 = []
for sub_list in gapminder_N:
    list1.append(sub_list.astype('float'))

list1 = normalize(list1, axis=0, norm='max')
arr_uni = np.delete(arr_uni, 48)
dict = {}
key = arr_uni
for j in range(8):
    col = list1[:, j]
    for i in range(len(arr_uni)):
        index = np.where(arr_con == arr_uni[i])
        index = index[0]
        index = index - 1
        value = np.take(col, index)
        mean = np.mean(value)
        dict.setdefault(arr_uni[i],[])
        keys = dict[arr_uni[i]]
        keys.append(mean)
dict_final = {}
for m in range(len(arr_uni)):
    key2 = dict[arr_uni[m]]
    f_sum = np.sum(key2)
    dict_final.setdefault(arr_uni[m], f_sum)
sort = sorted(dict_final.items(), key=operator.itemgetter(1), reverse=True)
print(sort)
sort1 = np.array(sort)
c = np.where(sort1 == "Pakistan")
print("Pakistan Ranked", c[0], "out of 227 countries")

rank = 0
with open("Rank.csv", "w", newline="") as file2:
    fieldnames = ["Ranking","Country with its value"]
    thewriter = csv.DictWriter(file2, fieldnames=fieldnames)
    thewriter.writeheader()
    for country in sort:
        rank = rank + 1
        thewriter.writerow({"Ranking": rank, "Country with its value": country})
