var rule = {
    title: '朱古力',
    host: 'https://pigav.com',
    url: '/fyclass/page/fypage',
    headers: {
        'User-Agent': 'MOBILE_UA'
    },
    timeout: 5000,
    class_name: '無碼AV&流出版AV&AV&熱門AV&AV影片&A片&每日AV&長片AV&精選AV&HDAV&日韓AV', //静态分类名称拼接
    class_url: '無碼av線上看&流出版av線上看&av&熱門av線上看&av影片&a片&每日av線上看&長片av線上看&精選av線上看&hdav線上看&日韓av線上看', //静态分类标识拼接
    limit: 5,
    play_parse: true,
    lazy: '',
    一级: '.l-post div&&a;a&&title;span&&data-bgsrc;.absolute.bottom-1&&Text;a&&href',
    二级: '*',
}