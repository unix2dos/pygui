import json
import re

import requests
from pyquery import PyQuery as pq


class Goods:
    def __init__(self, id):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.id = id
        self.area_id = "1_72_2799_0"

    # 获取价格
    def price(self):
        url = 'http://p.3.cn/prices/mgets'
        payload = {
            'type': 1,
            'skuIds': 'J_' + self.id,
        }
        price = 0
        try:
            response = requests.get(url, params=payload)
            resp_txt = response.text.strip()
            json_dict = json.loads(resp_txt[1:-1])
            price = json_dict['p']
        except Exception as e:
            pass
        return float(price)

    # 获取所有的促销信息
    def promotion(self):
        cat = self.__cat(f"https://item.jd.com/{self.id}.html")
        url = f"https://cd.jd.com/promotion/v2?skuId={self.id}&area={self.area_id}&cat={cat}"
        sess = requests.Session()
        res = sess.get(url=url, headers=self.headers)
        json_dict = json.loads(res.text)
        datas = {}
        for x in json_dict["prom"]["pickOneTag"]:

            # code 15 满减, 16 满赠, 19 打折, 36 更复杂打折, 60 换购
            # # 垃圾活动类型滚一边去
            # if x["code"] == "60":
            #     continue

            # 活动预告滚一边去
            if x["name"] == "活动预告":
                continue

            # 打折力度低的滚一边去
            t1 = re.findall("总价打(\w*.?\w*)折", x["content"])
            low = True
            if len(t1) > 0:
                low = False
                for tt1 in t1:
                    if float(tt1) < 7:
                        low = True
                        break
            if not low:
                continue

            # 返回促销信息
            one_data = {
                "code": x["code"],
                "content": x["content"],
                "name": x["name"],
            }
            datas[x["d"]] = one_data

        return datas

    # 获取分类信息
    def __cat(self, url):
        sess = requests.Session()
        res = sess.get(url=url, headers=self.headers)
        doc = pq(res.text)
        href = doc.find("#parameter-brand").find("a").attr("href")
        try:
            b = href.index("?cat=")
            e = href.index('&ev=')
            return href[b + 5:e]
        except Exception as e:
            print(f"get cat err: {e}")
            return ""


if __name__ == "__main__":
    # "https://item.jd.com/100002820036.html"
    # c = Goods("100002820036")
    # print(c.is_promotion())
    c = Goods("11038861478")
    print(c.promotion())
    c = Goods("39923667889")
    print(c.promotion())
