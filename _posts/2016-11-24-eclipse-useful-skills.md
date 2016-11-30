---
layout: post
title:  "eclipse实用技巧"
category: 编程语言
tags: [eclipse]
---

# 读代码

||||
|---|---|---|
|F2|当鼠标放在一个标记处出现Tooltip时候按F2则把鼠标移开时Tooltip还会显示即Show Tooltip|
|F3|跳转到定义处|
|F12|激活编辑器 |
|CTRL + e/pg dn/pg up|快速转换Tab页面|  
|CTRL + G| 工作区中的声明|搜索
|Ctrl+H |打开搜索对话框 |搜索
|Ctrl+J |正向增量查找(按下Ctrl+J后,你所输入的每个字母编辑器都提供快速匹配定位到某个单词,如果没有,则在stutes line中显示没有找到了)|搜索
|Ctrl+Shift+J |反向增量查找|搜索
|Ctrl+K |参照选中的Word快速定位到下一个|搜索
|CTRL + L|转至行 | 
|CTRL + m|打开/关闭编辑器窗口最大化|
|CTRL + o|查看当前类的方法或某个特定方法|
|CTRL + T 或 F4|查看一个类的继承关系树，自顶向下的。再多按一次`CTRL + T`, 会换成自底向上的显示结构|
|CTRL + W |关闭当前Editer |
|CTRL + Space |代码助手完成一些代码的插入(但一般和输入法有冲突,可以修改输入法的热键,也可以暂用Alt+/来代替)|
|CTRL + /(小键盘) |折叠当前类中的所有代码|
|CTRL + ×(小键盘) |展开当前类中的所有代码|
| Alt + 左/右|在导航历史记录（Navigation History）中后退/前进（就像Web浏览器的后退/前进），在利用F3跳转之后，特别有用|
|CTRL + Shift + G|在workspace中搜索引用（reference）。对于方法，这个热键的作用和F3恰好相反。它使你在方法的栈中，向上找出一个方法的所有调用者。|搜索
|CTRL + SHIFT + P |定位到成对的匹配符(如{})的起始/结束处|
|CTRL + SHIFT + r|打开工作区中任何一个文件|搜索
|Ctrl + Shift + T|类型|搜索 
|CTRL + SHIFT + u|出现在文件中|搜索
|Ctrl + Shift + ↑/↓| 转至上/下一个成员|
|Ctrl+Alt+H|查看一个方法被哪些地调用，产生一个调用关系树|搜索

<!-- more -->

# 编辑代码

|||
|---|---|
|Ctrl + B |编译|
|Ctrl + D|删除当前行 |
|Ctrl + Q| 回到最后一次编辑的地方|
|Ctrl + 1|快速修复|
|Ctrl + .|将光标移动至当前文件中的下一个报错处或警告处|
|Ctrl - /| 使用`//`对一行或多行注释/取消注释|
|Ctrl+Shift+M |(先把光标放在需导入包的类名上) 作用是加Import语句。 |
|Ctrl+Shift+O |作用是缺少的Import语句被加入，多余的Import语句被删除。 |
|Ctrl + Shift + /|使用`/**/`注释代码，再按一次 不对取消。在JSP文件窗口中是`〈!--~--〉`| 
|shift+enter|当前行之下创建一个空白行，与光标是否在行末无关|
|Ctrl+shift+enter|当前行之上创建一个空白行，与光标是否在行末无关|
| Alt+↑/↓|当前行/选中行的内容往上或下移动。在try/catch部分，这个快捷方式尤其好使。|
|Ctrl+Alt+↑/↓|复制并移动高亮显示的一行或多行。**经测试，与调屏幕亮度的key冲突**|
|Ctrl+Shift+X |把当前选中的文本全部变味大写|
|Ctrl+Shift+Y |把当前选中的文本全部变为小写|
|Alt+Shift+↑/↓ |选择封装元素，高亮一块代码|
|Alt+Shift+←/→ |选择封装元素，高亮一段代码|
|Alt+Shift+O(或点击工具栏中的Toggle Mark Occurrences按钮) |当点击某个标记时可使本页面中其他地方的此标记黄色凸显，并且窗口的右边框会出现白色的方块，点击此方块会跳到此标记处。 |

# 调试

|||
|---|---|
|单步返回 |F7 |
|单步跳过 |F6 |
|单步跳入 |F5 |
|单步跳入选择 |Ctrl+F5 |
|调试上次启动 |F11 |
|继续 |F8| 
|使用过滤器单步执行 |Shift+F5 |
|添加/去除断点 |Ctrl+Shift+B |
|显示 |Ctrl+D |
|运行至行 |Ctrl+R |
|执行 |Ctrl+U |

# SVN项目管理

# 配置

|||
|---|---|
|单击一个元素的时候，代码中所有该元素存在的地方都会被高亮显示|选择Windows->Preferences->Java-> Editor-> Mark Occurrences，勾选选项|
|根据代码风格设定重新格式化代码|准备配置文件：Window Style->Code Formatter，Code Style和Organize Imports->Export功能来生成配置文件。<br>导入配置文件：同上->Import<br>应配置文件：Control-Shift-F|
|锁定命令行窗口|在命令行视图中（Window ->Show View ->Other ->Basic ->Console），试试看用滚动锁定按钮来锁定控制台输出不要滚屏。|
|使用分级布局| 在包浏览视图（Package Explorer view）中默认的布局（扁平式）方式让我困惑，它把包的全名显示在导航树（navigation tree）中。我更喜欢我源码的包和文件系统视图，在Eclipse中叫做分级布局（Hierarchical Layout）。要切换到这种模式，点击包浏览视图中向下的按钮，选择布局（Layout），然后选择分级（Hierarchial）。|
|一次显示多个文件|把一个编辑窗口拖到另一个窗口的底部或侧边的滚动条上|
|显示行号|右击窗口的左边框即加断点的地方选Show Line Numbers|
|加断点|双击窗口的左边框| 

# 文本编辑的通用命令

|功能|局势键|
|---|---|
|查找并替换 |Ctrl+F |
|查找上一个 |Ctrl+Shift+K |
|查找下一个 |Ctrl+K |
|撤销 |Ctrl+Z |
|复制 |Ctrl+C |
|粘贴 |Ctrl+V |
|重做 |Ctrl+Y |
|恢复上一个选择 |Alt+Shift+↓ |
|剪切 |Ctrl+X |
|快速修正 |Ctrl1+1 |
|内容辅助 |Alt+/ |
|全部选中 |Ctrl+A |
|删除 |Delete |
|上滚行 |Ctrl+↑ |
|下滚行 |Ctrl+↓ |
|保存 |Ctrl+S |
|全部保存 |Ctrl+Shift+S |

# 重构 

下面的快捷键是重构里面常用的，一般重构的快捷键都是Alt+Shift开头

|||
|---|---|
|Alt+Shift+R |重命名 |
|Alt+Shift+M |抽取方法 |
|Alt+Shift+C |修改函数结构(比较实用,有N个函数调用了这个方法,修改一次搞定)|
|Alt+Shift+L |抽取本地变量( 可以直接把一些魔法数字和字符串抽取成一个变量,尤其是多处调用的时候)|
|Alt+Shift+F |把Class中的local变量变为field变量|
|Alt+Shift+I |内联| 
|Alt+Shift+V |移动函数和变量| 
|Alt+Shift+Z/Y |重构的后悔药(Undo)|





