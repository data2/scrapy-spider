import json

# with open("data/zb_data1.txt") as file:
#     t = eval(file.readline())
#     print(t)
# file.close()
from stats_spider.stats_spider.items import StatsZbSpiderItem

# with open("data/zb_data1.txt", "a") as file:
#     item = StatsZbSpiderItem()
#     item["dbcode"] = "ss"
#     item["id"]="sdf"
#     file.writelines(str(item).replace("\n","") + "\n")
# file.close()

# with open("data/tt.txt") as file:
#     d={}
#     d['aaa']='kkk'
#     dd = json.loads(str(d))
#     json.dump(dd,file)

str = "{\'dbcode\': \'hgjd\', \'id\': \'A0602\', \'isParent\': False, \'name\': \'固定资产投资价格指数_当季（上年同季=100）(-2018)\', \'pid\': \'A06\', \'wdcode\': \'zb\'}"

print(eval(str))
print(eval(str)['id'])


