---
layout: post
title:  "方便在博客中使用的UML画图工具"
category: [opensource]
tags: [atom, uml]
---

写技术类的博客文章，经常需要画图，以UML为主。  
常用的UML画图工具有很多，有的功能全面，有的免费实用。但这些工具对于写博客来说，总觉得有一些不趁手：  
 - 需要在多个工具和文件之间切换。  
写博客需要用到文件编辑器，画UML图又需要uml编辑器，画好之后又要使用截图工具截下来并贴到文件编辑器中。如果写作过程中对图有修改，又要切换到uml编辑器修改，再截图到文件编辑器中。  
这个过程涉及到了三个工具（文件编辑器、uml编辑器、截图工具）和三种文件（文本文件、uml文件、图片）之间的切换。  
 - uml画图工具经常需要鼠标操作，除了uml本身希望表达的信息之外，还要分出一部分注意力来调整图中诸如文字大小、对齐这类繁琐的事情，这并不是使用快捷键代替鼠标就能解决的。
 - 有些uml编辑器不支持导出为图片，只能保存为uml编辑器所支持的格式。需要使用截图工具手动截图。  
 - 必须以uml编辑器识别的格式保存、打开和编辑，没有版本控制。  

经常一段时间的摸索，终于找到了一种满足需求uml画图方式。  
![](/image/atom-plantuml-0.png)  

<!-- more -->

#### 明确需求

针对博客中插入uml图这一应用，我希望有这样一种uml画图方式：  

##### 文本编辑

将uml的编辑和显示分开，以文本的方式编辑uml信息。  
所有的信息都可以以文本的方式表达，不需要鼠标操作。
文本信息的格式不要太复杂。
任意的文本编辑器就可以打开、阅读和修改uml信息。  
支持版本控制。  

##### uml展示

将文本信息智能地转换为uml图  
效果图看上去专业
支持多种uml图

##### 导出和使用

直接将结果导出到文章中。  
不要每次有修改都要在三种工具和文件中来回切换。  
所有事情都在一个工具里完成。

#### 解决方案：atom + plantuml + graphviz + markdown

atom是文件编辑器  
palntuml是用于编辑uml的语言  
markdown是用于编辑博客的语言  
graphviz是画图工具。

##### 工作环境

1.安装graphviz  
2.在atom中安装package plantuml-viewer和markdown-preview  

##### 创建文章

新建文件blog.md  
在blog.md中加入uml图的链接：`![](uml.png)`  
打开markdown-preview  
现在什么都没有，所以预览到一片空白

##### 创建uml

创建uml.puml  
在文件中加入这样的内容  

```
@startuml

Alice -> Bob : Hello
Bob -> Cady : Hello

@enduml
```

打开plantuml-viewer，会看到这样的图  
![](/image/atom-plantuml-1.png)  

##### uml图export到文章中

在plantuml-viewer在点击图，右键另存为png格式。默认的文件名与puml文件同名。  
刷新blog.md，就能在markdown-preview中看到了。  

##### 更新uml

修改uml.puml  
plantuml-viewer会实时更新，重新右键另存为png  
图片的改变不会导致markdown-preview的自动更新，刷新一下就可以了。  
不刷新也没关系，下次再打开就是最新的了。  

使用atom + plantuml + graphviz + markdown给博客添加uml，不需要截图、复制、粘贴，也不需要在多个工具和文件之间切换。  
全部工作都在atom中完成，唯一需要额外安装的是graphviz，也只是要安装一下就好了。  

#### plantuml

上述的例子中是一张序列图，其实它可以提供的图非常丰富。  
这些都是在plantuml中定义的。  
如何使用plantuml定义各种各样的uml图，将在别的文章介绍。  
以下是一些uml图的展示  

 - 序列图  
 
 ![](http://s.plantuml.com/imgp/o0-sequence-diagram-035.png)  
 
 - 用例图  
 
 ![](http://s.plantuml.com/imgp/o0-use-case-diagram-014.png)  
 
 - 类图  
 
 ![](http://s.plantuml.com/imgp/o0-class-diagram-014.png)  
 
 - 活动图  
 
 ![](http://s.plantuml.com/imgp/o0-activity-diagram-legacy-012.png)  
 
 - 活动图 plus
 
 ![](http://s.plantuml.com/imgp/o0-activity-diagram-beta-016.png) 
 
 - 组件图
 
 ![](http://s.plantuml.com/imgp/o0-component-diagram-004.png)  
 
 - 状态图
 
 ![](http://s.plantuml.com/imgp/o0-state-diagram-008.png)  
 
 - 对象图
 
 ![](http://s.plantuml.com/imgp/o0-object-diagram-001.png)