---
layout: post
title:  "JAVA json解析工具 - Jackson"
category: [编程语言]
tags: [JAVA, json, jackson]
---

jackson是github上解析json的开源项目。  

<!-- more -->

#### 普通用法

参考链接：  
http://www.blogjava.net/bolo/archive/2014/04/16/412533.html

#### 自定义用法

参考链接：  
http://www.yiibai.com/jackson/jackson_streaming_api.html

http://blog.csdn.net/nothing0318/article/details/8107970

http://blog.csdn.net/accountwcx/article/details/24585987

#### list用法

参考链接：  
http://www.cnblogs.com/dupang/p/5673097.html

```java
public class jacksonTest
{
	public List<tempInfo> formatter(String content) throws JsonParseException, JsonMappingException, IOException
	{
		ObjectMapper mapper = new ObjectMapper();
        List<tempInfo> lendReco = mapper.readValue(c,new TypeReference<List<tempInfo>>() { });
        System.out.println(lendReco.get(0).title);
		return lendReco;
	}
}

class tempInfo
{
	public String title;
	public String msg;
	public String url;
	public tempInfo(){}
	@JsonCreator
	public tempInfo(@JsonProperty("title") String title, 
	             @JsonProperty("msg") String msg,
	             @JsonProperty("url") String url) {

	    this.title = title;
	    this.msg = msg;
	    this.url = url;
	}
}
```
#### 类内类使用list遇到的问题

如果把上文中的tempInfo作为jacksonTest的内部类，会报错。似乎是jackson本身的问题。github上说该问题已经修复，换新版本就可以了，没有试过。