---
layout: post
title:  "【转】VMware 12安装虚拟机Mac OS X 10.10(VMware12安装/共享文件夹)"
category: [ios]
tags: [ios, vmare, maxos]
---

#### 推荐电脑配置
1：Inter I5及以上 (A卡请自行百度大神解决方案)  
    必须开启CPU虚拟化：开机进入BIOS--->Intel Virtualization Technology--->修改为Enabled
    参考：[联想笔记本电脑如何打开Intel 虚拟化技术]( http://jingyan.baidu.com/article/91f5db1b3002831c7f05e3b0.html)  
2：内存 4G以上(IOS开发，安装Xcode，推荐12G及以上)  
3：硬盘现在笔记本都能满足需求。40G及以上  

<!-- more -->

#### 工具/原料
1.VMware Workstation 12 (这个版本仅适合64位Win7或更高版本操作系统)   
[下载链接](http://pan.baidu.com/s/1pJEdIpd)， 密码：zafx  
2.unlocker 203（for OS X 插件补丁）  
[下载链接](http://pan.baidu.com/s/1pJnFrmj)，密码：kpen  
Mac OS X 10.10镜像   
[下载链接](http://pan.baidu.com/s/1bn6uESZ)，密码：us9p

#### 一：虚拟机的安装
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638310.png)  
##### 1.双击程序自动解压，解压完成后进入安装向导。
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638311.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638312.png)  
Error解决方案：右键-->以管理员身份运行  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638313.png)  
解压完成后桌面右下角出现：  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638315.png)  

##### 2.安装向导，点击下一步
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638317.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638318.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638319.png)  

##### 3.点击更新修改路径。
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638320.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638321.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638322.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638323.png)
点击安装，然后静静的等待......  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638324.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638325.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638326.png)
安装完成，输入产品Key   VMware Workstation 12 Pro key/注册码：  
VY1DU-2VXDH-08DVQ-PXZQZ-P2KV8  
VF58R-28D9P-0882Z-5GX7G-NPUTF  
YG7XR-4GYEJ-4894Y-VFMNZ-YA296  
5A02H-AU243-TZJ49-GTC7K-3C61N  
或者百度直接搜索： vmware workstation 12 密钥  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638327.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638328.png)  
之后可能会弹出一个窗口：(不用理会，直接关掉)  

##### 4.双击VMware Workstation Pro ，点击工具栏上 [帮助]--->[关于VMware Workstation]
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638329.png)  
至此VMware Workstation 已经安装完成。  

#### 二：插件安装(unlocker 203)

目的：在VMware Workstation虚拟机中能够安装Apple Mac系统  

##### 1.步骤一完成后，打开任务管理器，找到服务项，选择按名称排序，将框中四项全部停止运行。
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638330.png)  

##### 2.然后打开下载的插件，解压unlock203.zip文件，找到 unlock203win-install.cmd，右键以管理员身份运行，等待运行完即可。（完成这一步vmware才能识别OS X）  
注意：unlock203.zip 的路径中不能带中文  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638331.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638332.png)
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638333.png)  

##### 3.运行插件之前 使用VMware Workstation 选中客户机操作系统(没有App Mac)
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638334.png)  
运行插件之后，我们可以新建App Mac虚拟机  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638335.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193638336.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639337.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639338.png)  
**Error：此主机不支持64位客户机操作系统，此系统无法运行**  
1：确认BIOS/固件设置中启用了 Inter VT-x并禁用了'可信执行'。  
2：如果这两项BIOS/固件设置有一项已更改，请重新启动主机。  
3：如果您在安装 VMware Workstation   之后从未重新启动主机，请重新启动。
4：将主机的BIOS/固件更新至最新版本。   
Hyper服务和VM不能同时开启。前提先禁用Hyper服务，具体方式参考下面步骤  
可能原因：CPU不支持虚拟化技术/还有另外一种情况：CPU支持虚拟化技术，但BIOS没有启动虚拟化技术支持。  
我们可以使用SecurAble来检测CPU是否支持虚拟化。  
官方下载网址：https://www.grc.com/securable.htm  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639339.png)  
我先暂时忽略这个警告，尝试新建虚拟机，看是否能运行  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639340.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639341.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639342.png)  
(因为我之前安装过Hyper，所以出现以下提示)，由此可以推断出，之前出现  
Error：此主机不支持64位客户机操作系统，此系统无法运行 也可能是这个原因  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639343.png)  
Error解决方案：  
(此命令用来设置禁用Hyper-v，以管理员身份运行)  
bcdedit /set hypervisorlaunchtype off  
(如果想再次启用Hyper-v，请运行此命令)  
bcdedit /set hypervisorlaunchtype auto  
最后，一定要重启电脑，以上两步设置才能生效  
在这里我重新安装Mac虚拟机，把之前的Mac虚拟机删掉。并去相应的安装目录删掉文件(防止重复)  
重新检测cpu是否支持虚拟化技术  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639344.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639347.png)  
其它同上。  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639348.png)  

##### 4.开启安装
我遇到了如下问题  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639350.png)  
出现这种情况，只要找到并打开安装目录下的 XXXX.vmx 文件，使用记事本打开后，在 smc.present = 'TRUE' 后添加“smc.version = 0”(建议您复制，不包括引号)后保存，问题即可解决。  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639352.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639354.png)  

##### 5.继续安装，看图
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639356.png)  
选中 以简体中文作为主要语言，回车即可  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639357.png)
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639358.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639359.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639360.png)  
然后点击左上角的磁盘工具，选择退出磁盘工具。然后在安装界面点击继续,再点击安装 以后就是初次进入系统的配置了【安装过程中最好使屏幕保持显示状态】  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639361.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639362.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639363.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639364.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639365.png)  
重新启动之后  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639366.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639367.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193639368.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640369.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640370.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640371.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640372.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640373.png)  
下面这一步 根据电脑配置情况，需要等待一段时间  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640374.png)  

##### 6.VMTool以及Darwin6.0.3的安装 以及共享文件夹。
VMWare Tools for OS X是虚拟机的一个实用工具，软件由官方开发，用虚拟机安装OS X的必备工具，软件可以增强虚拟机的显卡性能和磁盘性能，并且可以实现主机与虚拟机的文件共享，也可以把文件通过拖拽的方式在主机和虚拟机之间复制，鼠标也可以自由切换，总之，虚拟机必备。  
VMTool安装之前：无法建立共享文件夹  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640375.png)  
开始安装VMTool  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640376.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640377.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640378.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640379.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640380.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640381.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640382.png)  
共享文件夹的说明：由于虚拟机无法访问本机的硬盘，所以需要设置共享文件夹来方便虚拟机读取电脑的物理内存  

##### 1：VMware Workstation 设置  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640383.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640384.png)  

##### 2：Mac OS虚拟机设置
 2.1.确保左上角苹果标志的旁边是”Finder”  
 2.2.点击”Finder”  
 2.3.选择”偏好设置”  
 2.4.然后在 “通用” 标签下勾选”已连接服务器”  
 ![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640385.png)  
 ![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640386.png)  
![](http://www.it165.net/uploadfile/files/2015/1030/20151030193640387.png)  

[阅读原文](http://www.it165.net/os/html/201510/15384.html)
