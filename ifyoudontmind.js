function WhatTime(hour,minute,period){
    
    var msg = " in the evening";
    
    if(period === "AM"){
       msg = " in the morning";
    }
    if(minute <= 30){
      console.log("It's just after " + hour + "" + msg);
    }
    else {
      console.log("It's just before " + (hour + 1) + "" + msg);
  }
  }
    WhatTime(8,50,"AM");
    WhatTime(7,15,"PM");