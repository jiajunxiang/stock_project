/**
 * Created by yaling.he on 2015/11/18.
 */
//时间
function totwo(n){
    if(n<=9){
        return n = "0"+n;
    }
    else{
        return n =""+n;
    }
}

function fn(){
    var time = new Date();
    var str= "";

	var hour = document.getElementById("hours");
    // console.log(time);
    var year = time.getFullYear();
    var mon = time.getMonth()+1;
    var day = time.getDate();
    var h = time.getHours();
    var m = time.getMinutes();
    var s = time.getSeconds();
    var week = time.getDay();
    switch (week){
        case 0:week="日";
            break;
        case 1:week="一";
            break;
        case 2:week="二";
            break;
        case 3:week="三";
            break;
        case 4:week="四";
            break;
        case 5:week="五";
            break;
        case 6:week="六";
            break;
    }
	if(h < 6){
		hour.innerHTML = "凌晨好!";
	} else if(h < 11){
		hour.innerHTML = "上午好!";
	} else if(h < 13){
		hour.innerHTML = "中午好!";
	} else if(h < 19){
		hour.innerHTML = "下午好!";
	} else if(h < 21){
		hour.innerHTML = "傍晚好!";
	} else {
		hour.innerHTML = "深夜好!";
	}
    str = "现在是:"+year +"年"+totwo(mon)+"月"+totwo(day)+"日"+"&nbsp;"+totwo(h)+":"+totwo(m)+":"+totwo(s)+"&nbsp;"+"星期"+week;
    document.getElementById('time').innerHTML=str;
}

setInterval("fn();",1000);

