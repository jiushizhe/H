# coding=utf-8
# !/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup
from base.spider import Spider
import sys
sys.path.append('..')
xurl = "https://avcabi.com"
headerx = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Referer':xurl
 }


class Spider(Spider):
    global xurl
    global headerx

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def fl(self,key):
        videos = []
        doc = BeautifulSoup(key, "html.parser")
        soups = doc.find_all('div', class_="col-xs-12 col-sm-6 col-md-3 col-lg-3 top_grid1-box1")
        for soup in soups:
            name = soup.select_one("a")['title']
            id = xurl + soup.select_one("a")["href"]
            pic = soup.select_one("a div div img")['data-original']
            remark = soup.find('small').text
            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": remark
            }
            videos.append(video)
        return videos

    def homeContent(self, filter):
        result = {}
        result['class'] = []
        detail = requests.get(url=xurl, headers=headerx)
        detail.encoding = "utf-8"
        doc = BeautifulSoup(detail.text, "html.parser")
        soups = doc.find('ul', class_="nav navbar-nav navbar-right")
        soup = soups.find_all('li')
        for i in soup:
            name = i.select_one("a")['title']
            if name == '星火导航':
                continue
            id = i.select_one("a")['href'].replace('1.shtml', '')
            result['class'].append({'type_id': id, 'type_name': name})
        soups = doc.find('div', class_="tab-content")
        soup = soups.find_all('button')
        for i in soup:
            pd = i.select_one("span")
            if pd is None:
                name = i.select_one("a").text
                id = i.select_one("a")['href'].replace('1.shtml', '')
                result['class'].append({'type_id': id, 'type_name': name})
        return result

    def homeVideoContent(self):
        try:
            detail = requests.get(url=xurl, headers=headerx)
            detail.encoding = "utf-8"
            res = detail.text

            videos = self.fl(res)

            result = {'list': videos}
            return result
        except:
            pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        if pg:
            page = int(pg)
        else:
            page = 1
        page = int(pg)

        videos = []
        try:
            detail = requests.get(url=xurl + cid + str(page) + '.shtml', headers=headerx)
            print(xurl + cid + str(page) + '.shtml')
            detail.encoding = "utf-8"
            res = detail.text
            videos = self.fl(res)
        except:
            pass
        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        did = ids[0]
        result = {}
        videos = []
        purl = did.replace('voddetail', 'vodplay')

        videos.append({
            "vod_id": did,
            "vod_name": '',
            "vod_pic": "",
            "type_name": '',
            "vod_year": '',
            "vod_area": '',
            "vod_remarks": "",
            "vod_actor": '',
            "vod_director": '',
            "vod_content": '',
            "vod_play_from": '直链播放',
            "vod_play_url": purl
        })

        result['list'] = videos

        return result

    def playerContent(self, flag, id, vipFlags):
        result = {}
        res = requests.get(url=id, headers=headerx)
        res = res.text
        after_https = re.search(r'"contentUrl": "(.*?)"', res).group(1)
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = after_https
        result["header"] = ''
        return result

    def searchContentPage(self, key, quick, page):
        result = {}
        videos = []
        if not page:
            page = 1
        detail = requests.get(url=xurl + '/vodlist/---latest-' + str(page) + '.shtml?q=' + key, headers=headerx)
        detail.encoding = "utf-8"
        res = detail.text
        videos = self.fl(res)
        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None
