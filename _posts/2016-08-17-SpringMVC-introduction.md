---
layout: post
title:  "SpringMVC处理请求的流程"
category: [back-end]
tags: []
---

Spring Web MVC是一种基于Java的实现了Web MVC设计模式的请求驱动类型的轻量级Web框架，即使用了MVC架构模式的思想，将web层进行职责解耦，基于请求驱动指的就是使用请求-响应模型，框架的目的就是帮助我们简化开发，Spring Web MVC也是要简化我们日常Web开发的。  

<!-- more -->

#### Spring Web MVC能帮我们做什么

√让我们能非常简单的设计出干净的Web层和薄薄的Web层；  
√进行更简洁的Web层的开发；  
√天生与Spring框架集成（如IoC容器、AOP等）；  
√提供强大的约定大于配置的契约式编程支持；  
√能简单的进行Web层的单元测试；  
√支持灵活的URL到页面控制器的映射；  
√非常容易与其他视图技术集成，如Velocity、FreeMarker等等，因为模型数据不放在特定的API里，而是放在一个Model里（Map数据结构实现，因此很容易被其他框架使用）；  
√非常灵活的数据验证、格式化和数据绑定机制，能使用任何对象进行数据绑定，不必实现特定框架的API；  
√提供一套强大的JSP标签库，简化JSP开发；  
√支持灵活的本地化、主题等解析；  
√更加简单的异常处理；  
√对静态资源的支持；  
√支持Restful风格。  

#### Spring Web MVC处理请求的流程

Spring Web MVC框架也是一个基于请求驱动的Web框架，并且也使用了前端控制器模式来进行设计，再根据请求映射规则分发给相应的页面控制器（动作/处理器）进行处理。首先让我们整体看一下Spring Web MVC处理请求的流程：  

![](http://sishuok.com/forum/upload/2012/7/14/529024df9d2b0d1e62d8054a86d866c9__1.JPG)

其主要组件如下：  
 - 前端控制器是DispatcherServlet；  
 - 应用控制器其实拆为处理器映射器(Handler Mapping)进行处理器管理和视图解析器(View Resolver)进行视图管理；  
 - 页面控制器/动作/处理器为Controller接口（仅包含ModelAndView handleRequest(request, response) 方法）的实现（也可以是任何的POJO类）；  

具体执行步骤如下：  
1、  首先用户发送请求————>前端控制器，前端控制器根据请求信息（如URL）来决定选择哪一个页面控制器进行处理并把请求委托给它，即以前的控制器的控制逻辑部分；图2-1中的1、2步骤；  
2、  页面控制器接收到请求后，进行功能处理，首先需要收集和绑定请求参数到一个对象，这个对象在Spring Web MVC中叫命令对象，并进行验证，然后将命令对象委托给业务对象进行处理；处理完毕后返回一个ModelAndView（模型数据和逻辑视图名）；图2-1中的3、4、5步骤；  
3、  前端控制器收回控制权，然后根据返回的逻辑视图名，选择相应的视图进行渲染，并把模型数据传入以便视图渲染；图2-1中的步骤6、7；  
4、  前端控制器再次收回控制权，将响应返回给用户，图2-1中的步骤8；至此整个结束。  

下面将依次介绍这几个步骤。

#### 请求如何给前端控制器？

在web.xml中进行部署描述  

```xml
<servlet>  
    <servlet-name>aaa</servlet-name>  
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>  
    <load-on-startup>1</load-on-startup>  
</servlet>  
<servlet-mapping>  
    <servlet-name>aaa</servlet-name>  
    <url-pattern>/</url-pattern>  
</servlet-mapping>  
```
load-on-startup：表示启动容器时初始化该Servlet；  
url-pattern：表示哪些请求交给Spring Web MVC处理， “/” 是用来定义默认servlet映射的。也可以如“*.html”表示拦截所有以html为扩展名的请求。  
自此请求已交给Spring Web MVC框架处理。   

#### 前端控制器如何根据请求信息选择页面控制器进行功能处理？
需要配置HandlerMapping进行映射。例如上文中配置了`<servlet-name>aaa</servlet-name>`，那么默认配置文件为**WEB-INF/aaa-servlet.xml**。  
这个配置文件将在下方中多次用到。

```xml
<!-- HandlerMapping -->  
<bean class="org.springframework.web.servlet.handler.BeanNameUrlHandlerMapping"/>
```
BeanNameUrlHandlerMapping提供默认的注解映射，表示将请求的URL和Bean名字映射，如URL为 “上下文/hello”，则Spring配置文件必须有一个名字为“/hello”的Bean，上下文默认忽略。

```xml
<!-- 处理器 -->  
<bean name="/hello" class="projectname.web.controller.HelloWorldController"/> 
```
projectname.web.controller.HelloWorldController就是页面控制器的类名。  

#### 页面控制器

在WEB-INF/aaa-servlet.xml配置这样一句话：

```xml
<!-- HandlerAdapter -->  
<bean class="org.springframework.web.servlet.mvc.SimpleControllerHandlerAdapter"/>
```
SimpleControllerHandlerAdapter：表示所有实现了org.springframework.web.servlet.mvc.Controller接口的Bean可以作为Spring Web MVC中的处理器。如果需要其他类型的处理器可以通过实现HadlerAdapter来解决。  
在配置文件中配置了这句话之后，只要projectname.web.controller.HelloWorldController继承并实现org.springframework.web.servlet.mvc.Controller，就可以成为页面控制器。  

```java
package projectname.web.controller;  
import javax.servlet.http.HttpServletRequest;  
import javax.servlet.http.HttpServletResponse;  
import org.springframework.web.servlet.ModelAndView;  
import org.springframework.web.servlet.mvc.Controller;  
public class HelloWorldController implements Controller {  
    @Override  
    public ModelAndView handleRequest(HttpServletRequest req, HttpServletResponse resp) throws Exception {  
       //1、收集参数、验证参数  
       //2、绑定参数到命令对象  
       //3、将命令对象传入业务对象进行业务处理  
       //4、选择下一个页面  
       ModelAndView mv = new ModelAndView();  
       //添加模型数据 可以是任意的POJO对象  
       mv.addObject("message", "Hello World!");  
       //设置逻辑视图名，视图解析器会根据该名字解析到具体的视图页面  
       mv.setViewName("hello");  
       return mv;  
    }  
}  
```
作为页面控制器，HelloWorldController必须做以下这些事情：  
1.继承并实现Controller接口
2.重载handleRequest，完成相应的功能处理，比如收集参数、验证参数、绑定参数到命令对象、将命令对象传入业务对象进行业务处理、最后返回ModelAndView对象  

#### 如何支持多种页面控制器呢？
配置HandlerAdapter从而支持多种类型的页面控制器

#### 如何页面控制器如何使用业务对象？
可以预料到，肯定利用Spring IoC容器的依赖注入功能  

#### 页面控制器如何返回模型数据？
使用ModelAndView返回。  
ModelAndView：包含了视图要实现的模型数据和逻辑视图名；  
`mv.addObject("message", "Hello World!");`：表示添加模型数据，此处可以是任意POJO对象；
`mv.setViewName("hello");`：表示设置逻辑视图名为“hello”，视图解析器会将其解析为具体的视图。

#### 前端控制器如何根据页面控制器返回的逻辑视图名选择具体的视图进行渲染？

回到配置文件WEB-INF/aaa-servlet.xml，配置ViewResolver

```xml
<!-- ViewResolver -->  
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">  
    <property name="viewClass" value="org.springframework.web.servlet.view.JstlView"/>  
    <property name="prefix" value="/WEB-INF/jsp/"/>  
    <property name="suffix" value=".jsp"/>  
</bean>  
```
InternalResourceViewResolver：用于支持Servlet、JSP视图解析；   
viewClass：表示JSP模板页面需要使用JSTL标签库，classpath中必须包含jstl的相关jar包；  
prefix和suffix：查找视图页面的前缀和后缀（前缀[逻辑视图名]后缀）。  
本例中传进来的逻辑视图名为hello，则该jsp视图页面应该存放在`WEB-INF/jsp/hello.jsp`；  
    
#### 不同的视图技术如何使用相应的模型数据？
因为Model是一个Map数据结构，很容易支持其他视图技术

#### 从前端控制器的角度看Spring Web MVC处理请求的流程

由于前端控制器是处于最上层、直接与用户交互的部件，又起到前端控制的作用，从前端控制器的角度把这个过程再理一遍。  
DispatcherServlet即前端控制。  
![](http://sishuok.com/forum/upload/2012/7/14/57ea9e7edeebd5ee2ec0cf27313c5fb6__2.JPG)  
架构图对应的DispatcherServlet核心代码如下：
 
```java
//前端控制器分派方法  
protected void doDispatch(HttpServletRequest request, HttpServletResponse response) throws Exception {  
        HttpServletRequest processedRequest = request;  
        HandlerExecutionChain mappedHandler = null;  
        int interceptorIndex = -1;  
  
        try {  
            ModelAndView mv;  
            boolean errorView = false;  
  
            try {  
                   //检查是否是请求是否是multipart（如文件上传），如果是将通过MultipartResolver解析  
                processedRequest = checkMultipart(request);  
                   //步骤2、请求到处理器（页面控制器）的映射，通过HandlerMapping进行映射  
                mappedHandler = getHandler(processedRequest, false);  
                if (mappedHandler == null || mappedHandler.getHandler() == null) {  
                    noHandlerFound(processedRequest, response);  
                    return;  
                }  
                   //步骤3、处理器适配，即将我们的处理器包装成相应的适配器（从而支持多种类型的处理器）  
                HandlerAdapter ha = getHandlerAdapter(mappedHandler.getHandler());  
  
                  // 304 Not Modified缓存支持  
                //此处省略具体代码  
  
                // 执行处理器相关的拦截器的预处理（HandlerInterceptor.preHandle）  
                //此处省略具体代码  
  
                // 步骤4、由适配器执行处理器（调用处理器相应功能处理方法）  
                mv = ha.handle(processedRequest, response, mappedHandler.getHandler());  
  
                // Do we need view name translation?  
                if (mv != null && !mv.hasView()) {  
                    mv.setViewName(getDefaultViewName(request));  
                }  
  
                // 执行处理器相关的拦截器的后处理（HandlerInterceptor.postHandle）  
                //此处省略具体代码  
            }  
            catch (ModelAndViewDefiningException ex) {  
                logger.debug("ModelAndViewDefiningException encountered", ex);  
                mv = ex.getModelAndView();  
            }  
            catch (Exception ex) {  
                Object handler = (mappedHandler != null ? mappedHandler.getHandler() : null);  
                mv = processHandlerException(processedRequest, response, handler, ex);  
                errorView = (mv != null);  
            }  
  
            //步骤5 步骤6、解析视图并进行视图的渲染  
//步骤5 由ViewResolver解析View（viewResolver.resolveViewName(viewName, locale)）  
//步骤6 视图在渲染时会把Model传入（view.render(mv.getModelInternal(), request, response);）  
            if (mv != null && !mv.wasCleared()) {  
                render(mv, processedRequest, response);  
                if (errorView) {  
                    WebUtils.clearErrorRequestAttributes(request);  
                }  
            }  
            else {  
                if (logger.isDebugEnabled()) {  
                    logger.debug("Null ModelAndView returned to DispatcherServlet with name '" + getServletName() +  
                            "': assuming HandlerAdapter completed request handling");  
                }  
            }  
  
            // 执行处理器相关的拦截器的完成后处理（HandlerInterceptor.afterCompletion）  
            //此处省略具体代码  
  
  
        catch (Exception ex) {  
            // Trigger after-completion for thrown exception.  
            triggerAfterCompletion(mappedHandler, interceptorIndex, processedRequest, response, ex);  
            throw ex;  
        }  
        catch (Error err) {  
            ServletException ex = new NestedServletException("Handler processing failed", err);  
            // Trigger after-completion for thrown exception.  
            triggerAfterCompletion(mappedHandler, interceptorIndex, processedRequest, response, ex);  
            throw ex;  
        }  
  
        finally {  
            // Clean up any resources used by a multipart request.  
            if (processedRequest != request) {  
                cleanupMultipart(processedRequest);  
            }  
        }  
    }  
```

核心架构的具体流程步骤如下：  
1、  首先用户发送请求——>DispatcherServlet，前端控制器收到请求后自己不进行处理，而是委托给其他的解析器进行处理，作为统一访问点，进行全局的流程控制；  
2、  DispatcherServlet——>HandlerMapping， HandlerMapping将会把请求映射为HandlerExecutionChain对象（包含一个Handler处理器（页面控制器）对象、多个HandlerInterceptor拦截器）对象，通过这种策略模式，很容易添加新的映射策略；  
3、  DispatcherServlet——>HandlerAdapter，HandlerAdapter将会把处理器包装为适配器，从而支持多种类型的处理器，即适配器设计模式的应用，从而很容易支持很多类型的处理器；  
4、  HandlerAdapter——>处理器功能处理方法的调用，HandlerAdapter将会根据适配的结果调用真正的处理器的功能处理方法，完成功能处理；并返回一个ModelAndView对象（包含模型数据、逻辑视图名）；  
5、  ModelAndView的逻辑视图名——> ViewResolver， ViewResolver将把逻辑视图名解析为具体的View，通过这种策略模式，很容易更换其他视图技术；  
6、  View——>渲染，View会根据传进来的Model模型数据进行渲染，此处的Model实际是一个Map数据结构，因此很容易支持其他视图技术；  
7、返回控制权给DispatcherServlet，由DispatcherServlet返回响应给用户，到此一个流程结束。  
 
此处我们只是讲了核心流程，没有考虑拦截器、本地解析、文件上传解析等，后边再细述。  
 
------------------

本文内容非原创，来自http://jinnianshilongnian.iteye.com/blog/1594806  
排版做了些调整  
如有侵权，请告知
