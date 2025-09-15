var rule = {
    title: '海角社区[密]',
    host: 'https://haijiao.com',
    url: "/api/topic/node/topics?page=fypage&nodeId=fyclass&type=1&limit=50",
    searchUrl: '/es?key=**&node_id=0&type=2',
    searchable: 2,
    quickSearch: 0,
    filterable: 0,
    class_name: '收费视频',
    class_url: '1001',
    double: false,
    play_parse:true,
    lazy:$js.toString(()=>{
            input = {url: input,parse: 0}
        }),
    一级: $js.toString(()=>{
        let d = [];
        let html = request(input);
        let data = JSON.parse(html).data;
        let result = base64Decode(base64Decode(base64Decode(data)));
        let reldata = JSON.parse(result).results;
        reldata.forEach(it => {
            let id = 'https://haijiao.com/api/topic/'+it.topicId
            d.push({
            url:id,
            title:it.title,
            img:'http://www.weibomn.com/uploadfile/image/20240611/3eb5cec98ad4a447a7ff069a43b73481.jpg',
            desc:'',
        })
        })
       setResult(d);
    }),
    二级: $js.toString(()=>{
      let d = [];
      log(input)
        let html = request(input);
        let data = JSON.parse(html).data;
        let result = base64Decode(base64Decode(base64Decode(data)));
        let result_json = JSON.parse(result);
        let reldata = result_json.attachments;
    let url = '';
    let pic = '';
    let title = '';
    let content = '';
        reldata.forEach(it => {
            let id = result_json.topicId;
            if(it.remoteUrl!==null&&it.remoteUrl.includes("/api")){
                    url='https://haijiao.com'+it.remoteUrl,
                    title=result_json.title,
                    pic='http://www.weibomn.com/uploadfile/image/20240611/3eb5cec98ad4a447a7ff069a43b73481.jpg'
            content=it.content;
           }
        })
    let urls = ['不知道看美女'+'$'+url] 
    VOD = {
            vod_content: content,
            vod_name: title,
            type_name: '',
            vod_pic: pic,
            vod_play_from: '球球啦',
            vod_play_url: urls.join('#')
        };
    }),
    搜索: '*',
}