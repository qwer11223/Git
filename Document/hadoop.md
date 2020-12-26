# 集群linux环境搭建

## linux配置ip地址
`/etc/sysconfig/network-scripts/ifvfg-ens33`
> BOOTPROTO=static  
>
> IPADDR=192.168.60.100  
> GATEWAY=192.168.60.2  
> NETMASK=255.255.255.0  
> DNS1=114.114.114.114  
> DNS2=223.5.5.5

## 配置主机名和域名映射

* 修改主机名  
`vi /etc/sysconfig/network`  
> NETWORKING=yes  
HOSTNAME=node01

* 设置ip和域名映射  
`vi /etc/hosts`
> 192.168.60.100 node01 node01.hadoop.com  
192.168.60.110 node02 node02.hadoop.com  
192.168.60.120 node03 node03.hadoop.com

## 关闭防火墙和SELinux

* 关闭防火墙
```
service iptables stop #关闭防火墙
chkconfig iptables off #禁止开机启动
```

* 关闭selinux

SELinux是linux的一种安全子系统，linux中的权限管理是针对文件的，SELinux在Linux的文件权限之外，增加了对进程的限制，进程只能在进程允许的范围内操作资源。

> selinux 工作模式  
* `enforcing` 强制模式
* `permissive` 宽容模式
* `disable` 关闭

```
#修改selinux配置文件
vi /etc/selinux/config
```


## SSH免密登陆

Secure Shell (安全外壳协议)

1. 生成公私钥对

> `ssh-keygen -t rsa ` # -t表示类型选择，采用rsa算法

2. 将公钥拷贝到远程主机
> `ssh-copy-id node01`

3. 复制node01的认证到其他节点
> `scp /root/.ssh/authorized_keys node02:/root/.ssh`

## 时钟同步

1. 所有主机和同一台主机时间保持同步
2. 通过网络，所有主机时钟与服务器保持同步
> #安装  
> yum install ntp  
>
> #启动定时任务  
> crontab -e
> 
> #在输入界面键入
> */1 * * * * /usr/sbin/ntpdate ntp4.aliyun.com;

