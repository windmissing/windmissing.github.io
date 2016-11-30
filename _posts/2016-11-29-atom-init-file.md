---
layout: post
title:  "atom init文件"
category: [opensource]
tags: [atom]
---

 > When Atom finishes loading, it will evaluate `init.coffee` in your `%USERPROFILE%\.atom` directory, giving you a chance to run CoffeeScript code to make customizations. Code in this file has full access to [Atom's API](https://atom.io/docs/api/latest). If customizations become extensive, consider creating a package, which we will cover in [Package: Word Count](http://flight-manual.atom.io/hacking-atom/sections/package-word-count).  

Atom加载完成后，会读取你的`%USERPROFILE%\.atom`路径下的`init.coffee`文件，并运行里的CoffeeScript代码来实现定制化。这个文件中的代码对[Atom的API](https://atom.io/docs/api/latest)拥有完整的权限。如果有大量的定制化，考虑把它作成一个package。这部分内容将会在[Package: Word Count](http://flight-manual.atom.io/hacking-atom/sections/package-word-count)中提到。  

<!-- more -->

 > You can open the `init.coffee` file in an editor from the *File > Init Script* menu. This file can also be named `init.js` and contain JavaScript code.  

你可以使用编辑器的*文件->初始化脚本*打开`init.coffee`文件。这个文件也可以被命名为`init.js`并使用Javascript代码。  

 > For example, if you have the Audio Beep configuration setting enabled, you could add the following code to your `init.coffee` file to have Atom greet you with an audio beep every time it loads:  

举个例子，比如你要使用蜂鸣声的配制，你可以把以下代码下到你的`init.coffee`文件中，这样，atom每次加载后都会用蜂鸣声向你问好。  

```
atom.beep()
```

 > Because `init.coffee` provides access to Atom's API, you can use it to implement useful commands without creating a new package or extending an existing one. Here's a command which uses the [Selection API](https://atom.io/docs/api/latest/Selection) and [Clipboard API](https://atom.io/docs/api/latest/Clipboard) to construct a Markdown link from the selected text and the clipboard contents as the URL:

由于`init.coffee`文件能够访问Atom的API，你可以直接使用这些API实现成你想要的命令，而不需要创建或者扩展一个package。以下这个命令使用了[Selection API](https://atom.io/docs/api/latest/Selection)和[Clipboard API](https://atom.io/docs/api/latest/Clipboard)，用于把选中的文本和剪切版的内容构造成Markdown的链接URL：

```
atom.commands.add 'atom-text-editor', 'markdown:paste-as-link', ->
  return unless editor = atom.workspace.getActiveTextEditor()

  selection = editor.getLastSelection()
  clipboardText = atom.clipboard.read()

  selection.insertText("[#{selection.getText()}](#{clipboardText})")
```

 > Now, reload Atom and use the [Command Palette](http://flight-manual.atom.io/getting-started/sections/atom-basics/#command-palette) to execute the new command, "Markdown: Paste As Link", by name. And if you'd like to trigger the command via a keyboard shortcut, you can define a [keybinding for the command](http://flight-manual.atom.io/using-atom/sections/basic-customization/#customizing-keybindings).
 
 现在，重新加载Atom，使用[命令行面板](http://flight-manual.atom.io/getting-started/sections/atom-basics/#command-palette)执行这个新命令"Markdown: Paste As Link"。如果要通过快捷键触发这个命令，可以为这个命令[绑定一个快捷键](http://flight-manual.atom.io/using-atom/sections/basic-customization/#customizing-keybindings)。