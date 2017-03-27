---
layout: post
title:  "eclipse插件导出失败"
category: [编程语言]
tags: [eclipse, plugin, export, java]
---

将eclipse插件导出为`Deployed plug-ins and fragments`时失败并提示：  
![](/image/eclipse-plugin-export-fail-0.jpg)  

<!-- more -->

#### 现象

将eclipse插件导出时失败，根据提示打开log  

```
1. ERROR in D:\workspace\com.test.myplugin\src\com\test\myplugin\Environment.java (at line 5)
	import org.eclipse.jdt.core.IJavaElement;
	       ^^^^^^^^^^^^^^^
The import org.eclipse.jdt cannot be resolved
```

似乎是import org.eclipse.jdt有问题，但在工程中，org.eclipse.jdt.core.IJavaElement对应的jar包已经导入且编译正常  
![](/image/eclipse-plugin-export-fail-1.jpg)

#### 解决方法

原因还没找到，但有解决方法。  
在`Deployed plug-ins and fragments`，打开Options选项卡，钩选`Use class files compiled in the workspace`  
![](/image/eclipse-plugin-export-fail-2.jpg)



#### classdefnotfound