/**
 * Created by xieyaxiong on 6/23/17.
 */
//圆形区域搜索关键字：学校
    function schoolSearch(x,y){
        addClass("m1")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var circle = new BMap.Circle(point,1200,{fillColor:"blue", strokeWeight: 1 ,fillOpacity: 0.3, strokeOpacity: 0.3});
        map.addOverlay(circle);
        var local =  new BMap.LocalSearch(map, {renderOptions: {map: map, autoViewport: false}});
        local.searchNearby('学校',point,1200);
        var school = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"e-result"},
            pageCapacity:5
        });
        school.searchInBounds('学校', map.getBounds());
    }

    //圆形区域搜索关键字：医院
    function hospitalSearch(x,y){
        addClass("m2");
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var circle = new BMap.Circle(point,1300,{fillColor:"blue", strokeWeight: 1 ,fillOpacity: 0.3, strokeOpacity: 0.3});
        map.addOverlay(circle);
        var local =  new BMap.LocalSearch(map, {renderOptions: {map: map, autoViewport: false}});
        local.searchNearby('医院',point,1300);
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"h-result"},
            pageCapacity:5
        });
        local.searchInBounds('医院', map.getBounds());
    }

    //圆形区域搜索关键字：银行
    function bankSearch(x,y){
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

       var circle = new BMap.Circle(point,1000,{fillColor:"blue", strokeWeight: 1 ,fillOpacity: 0.3, strokeOpacity: 0.3});
        map.addOverlay(circle);
        var local =  new BMap.LocalSearch(map, {renderOptions: {map: map, autoViewport: false}});
        local.searchNearby('银行',point,1000);
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"k-result"},
            pageCapacity:5
        });
        local.searchInBounds('银行', map.getBounds());
    }

    //多关键字查询：茶楼、KTV、电影院(休闲娱乐)
    function ktvSearch(x,y){
        addClass("m7")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['KTV','电影院'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"t-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    //多关键字查询：餐馆(餐饮)
    function repastSearch(x,y){
        addClass("m4")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['茶楼','餐馆','餐饮','饭店','酒店'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"r-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    function rentSearch(x,y){
        addClass("m5")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['酒店','住宿'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"r-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    function gardenSearch(x,y){
        addClass("m6")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['公园'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"r-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    //多关键字查询：商场、超市(购物)
    function shopSearch(x,y){
        addClass("m3")
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['商场','超市'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"s-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    //多关键字查询：健身房、球馆(运动、健身)
    function sportSearch(x,y){
        var map = new BMap.Map("bdmap1");
        var point = new BMap.Point(x,y);
        var marker = new BMap.Marker(point);  // 创建标注
        map.addOverlay(marker);              // 将标注添加到地图中
        map.enableScrollWheelZoom();
        map.centerAndZoom(point, 15);
        //添加地图缩放控件
        var navigationControl = new BMap.NavigationControl({
            // 靠左上角位置
            anchor: BMAP_ANCHOR_TOP_RIGHT,
            // LARGE类型
            type: BMAP_NAVIGATION_CONTROL_LARGE,
            // 启用显示定位
            enableGeolocation: true
        });
        map.addControl(navigationControl);

        var myKeys = ['健身房','球馆'];
        var local = new BMap.LocalSearch(map, {
            renderOptions:{map: map, panel:"o-result"},
            pageCapacity:5
        });
        local.searchInBounds(myKeys, map.getBounds());
    }

    function addClass(id){
        for(var i=1;i<=7;i++){
            $("#m"+i).removeClass("on");
        }
        $("#"+id).addClass("on");
    }