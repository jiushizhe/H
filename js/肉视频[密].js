var rule = {
  title: '',
  host: 'https://rou.video',
  url: '/t/fyclass?order=createdAt&page=fypage',
  searchUrl: '/search?q=**&t=&page=fypage',
  homeUrl:'/home',
  searchable: 2,
  quickSearch: 0,
  filterable: 0,
  headers: {
    'User-Agent': 'MOBILE_UA',
  },
  class_name:'國產AV&自拍流出&探花&OnlyFans&日本',
  class_url:'國產AV&自拍流出&探花&OnlyFans&日本',
  play_parse: true,
  lazy: '',
  limit: 6,
  推荐: '*',
  double: true,
  一级: '.my-auto .relative;img&&alt;img&&src;.rounded-sm&&Text;a&&href',
  二级: $js.toString(() => {
    //let name=jsp.pdfh(fetch(input,{redirect:false}),'.px-2 .hidden&&Text')
    let url=input.replace('https://rou.video', 'https://rou.video/api')
    let url1=JSON.parse(fetch(url,{redirect:false})).video.videoUrl
    let url2=fetch(url1,{redirect:false}).trim().split('\n').pop()
    VOD={
      vod_play_from: 'rousp',
      //vod_play_url: `${name}$${url2}`
      vod_play_url: `无名$${url2}`
    }
  }),
  搜索: '*',
}