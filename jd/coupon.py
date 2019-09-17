from http.cookies import SimpleCookie

import requests
from pyquery import PyQuery


class Coupon:
    def __init__(self, id):
        self.cookie = "__jdu=1438956430; shshshfpa=d804ae50-6118-1194-8757-3641e3263b66-1567907475; shshshfpb=woPJUoIUyRUqbrI%20ZmsC8pA%3D%3D; ipLocation=%u5317%u4eac; areaId=1; unpl=V2_ZzNtbRVQQEJ3Ck4Gfh1dAWIKG18RUUoQfV9DAy8ZCQVlCxpaclRCFX0UR1xnGVgUZwEZXEZcRhZFCEdkexhdBGYKGlRKVXMVcQ8oVRUZVQAJbRoPQAJBEiBcRQB%2bHgwMZ1YibUFXcxRFCENWchFYAmIBE21yV0sRRTiR%2fdXP0KOzuriK8NVzEXMLQFB6GF0GVwIiXHIcLRQ4CENWchFYAmIBE21DZ0A%3d; ipLoc-djd=1-2901-4135-0.138323916; __jdv=76161171|www.baidu.com|-|referral|-|1570930988964; PCSYCityID=CN_110000_110100_110105; user-key=e4c0d4d7-91bd-49b2-9efa-c8b9e73be1a6; cn=50; shshshfp=82aa44952e73625ea9d7820607b34685; shshshsID=6ae265f5892f39cb14be48c8284760cb_11_1570933178390; __jda=122270672.1438956430.1567696527.1568733259.1570930989.33; __jdc=122270672; 3AB9D23F7A4B3C9B=MTUEJWMMSIBU36ADDCZVXZ5HHEU5HW6RV4OCL3RFJXFECHLGYWCXJWGRQRKTLK35S7LVJTUFMM3A2HHSM5IJTKULDU; mt_xid=V2_52007VwMXUFRQVl0aSxhsVTNURVVZDVBGFkocWxliCkcCQVBTXxZVGQ8FNwYSWwoLBQoZeRpdBW8fElNBWFBLH0gSXwRsAxZiXWhSahZMHloNYgMSVlxZVF0aSx5dAGIzEFZcXQ%3D%3D; wlfstk_smdl=ysfpxq7fk3jt6g3psz33dgnh8d3b2dy1; TrackID=1-mivsT3iirU0PvaLkNm3vGh2PIAgRe0vRulSU9pBAADVEo8KlvCesa_YL7KGI_tgZ2_209Dy4G80RwjNtnCFpMzWStkJG0Z5jzQuw1ioAveqRbq6g7hY2Oorh_7JaN7q; thor=B3EA00155896A0E4AF1B74B851513507BDE74CBD037AC0686E2A85290D7B6A4CA5A263EFC0B8CA4064F94DFC2E5F2C10C7B41D811D99D40D75A4A9C565155937A35B9EE773FC35CB6685A447380C30180FE30F5FFE6246679646B5388BAF8F0608ADEB0AC4502C274647B1DBC82684C52303154F515A018C43C252CCD3A57B678231FA3A6CC8D02B33F349D279E42CED; pinId=s4sOjqXN9XK-v_3guy9wFg; pin=18311374266_p; unick=xuanyuanting; ceshi3.com=103; _tp=b1MP0CnKRT3uCp%2Faspq1Iw%3D%3D; _pst=18311374266_p; __jdb=122270672.50.1438956430|33.1570930989"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.id = id
        self.url = f"https://search.jd.com/Search?coupon_batch={id}&psort=2"

    def get_cookie_dict(self):
        cookie = SimpleCookie()
        cookie.load(self.cookie)
        cookies = {}
        for key, morsel in cookie.items():
            cookies[key] = morsel.value
        return cookies

    # 获取优惠券的所有商品
    def GetGoods(self):
        sess = requests.Session()
        sess.cookies = requests.utils.cookiejar_from_dict(self.get_cookie_dict())

        # 优惠券商品有很多页, 通过没有数据返回退出
        i = 1
        while True:
            newurl = '{}&page={}&scrolling=y'.format(self.url, i)
            print(newurl)
            res = sess.get(url=newurl, headers=self.headers)
            res.encoding = 'utf-8'
            datas = self.parse_page_goods(res.text)
            if len(datas) == 0:
                break
            i = i + 1

    # 解析优惠券的每一页商品
    def parse_page_goods(self, html):
        doc = PyQuery(html)
        items = doc.find(".gl-item").items()
        datas = {}

        # 每一个商品都去看它的详情
        for item in items:
            goods_id = item.attr("data-sku")
            # goods = Goods(goods_id)

            # # 这个商品没有平行优惠, 直接放弃
            # promotions = goods.promotion()
            # if len(promotions) == 0:
            #     continue

            title = item.find(".p-name em").text()
            url = "https:" + item.find(".p-img a").attr("href")
            shop = item.find(".p-shop").text()

            one_data = {
                "url": url,
                "goods_id": goods_id,
                "title": title,
                "shop": shop,
                # "price": price,
                # "promotion": promotions,
                # "coupon": self.data,
            }
            print(one_data, "\n")
            datas[id] = one_data

        return datas


if __name__ == "__main__":
    # "https://search.jd.com/Search?coupon_batch=250384466"
    c = Coupon("254436170")
    c.GetGoods()

    # print(c.is_good())
    # c.foreach_goods()
    # c = Coupon(None)
    # print(c.status("42341454e21dd85425075cc05d6179e8a10299d3ac812ccd47fffbec632825cb04691e1d0508d5d44030de3f75fd9900"))
