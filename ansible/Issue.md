## 1,unknow locale: UTF-8  

```
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: ValueError: unknown locale: UTF-8
fatal: [tvt1003]: FAILED! => {"msg": "Unexpected failure during module execution.", "stdout": ""}
```
解决办法：  
在~/.bash_profile文件中添加以下内容  
```
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```
然后运行
```
$ source ~/.bash_profile
```