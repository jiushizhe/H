var rule = {
    title: 'CNAV',
    host: 'https://555760.xyz/',
    url: 'https://555760.xyz/category/fyclass/page/fypage/',
    searchUrl: 'https://555760.xyz/?s=**',
        //class_parse:'#menu-main-menu&&.menu-item;a&&title;a&&href;.*/(.*?).html',
    class_name: '91大神&国产传媒&有码中文&无码中文&欧美专区&成人动漫',
    class_url: '91大神&国产传媒&youmazhongzi&wumazhongzi&oumei&chengrendongman',
    searchUrl: '',
    searchable: 2,
    quickSearch: 0,
    headers: {
        'User-Agent': 'MOBILE_UA',
    },
    timeout: 5000,
    //class_parse: '#uk-nav-header li;a&&Text;a&&href;/(.*?)\.html',
    cate_exclude: '',
    /*play_parse: true,
                                     lazy: `js:
let kcode=jsp.pdfh(request(input).match(/<iframe(.*?)</iframe>/)[1]);
let kurl=kcode.match(/url=(.*?)\"/)[1];
if (/m3u8|mp4/.test(kurl)) {
input = { jx: 0, parse: 0, url: kurl }
} else {
input = { jx: 0, parse: 1, url: rule.parse_url+kurl }
}`, 
    double: true,*/
   推荐: '.videos-list&&.loop-video;a&&title;img&&data-src;span&&Text;a&&href',
    一级: '#main&&.videos-list&&.thumb-block;a&&title;img&&data-src;span&&Text;a&&href',
    二级: '*',
     搜索: '.s-tab-main&&li;.js-tongjic&&title;img&&src;.hint&&Text;a&&href;.pay&&Text',
}