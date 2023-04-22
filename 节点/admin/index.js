function change(limit){ //B转化成KB，MB，GB
    var size = "";
    if(limit < 0.1 * 1024){                            //小于0.1KB，则转化成B
        size = limit.toFixed(2) + "B"
    }else if(limit < 0.1 * 1024 * 1024){            //小于0.1MB，则转化成KB
        size = (limit/1024).toFixed(2) + "KB"
    }else if(limit < 0.1 * 1024 * 1024 * 1024){        //小于0.1GB，则转化成MB
        size = (limit/(1024 * 1024)).toFixed(2) + "MB"
    }else{                                            //其他转化成GB
        size = (limit/(1024 * 1024 * 1024)).toFixed(2) + "GB"
    }
 
    var sizeStr = size + "";                        //转成字符串
    var index = sizeStr.indexOf(".");                    //获取小数点处的索引
    var dou = sizeStr.substr(index + 1 ,2)            //获取小数点后两位的值
    if(dou == "00"){                                //判断后两位是否为00，如果是则删除00               
        return sizeStr.substring(0, index) + sizeStr.substr(index + 3, 2)
    }
    return size;
}
function Toast(msg,duration){   //消息提示框
    duration=isNaN(duration)?3000:duration;  
    var m = document.createElement('div');  
    m.innerHTML = msg;  
    m.style.cssText="font-size: .32rem;color: rgb(255, 255, 255);background-color: rgba(0, 0, 0, 0.6);padding: 10px 15px;margin: 0 0 0 -60px;border-radius: 4px;position: fixed;    top: 50%;left: 50%;width: 130px;text-align: center;";
    document.body.appendChild(m);  
    setTimeout(function() {  
        var d = 0.5;
        m.style.opacity = '0';  
        setTimeout(function() { document.body.removeChild(m) }, d * 1000);  
    }, duration);  
}
function get(keyword) {
    var reg = new RegExp("(^|&)"+keyword+"=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;   //注意此处参数是中文，解码使用的方法是unescape ，那么在传值的时候如果是中文，需要使用escape('曲浩')方法来编码。
}
function homepage(){
    updateUrl('path','/');
    Refresh();
}
// 实现js更改url参数，但不刷新或重载页面
function updateUrl( key, value){
      var newurl = updateQueryStringParameter(key, value)
      //向当前url添加参数，没有历史记录
      window.history.replaceState({
      	path: newurl
      }, '', newurl);
    }
 
    function updateQueryStringParameter(key, value) {
      var uri = window.location.href
    	if(!value) {
    		return uri;
    	}
    	var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
    	var separator = uri.indexOf('?') !== -1 ? "&" : "?";
    	if (uri.match(re)) {
    		return uri.replace(re, '$1' + key + "=" + value + '$2');
    	}
    	else {
    		return uri + separator + key + "=" + value;
    	}
}
function Fdelete(key){ //删除文件
    if(confirm('您真的要删除吗，文件会想你的，哈哈哈')){
    $(document).ready(function(){
        $.ajax({
            type: "POST",
            url: "/api/delete",
            data: {
            path:pathData[key][0],
            api_id:api_id,
            api_key:api_key
        },
            success: function (data,status,xhr) {
                //当请求成功时运行的函数。
                //alert(data)
                Refresh()
                //pathData = JSON.parse(data)
            },
            error:function(xhr,status,error){
                //如果请求失败要运行的函数。
                alert('删除失败'+error)
            }});
    });
}
}
function new_directory(){ //新建目录
    word = prompt("目录名","");
    if(word){
        $(document).ready(function(){
            $.ajax({
                type: "POST",
                url: "/api/add",
                data: {
                route:true,
                api_id:api_id,
                api_key:api_key,
                path:get('path')+'/'+word
            },
                success: function (data,status,xhr) {
                    //当请求成功时运行的函数。
                    //alert(data)
                    Refresh()
                    //pathData = JSON.parse(data)
                },
                error:function(xhr,status,error){
                    //如果请求失败要运行的函数。
                    alert('创建'+error)
                }});
        });
    }
}
function f_list_html(i){
    `i:文件名`
    return `<li id="flist" >
    <a  href="javascript:void(0);" onclick="flist_li('`+i+`')">`+i+
    '</a><a class="del" style="float: right;" href="javascript:void(0);" onclick="Fdelete(`'+i+'`)" >删除</a>'+
    '</a><a  style="float: right;" href="javascript:void(0);" onclick="copy(`'+i+'`)" >复制</a>'+
    '</a><a  style="float: right;" href="javascript:void(0);" onclick="move(`'+i+'`)" >剪切</a>'+
    '<span >'+change(pathData[i][3])+'</span>'+
    '</li>';
}
function flist_li(key){ //获取文件列表
    PreviousStep = get('path'); //记录上一步路径
    updateUrl('path',pathData[key][0]);
    Refresh();
    // console.log(pathData[key][3]);
    // if(pathData[key][2]){
    //     //window.location.href = '../'+pathData[key][0]
    //     Refresh(); // 刷新列表
    // } else {
    //     $(document).ready(function(){
    //         $.post("/api/PathInfo",{
	// 		type:"appoint",
	// 		path:get('path'),
    //         api_id:api_id,
    //         api_key:api_key
    //         },
    //         function(data){
    //             $("#wenjiancaid_ul").empty();
    //             pathData = JSON.parse(data) //目录列表数据
    //             for (let i in pathData){
    //                 $("#wenjiancaid_ul").append(f_list_html(i));
    //             }
    //             console.log(pathData);
    //         });
    //     });
    //     LastActivityView.push(get('path'));
    //     path_xianshi(); //刷新显示的路径
    // }
}
function skip(key){ //获取文件列表
    PreviousStep = get('path'); //记录上一步路径
    updateUrl('path',key);
    Refresh();
}
function upload(){
    $(document).ready(function(){
        $("#wenjiancaid_ul").empty();
        $("#wenjiancaid_ul").append(
            `
            <iframe frameborder="0"
             noresize="noresize"
             style="position: absolute; background: transparent; width: 70%; height:70%;"
             src="../upload?path=`+get('path')+`&api_id=`+api_id+`&api_key=`+api_key+`&"
             frameborder="0">
            </iframe>
            `
        );
    });
}
function Refresh(){ // 刷新文件列表
    $(document).ready(function(){
        $.ajax({ //请求API
            type: "POST",
            url: "/api/PathInfo",
            data: {
            type:"appoint",
            path:get('path'),
            api_id:api_id,
            api_key:api_key
        },
            success: function (data,status,xhr) {
                //当请求成功时运行的函数，在这里是获取目录列表，如果获取目录列表失败就会报错500
                $("#wenjiancaid_ul").empty();
                pathData = JSON.parse(data)
                for (let i in pathData){
                    $("#wenjiancaid_ul").append(f_list_html(i));
                }
                console.log(pathData);
            },
            error:function(xhr,status,error){
                //如果请求失败要运行的函数,在这里是获取文件内容并且显示
                $(document).ready(function(){
                    $("#wenjiancaid_ul").empty();
                    $("#wenjiancaid_ul").append(`
                    <iframe frameborder="0"
                    noresize="noresize"
                    style="position: absolute; background: transparent; width: 70%; height:70%;"
                    src="`+get('path')+`?api_id=`+api_id+`&api_key=`+api_key+`&"
                    frameborder="0">
                    </iframe>
                    `)
                    console.log(`
                    <iframe frameborder="0"
                    noresize="noresize"
                    style="position: absolute; background: transparent; width: 70%; height:70%;"
                    src="`+'/'+get('path')+`&api_id=`+api_id+`&api_key=`+api_key+`&"
                    frameborder="0">
                    </iframe>
                    `);
                    path_xianshi();
            });
    }});
    path_xianshi();
    });
    LastActivityView.push(get('path')); //添加当前的操作记录
}
function paste(){ // 粘贴函数
    _new = get('path')+'/'+copy_move_old_name;
    _old = copy_move_old;
    if(copy_move_old == ''){
        Toast('你没有要粘贴的路径',1000)
        return false;
    }
    if(_paste == 'copy'){
        $(document).ready(function(){
            $.ajax({ //请求API
                type: "GET",
                url: "/api/copy",
                data: {
                old:_old,
                new:_new,
                api_id:api_id,
                api_key:api_key
            },
                success: function (data,status,xhr) {
                    copy_move_old = ''; //操作成功后删除类型
                    _paste = '';
                },
                error:function(xhr,status,error){
                    Toast('粘贴失败',1000)
            }
            });
        });
    } else if (_paste == 'move') {
        $(document).ready(function(){
            $.ajax({ //请求API
                type: "POST",
                url: "/api/move",
                data: {
                old:_old,
                new:_new,
                api_id:api_id,
                api_key:api_key
            },
                success: function (data,status,xhr) {
                    copy_move_old = ''; //操作成功后删除数据
                    _paste = '';
                },
                error:function(xhr,status,error){
                    Toast('粘贴失败',1000)
            }
            });
        });
    } else {
        Toast('并不需要粘贴',1000)
    }
    Refresh();
}
function copy(name){ //标记复制数据
    `name:文件名`
    _paste = 'copy';
    copy_move_old_name = name;
    copy_move_old = get('path')+'/'+copy_move_old_name;
    console.log([_paste,copy_move_old]);
}
function move(name){ //标记移动文件数据
    `name:文件名`
    _paste = 'move';
    copy_move_old_name = name;
    copy_move_old = get('path')+'/'+copy_move_old_name;
    console.log([_paste,copy_move_old]);
}
function cookie_apikey(api_id,api_key){ //将apikey写入cookie
    $(function(){
        $.cookie('api_id', api_id);
        $.cookie('api_key', api_key);
        delete_cookie_apikey()
    });
}
function get_cookie_apikey(){ //查看cookie
    $(function(){
        api_id = $.cookie('api_id'); 
        api_key = $.cookie('api_key');
    })
}
function delete_cookie_apikey() { //Apikey of delete cookie
    $(function(){
        if($.removeCookie('api_id') && $.removeCookie('api_key')){
            return true;
        }
    })
}
function forward(){ //向后退目录操作
    updateUrl('path',PreviousStep); //改变path参数值
    Refresh(); //刷新路径
}
function path_xianshi(){ //显示路径
    let path  = String(get('path')).split('\\');
    console.log(path);
    rte = '';
    pingj = '';
    for (let i = 0; i < path.length; i++) {
        // console.log(i);
        for(let j = 0; j <= i; j++) { 
            pingj += path[j] + '\\\\' ;
            // console.log('j:'+j);
            // console.log('jstr:'+path[j]);
        }
        // console.log(pingj)
        // console.log(path[i]);
        rte += '\\' + `<a href="javascript:void(0);" onclick="skip('`+pingj+`')" style="width: 30%;">`+path[i]+`</a>`;
        // console.log(rte);
        pingj = '';
    }
    // console.log(rte);
    $(function(){
        $("#path").empty(); //删除旧的
        $("#path").append(rte); //刷新
    });
    return rte;
}
var url = window.location.href;  //访问时URL
var api_id = ''; //APIid
var api_key = '';//APIkey
// let path = get('path');//访问时的path
var pathData;//目录列表数据
var copy_move_old = ''; //复制(移动)前路径标记数据，标记文件/目录的路径
var copy_move_old_name = ''; //复制(移动)前路径标记数据，标记文件/目录的文件名
var _paste = ''; //标记粘贴类型（copy/move）
var LastActivityView = [] ; //路径操作记录
var PreviousStep = '' ; //上一步操作的目录
LastActivityView.push(get('path')); //添加当前的操作记录
PreviousStep = get('path'); //记录上一步操作的路径
get_cookie_apikey(); //访问时刷新apikey
Refresh() //访问时刷新列表
// path_xianshi() //刷新访问路径