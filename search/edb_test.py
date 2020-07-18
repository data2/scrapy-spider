import jieba
import jieba.posseg as psg
import string

# seg_list = jieba.cut("农林牧渔业民间固定资产投资_累计增长")  # 默认是精确模式
# print(",".join(seg_list))
#
# seg_list = jieba.cut_for_search("农林牧渔业民间固定资产投资_累计增长")  # 默认是精确模式
# print(",".join(seg_list))


print([(x.word,x.flag) for x in psg.cut("中西药品及医疗保健用品类商品零售价格指数(上年同月=100)")])

list  = psg.cut("中西药品及医疗保健用品类商品零售价格指数(上年同月=100)")

for word, flat in list:
    if len(word) >= 1 and "n" in flat:
        print("%s | %s" % (word, flat))
