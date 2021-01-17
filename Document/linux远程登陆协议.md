目前我们常见的远程管理控制方式主要有以下几种：

1. `RDP(remote desktop protocol)协议`　　远程桌面协议，我们常用的windows操作系统就是的远程桌面管理就是基于该协议的，更多有关RDP协议的可以查看百度百科 RDP 

2. `telnet　　CLI (command-line interface ,命令行界面)`界面下的远程管理工具，因为其历史非常悠久，几乎所有的操作系统都有该工具(telnet在传送数据时是通过明文传输的，没有加密，所以现在几乎都不会使用telnet来进行远程管理了)　　telnet

3. `SSH(Secure Shell)协议`　　CLI界面下的远程管理工具，几乎所有的操作系统都有(区别于telnet，SSH在进行数据传送时会对数据进行加密，所以SSH是比较安全的协议)，几乎所有的类UNIX操作系统都是采用SSH来进行远程管理(linux、BSD、Mac OS等)。　　SSH

4. `RFB(Remote FrameBuffer)协议`　　图形化远程管理协议，`VNC(Virtual Network Computing)`就是基于该协议的，上面讲的SSH在类UNIX下是CLI界面常用的远程管理方式，那么在类UNIX操作系统中，同样存在图形化的远程管理工具，VNC就是类UNIX系统下常用的图形化远程管理工具