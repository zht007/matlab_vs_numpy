
### 1. 数据生成

使用一个正弦信号，一个三角信号和一个随机杂讯合成4个信号，其中第四个信号仅为杂讯。信号图如下图所示

![下载](https://s2.loli.net/2022/07/08/NGcndemzq5Ho2ju.png)

### 2 PCA 数据分析

#### 2.1 PCA在matlab 和 python 中的调用

在 Matlab 中使用 `pca()`函数。在 python 中需要使用 sklearn.decomposition 中 import PCA 模型。**注意输入的信号的维度**

> Matlab 中PCA 中可以直接返回的三个变量[U,PC,eigenVal]
>
> * U: eigenVector
>
> * PC: Principle component
>
> * eigenVal: eigenValue
>
> sklearn 中的PCA模型是对象，初始化之后，使用 fit_transform() 得到 PC，所以
>
> * PC = pca.fit_transform(X.T) 
> * U = pca.components_
> * eigenVal = pca.explained_variance_

```python
# Matlab
[U,PC,eigenVal]=pca(X');

# Python
                    
pca = PCA()

PC = pca.fit_transform(X.T) # shape: n_features x n_components
U = pca.components_
eigenVal = pca.explained_variance_
```

我们可以把 PC 画出来，可以看到除了前两个 components 其他三个都是杂讯。如果将每个 PC 的 eigen value 得贡献画出来，可以看到，前两个PC贡献了95% 以上的信息。

 ![image-20220707175406456](https://s2.loli.net/2022/07/08/X8bQrqd6YhtsmLH.png)

在Matlab 和 Python 中分别使用 cov() 或者 np.cov() 函数计算各个信号的协方差(covariance)可以看到，除了对角线自己的方差 variance, 相互的协方差系数都十分低。

```python
# Matlab 
cov(PC)  % make sure if the PCs are uncorrelated !
---
ans =

    0.5441    0.0000    0.0000    0.0000   -0.0000
    0.0000    0.0854   -0.0000   -0.0000    0.0000
    0.0000   -0.0000    0.0307    0.0000   -0.0000
    0.0000   -0.0000    0.0000    0.0051    0.0000
   -0.0000    0.0000   -0.0000    0.0000    0.0008


# Python
print(np.round(np.cov(PC.T),5)) 
---
[[ 0.54648 -0.      -0.      -0.      -0.     ]
 [-0.       0.08668  0.      -0.       0.     ]
 [-0.       0.       0.03027  0.       0.     ]
 [-0.      -0.       0.       0.00501 -0.     ]
 [-0.       0.       0.      -0.       0.00083]]
```



#### 2.2  数据重构

只用两个最主要的 Component 对数据进行重建，可以看到如下图所示红色的为重建信号，除了最后一张无法重建杂讯之外，其他4个讯号均完美重建。

```python
# Matlab
newX = U(:,1:PCnum)*PC(:,1:PCnum)';

#Python
newX = U[:PCnum,:].T @ PC[:,:PCnum].T
```

![output](https://s2.loli.net/2022/07/08/ykvOqUmGtPeocxb.png)

### 3. ICA 独立成分分析

PCA 虽然可以提取出主要成分，但是该方法却并不能还原出原始的独立信号。这个时候就需要使用ICA了。 在 Matlab 中均可以使用 FastICA 工具。

#### 3.2 ICA 在 Matlab 和 Python 使用的调用

Matlab 中需要将 FastICA 的库文件夹放在工程目录下，Python 中和 PCA 一样需要在 sklearn.decompostion 库中调用 FastICA 模型对象

> Matlab 中
>
> * icasig: ICA 信号
>
> * A: Eigen Vector
>
> Python 中
>
> * icasig = transformer.fit_transform(X.T)
>
> * A = transformer.mixing_
>
> * transformer =FastICA(n_components=3)
>
> 

```python
# Matlab
[icasig, A, W] = fastica(X,'numOfIC',ICNo,'displayMode','off','firstEig',1,'lastEig',PCNo); % fast ICA

% [icasig, A, W] = fastica(X,'numOfIC',ICNo,'displayMode','off','interactivePCA','on'); % fast ICA
% fasticag(X)  % used the correct number of PCA can always produce good results
% [icasig, A, W] = fastica (X)

# Python
## Independent Components Analysis using FastICA
transformer =FastICA(n_components=3)
icasig = transformer.fit_transform(X.T) # input shape = n_features * n_components

icasig = icasig.T
A = transformer.mixing_

```



如下图所示，可以看到 ICA 将原始信号还原了处出来

![output2](C:\Users\Hongtao_Z\Downloads\output2.png)

#### 3.2 数据重构

同样地，用 ICA 提取出来的独立成分，在丢掉明显像杂讯的成分，也可以还原出原始信号。

```python
# Matlab
A2(:,rejectICA)=[];
icasig2(rejectICA,:)=[];

newX=(A2*icasig2);

# Python
newX = A[:,:2] @ icasig[:2,:]
```

![output3](https://s2.loli.net/2022/07/08/HkJ1ba4uyx95Ezn.png)
