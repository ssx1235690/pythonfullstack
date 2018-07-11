#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 11:47
# @Author  : sxsong
# @Site    : 
# @File    : 22-day事件驱动模型.py
# @Software: PyCharm

from PIL import Image
# http://www.cnblogs.com/yuanchenqi/articles/5722574.html

# 1
# IO模型前戏准备
# 在进行解释之前，首先要说明几个概念：
#
# 用户空间和内核空间
# 进程切换
# 进程的阻塞
# 文件描述符
# 缓存
# I / O
# 用户空间与内核空间
# 现在操作系统都是采用虚拟存储器，那么对32位操作系统而言，它的寻址空间（虚拟存储空间）为4G（2
# 的32次方）。
# 操作系统的核心是内核，独立于普通的应用程序，可以访问受保护的内存空间，也有访问底层硬件设备的所有权限。
# 为了保证用户进程不能直接操作内核（kernel），保证内核的安全，操心系统将虚拟空间划分为两部分，一部分为内核空间，一部分为用户空间。
# 针对linux操作系统而言，将最高的1G字节（从虚拟地址0xC0000000到0xFFFFFFFF），供内核使用，称为内核空间，而将较低的3G字节（从虚拟地址0x00000000到0xBFFFFFFF），供各个进程使用，称为用户空间。
#
# 进程切换
# 为了控制进程的执行，内核必须有能力挂起正在CPU上运行的进程，并恢复以前挂起的某个进程的执行。这种行为被称为进程切换，这种切换是由操作系统来完成的。因此可以说，任何进程都是在操作系统内核的支持下运行的，是与内核紧密相关的。
# 从一个进程的运行转到另一个进程上运行，这个过程中经过下面这些变化：
#
# 保存处理机上下文，包括程序计数器和其他寄存器。
#
# 更新PCB信息。
#
# 把进程的PCB移入相应的队列，如就绪、在某事件阻塞等队列。
#
# 选择另一个进程执行，并更新其PCB。
#
# 更新内存管理的数据结构。
#
# 恢复处理机上下文。
# 注：总而言之就是很耗资源的
#
# 进程的阻塞
# 正在执行的进程，由于期待的某些事件未发生，如请求系统资源失败、等待某种操作的完成、新数据尚未到达或无新工作做等，则由系统自动执行阻塞原语(
#     Block)，使自己由运行状态变为阻塞状态。可见，进程的阻塞是进程自身的一种主动行为，也因此只有处于运行态的进程（获得CPU），
# 才可能将其转为阻塞状态。当进程进入阻塞状态，是不占用CPU资源的。
#
# 文件描述符fd
# 文件描述符（File
# descriptor）是计算机科学中的一个术语，是一个用于表述指向文件的引用的抽象化概念。
# 文件描述符在形式上是一个非负整数。实际上，它是一个索引值，指向内核为每一个进程所维护的该进程打开文件的记录表。
# 当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。在程序设计中，一些涉及底层的程序编写往往会围绕着文件描述符展开。
# 但是文件描述符这一概念往往只适用于UNIX、Linux这样的操作系统。
#
# 缓存
# I / O
# 缓存
# I / O
# 又被称作标准
# I / O，大多数文件系统的默认
# I / O
# 操作都是缓存
# I / O。在
# Linux
# 的缓存
# I / O
# 机制中，操作系统会将
# I / O
# 的数据缓存在文件系统的页缓存（ page
# cache ）中，也就是说，数据会先被拷贝到操作系统内核的缓冲区中，然后才会从操作系统内核的缓冲区拷贝到应用程序的地址空间。用户空间没法直接访问内核空间的，内核态到用户态的数据拷贝
#
# 思考：为什么数据一定要先到内核区，直接到用户内存不是更直接吗？
# 缓存
# I / O
# 的缺点：
#
# 数据在传输过程中需要在应用程序地址空间和内核进行多次数据拷贝操作，这些数据拷贝操作所带来的
# CPU
# 以及内存开销是非常大的。
#
#
#
# 同步（synchronous） IO和异步（asynchronous） IO，阻塞（blocking） IO和非阻塞（non - blocking）IO分别是什么，到底有什么区别？
# 这个问题其实不同的人给出的答案都可能不同，比如wiki，就认为asynchronous
# IO和non - blocking
# IO是一个东西。这其实是因为不同的人的知识背景不同，并且在讨论这个问题的时候上下文(context)
# 也不相同。所以，为了更好的回答这个问题，我先限定一下本文的上下文。
# 本文讨论的背景是Linux环境下的network
# IO。
#
# Stevens在文章中一共比较了五种IO
# Model：
#
############### blocking IO
############### nonblocking  IO
############## multiplexing  IO
################# signal driven IO
###################### asynchronous IO
# 由于signal driven
# IO在实际中并不常用，所以我这只提及剩下的四种IO  Model。
# 再说一下IO发生时涉及的对象和步骤。
# 对于一个network
# IO(这里我们以read举例)，它会涉及到两个系统对象，一个是调用这个IO的process( or thread)，另一个就是系统内核(kernel)。当一个read操作发生时，它会经历两个阶段：
# 1 等待数据准备(Waiting for the data to be ready)
# 2 将数据从内核拷贝到进程中(Copying the data from the kernel to the process)
# 记住这两点很重要，因为这些IO
# Model的区别就是在两个阶段上各有不同的情况。
#
######################### 2   blocking  IO （阻塞IO） ####################################

im = Image.open(r"C:\Users\ronglian\pythonfullstack\picture\blockingIO.png")
im.show()
# 当用户进程调用了recvfrom这个系统调用，kernel就开始了IO的第一个阶段：准备数据。对于network io来说，
# 很多时候数据在一开始还没有到达（比如，还没有收到一个完整的UDP包），这个时候kernel就要等待足够的数据到来。
# 而在用户进程这边，整个进程会被阻塞。当kernel一直等到数据准备好了，它就会将数据从kernel中拷贝到用户内存，
# 然后kernel返回结果，用户进程才解除block的状态，重新运行起来。
# 所以，blocking IO的特点就是在IO执行的两个阶段都被block了。

##################### 3. noblocking IO #################################################
im = Image.open(r"C:\Users\ronglian\pythonfullstack\picture\noblockingIO.png")
im.show()

# 从图中可以看出，当用户进程发出read操作时，如果kernel中的数据还没有准备好，那么它并不会block用户进程，而是立刻返回一个error。
# 从用户进程角度讲 ，它发起一个read操作后，并不需要等待，而是马上就得到了一个结果。用户进程判断结果是一个error时，
# 它就知道数据还没有准备好，于是它可以再次发送read操作。一旦kernel中的数据准备好了，并且又再次收到了用户进程的system call，
# 那么它马上就将数据拷贝到了用户内存，然后返回。
# 所以，用户进程其实是需要不断的主动询问kernel数据好了没有。
#  注意：
#  在网络IO时候，非阻塞IO也会进行recvform系统调用，检查数据是否准备好，与阻塞IO不一样，”非阻塞将大的整片时间的阻塞分成N多的小的阻塞,
# 所以进程不断地有机会 ‘被’ CPU光顾”。即每次recvform系统调用之间，cpu的权限还在进程手中，这段时间是可以做其他事情的，
#  也就是说非阻塞的recvform系统调用调用之后，进程并没有被阻塞，内核马上返回给进程，如果数据还没准备好，此时会返回一个error。
# 进程在返回之后，可以干点别的事情，然后再发起recvform系统调用。重复上面的过程，循环往复的进行recvform系统调用。这个过程通常被称之为轮询。
# 轮询检查内核数据，直到数据准备好，再拷贝数据到进程，进行数据处理。需要注意，拷贝数据整个过程，进程仍然是属于阻塞的状态。

#################### IO 多路复用 ########################################

# IO multiplexing这个词可能有点陌生，但是如果我说select，epoll，大概就都能明白了。有些地方也称这种IO方式为event  driven IO。
# 我们都知道，select / epoll的好处就在于单个process就可以同时处理多个网络连接的IO。
# 它的基本原理就是select / epoll这个function会不断的轮询所负责的所有socket，当某个socket有数据到达了，就通知用户进程。它的流程如图：

im = Image.open(r"C:\Users\ronglian\pythonfullstack\picture\multiplexingIO.png")
im.show()

#  当用户进程调用了select，那么整个进程会被block，而同时，kernel会“监视”所有select负责的socket，当任何一个socket中的数据准备好了，
# select就会返回。这个时候用户进程再调用read操作，将数据从kernel拷贝到用户进程。
# 这个图和blocking IO的图其实并没有太大的不同，事实上，还更差一些。因为这里需要使用两个system call (select 和 recvfrom)，
# 而blocking IO只调用了一个system call (recvfrom)。但是，用select的优势在于它可以同时处理多个connection。（多说一句。所以，
# 如果处理的连接数不是很高的话，使用select/epoll的web server不一定比使用multi-threading + blocking IO的web server性能更好，
# 可能延迟还更大。select/epoll的优势并不是对于单个连接能处理得更快，而是在于能处理更多的连接。）
# 在IO multiplexing Model中，实际中，对于每一个socket，一般都设置成为non-blocking，但是，如上图所示，整个用户的process其实是一直被block的。
# 只不过process是被select这个函数block，而不是被socket IO给block。
#
# 注意1：select函数返回结果中如果有文件可读了，那么进程就可以通过调用accept()或recv()来让kernel将位于内核中准备到的数据copy到用户区。
#
# 注意2: select的优势在于可以处理多个连接，不适用于单个连接


################################## 5  Asynchronous I/O（异步IO）###################################
im = Image.open(r"C:\Users\ronglian\pythonfullstack\picture\asynchronousIO.png")
im.show()

# 用户进程发起read操作之后，立刻就可以开始去做其它的事。而另一方面，从kernel的角度，当它受到一个asynchronous read之后，
# 首先它会立刻返回，所以不会对用户进程产生任何block。然后，kernel会等待数据准备完成，然后将数据拷贝到用户内存，当这一切都完成之后，
# kernel会给用户进程发送一个signal，告诉它read操作完成了。
#
#       到目前为止，已经将四个IO Model都介绍完了。现在回过头来回答最初的那几个问题：blocking和non-blocking的区别在哪，synchronous IO和asynchronous IO的区别在哪。
# 先回答最简单的这个：blocking vs non-blocking。前面的介绍中其实已经很明确的说明了这两者的区别。调用blocking IO会一直block住对应的进程直到操作完成，
# 而non-blocking IO在kernel还准备数据的情况下会立刻返回。
#
# 在说明synchronous IO和asynchronous IO的区别之前，需要先给出两者的定义。Stevens给出的定义（其实是POSIX的定义）是这样子的：
#     A synchronous I/O operation causes the requesting process to be blocked until that I/O operationcompletes;
#     An asynchronous I/O operation does not cause the requesting process to be blocked;
#       两者的区别就在于synchronous IO做”IO operation”的时候会将process阻塞。按照这个定义，之前所述的blocking IO，non-blocking IO，
# IO multiplexing都属于synchronous IO。有人可能会说，non-blocking IO并没有被block啊。这里有个非常“狡猾”的地方，定义中所指的”IO operation”是指真实的IO操作，
# 就是例子中的recvfrom这个system call。non-blocking IO在执行recvfrom这个system call的时候，如果kernel的数据没有准备好，这时候不会block进程。
# 但是，当kernel中数据准备好的时候，recvfrom会将数据从kernel拷贝到用户内存中，这个时候进程是被block了，在这段时间内，进程是被block的。
# 而asynchronous IO则不一样，当进程发起IO 操作之后，就直接返回再也不理睬了，直到kernel发送一个信号，告诉进程说IO完成。在这整个过程中，进程完全没有被block。
#
#        注意：由于咱们接下来要讲的select，poll，epoll都属于IO多路复用，而IO多路复用又属于同步的范畴，故，epoll只是一个伪异步而已。
#
# ########################各个IO Model的比较如图所示： 22-day5中io模型比较###################################################

im = Image.open(r"C:\Users\ronglian\pythonfullstack\picture\22-day5中io模型比较.png")
im.show()
# 经过上面的介绍，会发现non - blocking
# IO和asynchronous
# IO的区别还是很明显的。在non - blocking
# IO中，虽然进程大部分时间都不会被block，但是它仍然要求进程去主动的check，并且当数据准备完成以后，也需要进程主动的再次调用recvfrom来将数据拷贝到用户内存。而asynchronous
# IO则完全不同。它就像是用户进程将整个IO操作交给了他人（kernel）完成，然后他人做完后发信号通知。在此期间，用户进程不需要去检查IO操作的状态，也不需要主动的去拷贝数据。


################################6 select poll epoll IO多路复用介绍 ############################################
# 首先列一下，sellect、poll、epoll三者的区别
#
# select
# select最早于1983年出现在4.2BSD中，它通过一个select()系统调用来监视多个文件描述符的数组，当select()返回后，该数组中就绪的文件描述符便会被内核修改标志位，使得进程可以获得这些文件描述符从而进行后续的读写操作。
# select目前几乎在所有的平台上支持
# 　
# select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。
# 　
# 另外，select()所维护的存储大量文件描述符的数据结构，随着文件描述符数量的增大，其复制的开销也线性增长。同时，由于网络响应时间的延迟使得大量TCP连接处于非活跃状态，但调用select()会对所有socket进行一次线性扫描，所以这也浪费了一定的开销。
# poll
# 它和select在本质上没有多大差别，但是poll没有最大文件描述符数量的限制。
# 一般也不用它，相当于过渡阶段
#
# epoll
# 直到Linux2.6才出现了由内核直接支持的实现方法，那就是epoll。被公认为Linux2.6下性能最好的多路I/O就绪通知方法。windows不支持
#
# 没有最大文件描述符数量的限制。
# 比如100个连接，有两个活跃了，epoll会告诉用户这两个两个活跃了，直接取就ok了，而select是循环一遍。
#
# （了解）epoll可以同时支持水平触发和边缘触发（Edge Triggered，只告诉进程哪些文件描述符刚刚变为就绪状态，它只说一遍，如果我们没有采取行动，那么它将不会再次告知，这种方式称为边缘触发），理论上边缘触发的性能要更高一些，但是代码实现相当复杂。
# 另一个本质的改进在于epoll采用基于事件的就绪通知方式。在select/poll中，进程只有在调用一定的方法后，内核才对所有监视的文件描述符进行扫描，而epoll事先通过epoll_ctl()来注册一个文件描述符，一旦基于某个文件描述符就绪时，内核会采用类似callback的回调机制，迅速激活这个文件描述符，当进程调用epoll_wait()时便得到通知。
#
# 所以市面上上见到的所谓的异步IO，比如nginx、Tornado、等，我们叫它异步IO，实际上是IO多路复用。


