---
layout: post
title:  "javascript等待条件发生时执行"
category: [编程语言]
tags: [javascript]
---

目标：  
当condition=true时才执行doSomething()，如何让doSomething()等待condition变为true  

<!-- more -->

```javascript
function wait(callback,seconds){
    var timelag=null;//这里应该用if判断一下；可以扩展
    timelag=window.setTimeout(callback,seconds);
}
function doItWhenCondition()
{
    if(contidion)
    {
        console.log("I'm waiting");
        wait(doItWhenCondition,2000);
    }
    else {
        doSomething();
    }
}
wait(doItWhenCondition,2000);
```