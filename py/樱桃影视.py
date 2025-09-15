# coding=utf-8
# !/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup
import re
from base.spider import Spider

sys.path.append('..')

headerx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    }

xurl = "https://www.kan9.xyz"


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

    def fl(self,res):
        videos = []
        res.encoding = "utf-8"
        res = res.text
        doc = BeautifulSoup(res, "html.parser")
        sourcediv = doc.find_all('ul', class_='stui-vodlist clearfix')
        vod = [a for div in sourcediv for a in div.find_all('li')]
        for item in vod:
            name = item.select_one('div a')['title']
            id = item.select_one('div a')['href']
            pic = item.select_one('div a')["data-original"]
            remark = item.find("span", class_="pic-text text-right").text

            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": "年份:" + remark
            }
            videos.append(video)
        return videos

    def homeVideoContent(self):
        try:
            res = requests.get(xurl, headers=headerx, verify=False)

            videos = self.fl(res)
        except:
            pass
        result = {'list': videos}
        return result

    def homeContent(self, filter):
        result = {}
        result['class'] = []
        result['class'].append({'type_id': '/sortlist/4353', 'type_name': '国产视频'})
        result['class'].append({'type_id': '/sortlist/4354', 'type_name': '日韩视频'})
        result['class'].append({'type_id': '/sortlist/4355', 'type_name': '欧美视频'})
        result['class'].append({'type_id': '/sortlist/4356', 'type_name': '动漫视频'})
        result['class'].append({'type_id': '/sortlist/4357', 'type_name': '制服人妻'})
        result['class'].append({'type_id': '/sortlist/4358', 'type_name': '自拍自慰'})
        result['class'].append({'type_id': '/sortlist/4359', 'type_name': '群交颜射'})
        result['class'].append({'type_id': '/sortlist/4360', 'type_name': '写真伦理'})
        res = requests.get(xurl + '/tags.html', headers=headerx, verify=False)

        res.encoding = "utf-8"
        doc = BeautifulSoup(res.text, "html.parser")
        sourcediv = doc.find_all('ul', class_='stui-screen__list type-slide bottom-line-dot clearfix')

        vod = [a for div in sourcediv for a in div.find_all('li')]

        for item in vod:
            a_element = item.select_one('a')
            if a_element:
                id = a_element['href']
                id = id.replace('http://www.kan9.xyz', "")
                id = id.replace(".html", "")
                name = a_element.text
                result['class'].append({'type_id': id, 'type_name': name})
        return result

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []
        if pg:
            page = int(pg)
        else:
            page = 1
        res = requests.get(url=xurl + cid + "/time-" + str(page) + ".html", headers=headerx, verify=False)
        videos = self.fl(res)
        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        did = ids[0]
        result = {}

        res = requests.get(did, headers=headerx, verify=False)
        res.encoding = "utf-8"
        res = res.text

        name_match = re.search(r'class="btn btn-primary" href="(.*?)"', res)
        if name_match:
            tx = name_match.group(1)
            res = requests.get(tx, headers=headerx, verify=False)
            res.encoding = "utf-8"
            res = res.text
            purl_match = re.search(r'thisUrl = "(.*?)"', res)
            if purl_match:
                purl = purl_match.group(1)

        videos = []
        videos.append({
            "vod_id": did,
            "vod_name": tx,
            "vod_pic": "",
            "type_name": "ぃぅおか🍬 คิดถึง",
            "vod_year": "",
            "vod_area": "",
            "vod_remarks": "",
            "vod_actor": "",
            "vod_director": "",
            "vod_content": "",
            "vod_play_from": "直链播放",
            "vod_play_url": purl
        })

        result = {}
        result['list'] = videos

        return (result)

    def playerContent(self, flag, id, vipFlags):
        result = {}

        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = id
        result["header"] = headerx
        return result

    def searchContent(self, key, quick):
        return self.searchContentPage(key, quick, '1')

    def searchContentPage(self, key, quick, page):
        result = {}
        url = xurl + '/search/{0}/time-{1}.html'.format(key, page)
        res = requests.get(url=url, headers=headerx, verify=False)
        videos = self.fl(res)
        result['list'] = videos
        result['page'] = page
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None






