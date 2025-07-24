# python学习
设置环境变量
```shell
python -m venv .venv
```
执行上述的命令就会生成.venv的私有环境
![img.png](files/img.png)

* .venv的作用


* 可以使用以下命令导出依赖清单
> pip freeze > requirements.txt

* 在新的环境中可以批量导入依赖
>pip install -r requirements.txt