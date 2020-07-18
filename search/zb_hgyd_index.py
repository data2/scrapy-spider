import jieba.posseg as psg
import jieba
import json
from collections import Counter

import time
all_words = []


with open("../spider/data/zb_hgnd_data_son_zb.txt") as file:
    for line in file:
        print(line)
        zb_json = eval(line)

        list = psg.cut(zb_json['name'])
        count = 0
        for word, flat in list:
            if count > 7:
                break
            if len(word) > 1 and "n" in flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
            if len(word) == 1 and "n" == flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
file.close()


with open("../spider/data/zb_hgjd_data_son_zb.txt") as file:
    for line in file:
        print(line)
        zb_json = eval(line)

        list = psg.cut(zb_json['name'])
        count = 0
        for word, flat in list:
            if count > 7:
                break
            if len(word) > 1 and "n" in flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
            if len(word) == 1 and "n" == flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
file.close()


with open("../spider/data/zb_hgyd_data_son_zb.txt") as file:
    for line in file:
        print(line)
        zb_json = eval(line)

        list = psg.cut(zb_json['name'])
        count = 0
        for word, flat in list:
            if count > 7:
                break
            if len(word) > 1 and "n" in flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
            if len(word) == 1 and "n" == flat:
                print("%s | %s" % (word, flat))
                count = count + 1
                all_words.append(word)
file.close()

print(len(all_words))
words_set = set(all_words)
print(words_set)
print(len(words_set))




for word in words_set:

    time.sleep(2)
    invert_index = dict()
    temp = []
    with open("../spider/data/zb_hgnd_data_son_zb.txt") as file:
        for line in file:
            if word in line:
                zb_json2 = eval(line)
                temp.append(zb_json['id'])
    file.close()

    with open("../spider/data/zb_hgjd_data_son_zb.txt") as file:
        for line in file:
            if word in line:
                zb_json2 = eval(line)
                temp.append(zb_json['id'])
    file.close()

    with open("../spider/data/zb_hgyd_data_son_zb.txt") as file:
        for line in file:
            if word in line:
                zb_json2 = eval(line)
                temp.append(zb_json['id'])
    file.close()

    print(word)
    print(temp)
    invert_index[word] = temp
    with open("data/index.txt", "a") as file:
        file.write(str(invert_index) + "\n")
    file.close()

print(invert_index)
print(len(invert_index))


# docu_set = {'d1': 'i love shanghai',
#             'd2': 'i am from shanghai now i study in tongji university',
#             'd3': 'i am from lanzhou now i study in lanzhou university of science  and  technolgy', }
#
# all_words = []
# for i in docu_set.values():
#     #    cut = jieba.cut(i)
#     cut = i.split()
#     all_words.extend(cut)
#
# set_all_words = set(all_words)
#
# print(set_all_words)
#
# invert_index = dict()
# for b in set_all_words:
#
#     temp = []
#     for j in docu_set.keys():
#
#         field = docu_set[j]
#
#         split_field = field.split()
#
#         if b in split_field:
#             temp.append(j)
#     invert_index[b] = temp
#
# print(invert_index)