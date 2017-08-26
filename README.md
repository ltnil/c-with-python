# python调用c

`本文参考于：《Python Cookbook》`

---
注意：
**本文件夹中的sample.c为原生底层c语言模块，以下都以这个文本作为基础，对此库进行python的封装。**


sample.c中有

1. 4个基本函数：gcd, in_mandel, divide, avg, distance
2. 一个数据结构：Point ---代表一个二维点

---
##第一种方法 运用ctypes
利用ctypes访问c代码，本人觉得此方法太繁杂麻烦，所以不作演示

----

##第二种方法 直接运用Python 扩展API编写c扩展模块
为sample.c进行python扩展要先为sample.c编写一个头文件sample.h.

python中所有对象在c中都是一个PyObject的数据类型。

定义的每一个python函数都是PyObject,带入参数都是self一个指针和args的指针.参数self在这里是用不到的
但是如果想在c中定义新的类或对象类型就可以使用了，args是python 函数调用传入的参数。

###函数介绍

PyArg_ParseTuple这个函数是用于解析python函数中的参数的。

Py_BuildValue是从c数据类型中创建出对应的Python对象。

PyBuffer_GetBuffer会尝试获取有关对象的底层内存表示的相关信息,[具体参照](https://docs.python.org/3/c-api/buffer.html?highlight=pybuffer#)。
针对数组，字节串以及其它相似的对象，Py_buffer会保存相关的数据信息，大小。当我们需要对数组高效计算通常要运用到它。
最后buffer要通过PyBuffer_Release来释放.[具体参见](https://docs.python.org/3/c-api/buffer.html)


在任何扩展模块的底部，我们都需要一个cal.c中samplemethod这样的函数表，列出定义的函数。

最后函数PyInit_sample是模块初始化的函数，在模块导入的时候会执行，它的作用就是把模块对象注册到python解释器中。

###管理不透明指针

现在我们有一个c结构图体的指针Point，但是又不想把内部暴露给python，就可以用capsule来包装这个指针。


capsule对象和c中的void指针很相似。capsule内部持有一个泛型指针以及一个标志名称。通过PyCapsule_New可以简单构建出一个capsule对象。注意要关联一个构析函数给垃圾回收。

----
##使用swig封装c代码
未做


##使用Cython封装c代码

从某种程度看，用cython创建一个扩展模块和手动编写扩展模块有些相似。但是与原生c api不一样，
我们不必再用c完成扩展模块，使用cython能让代码看上去更像python


cython需要一个pyd的文件，作用类似与c的头文件，声明你要封装的函数。

然后需要一个pyx的文件来编写你的封装c代码。

从高层来看，cython是用来模仿c的。pyd文件仅仅只是包含了c种的声明，pyx文件包含了实现。