---
layout: post
title:  "eclipse插件开发 Hello World"
category: [编程语言]
tags: [eclipse, plugin, java]
---

#### 使用模板创建一个插件

File -> New -> Other -> Plug-in Project  
**如果Wizards中没有Plub-in Project，可能因为使用的是Java SE版本的eclipse，换成Java EE版本的eclipse就可以了。**  
  
输入Project name

选择一个模板，例如“Hello, World Command”，Finish

<!-- more -->

#### 运行效果

出现了这样的一个工程：  
![](/image/create-a-eclipse-plugin-by-template-0.jpg)  
点击运行按钮，将再开一个eclipse  

 - 效果一：菜单栏Run后面出现“Sample Menu”，点击后弹出对话框：“Hello, Eclipse world”  
 - 效果二：工具栏出现一个紫色的小球，点击后弹出对话框：“Hello, Eclipse world”  

![](/image/create-a-eclipse-plugin-by-template-2.jpg)   

#### 插件导出与加载

##### 导出

File -> Export -> Plugin 

##### 加载

打开eclipse的安装目录ECLIPSE  
把jar包copy到ECLIPSE/plugins  
重启eclipse  

#### 工程说明

打开plugin.xml，选择Extensions，会看到这样的内容：  
![](/image/create-a-eclipse-plugin-by-template-1.jpg)  

##### commands结点

提供哪些command。

##### handlers结点

定义处理command执行行为的类。例如触发example.commands.sampleCommand的行为，即弹出“Hello, World Command”，就是在example.handlers.SampleHandler中定义。  

```java
public class SampleHandler extends AbstractHandler {

	@Override
	public Object execute(ExecutionEvent event) throws ExecutionException {
		IWorkbenchWindow window = HandlerUtil.getActiveWorkbenchWindowChecked(event);
		MessageDialog.openInformation(
				window.getShell(),
				"Example",
				"Hello, Eclipse world");
		return null;
	}
}
```

##### bindings

##### menus

定义要增加的menu和toolbar的属性，例如：  
菜单的位置、显示的字符串、快捷键、点击时触发的command  
工具栏按钮的位置、提示的字符串、图标、点击时触发的command  