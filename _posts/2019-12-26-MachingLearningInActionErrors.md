---
layout: post
title:  "机器学习实战代码勘误"
category: [Machine Learning]
tags: []
---

2.2.1第二段代码  
L2：`datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')` -> `datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')`

2.2.5 Listing 2.5
L5:`ffMiles = float(raw_input("frequent flier miles earned per year?"))` -> `ffMiles = float(input("frequent flier miles earned per year?"))`  
L6、L7同上  

<!-- more -->

3.2.2 Listing 3.6  
L3: `firstStr = myTree.keys()[0]` -> `firstStr = myTree.keys()[0]`  
L13: `firstStr = myTree.keys()[0]` -> `firstStr = myTree.keys()[0]`  

3.3.2 Listing 3.9  
L4: `fw = open(filename,'w')`->`fw = open(filename,'wb')`  
L10: `fr = open(filename)`->`fr = open(filename, 'rb)`  

4.6.1第二段代码  
L2:`regEx = re.compile('\\W*')` -> `regEx = re.compile('\\W+')`

4.6.2 Listing 4.5  
L13:`wordList = textParse(open('email/ham/%d.txt' % i, encoding='ISO-8859-15').read())`->`wordList = textParse(open('email/ham/%d.txt' % i).read())`

4.7.1 第一段代码  
在cmd下，将路径切换到python安装路径的scripts文件下，例如：C:\Users\xxx\anaconda3\Scripts，（很关键）通过pip install feedparser进行安装   
这个方法亲测不成功，feedParser下不下来   

6.2.1 公式2  
公式中的ahpha和a可以看作是同一个符号

6.2.1 公式4、公式5  
`i-1` -> `i=1`

8.2 公式2
分子少了一个平方符号

9.2 Listing9.1  
L13: `mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0],:][0]` -> `mat0 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]`  
L14同上

13.2.2 Listing 13.1  
L6：`datArr = [map(float,line) for line in stringArr]` -> `datArr = [list(map(float,line)) for line in stringArr]`