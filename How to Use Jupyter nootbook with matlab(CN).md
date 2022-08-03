

### 1. 安装python, matlab

需要安装 matlab 软件和 Python。

> matlab 目前仅支持 python3.8 及以下

### 2. 安装 matlab_kernel

```
pip install matlab_kernal
```

### 3. 配置 matlab_kernal

1. cd 到 Matlab 的安装目录 (Windows 为 C:\Program Files\MATLAB)
2. cd 到 MATLAB\\(当前版本目录)\extern\engines\python
3. 执行 `python setup.py install` 命令

### 4. 安装 jupyter notebook 或 jupyter lab

```
pip install notebook
```

### 5. 启动 jupyter notebook

```
jupyter notebook
```

在浏览器中打开 jupyter notebook 在 kernel 中可以选择 malab, 此时便可以像使用python 一样在 jupyter notebook 中使用 matlab了。