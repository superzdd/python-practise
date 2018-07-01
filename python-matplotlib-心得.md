### 声明matplotlib
```
% matplotlib inline
```

### 每画一张图，用`;`,防止打印尖括号内容
```python
# 不带分号，在plot时，会打印以下内容
df.tail(1).plot(kind='bar')
# output
<matplotlib.axes._subplots.AxesSubplot at 0x7f44a8ad7a58>
```

### 画柱状图
> 下面都是能成功画出柱状图的代码，方便以后看例子
```
df.tail(1).plot(kind='bar');
df.mean().plot(kind='bar');
df[df['week']=='2016-03-13'].plot(kind='bar');
df.tail(12).sum().iloc[1:].plot(kind='bar');
```

### 画关系图，散点图
```
# 绘制温度与电力输出之间的关系图
% matplotlib inline
df.plot(x='Temperature',y='Electrical output',kind='scatter');
```

### 使用pyplot画图的完整示意
```python
import matplotlib.pyplot as plt
% matplotlib inline
```

> pyplot 的 `bar` 功能中有两个必要参数：条柱的 x 坐标和条柱的高度。

```python
plt.bar([1, 2, 3], [224, 620, 425]);
```

> 可以利用 pyplot 的 `xticks` 功能，或通过在 `bar` 功能中指定另一个参数，指定 x 轴刻度标签。以下两个框的结果相同。

```python
# 绘制条柱
plt.bar([1, 2, 3], [224, 620, 425])

# 为 x 轴指定刻度标签及其标签
plt.xticks([1, 2, 3], ['a', 'b', 'c']);
```

```python
# 用 x 轴的刻度标签绘制条柱
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c']);
```

> 用以下方法设置轴标题和标签。

```python
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label')
```

### 画柱状图时，将两组数据的柱状图，x值相同的两根柱画在一起
> 这是一个骚操作，关键在与两组数据的x坐标，通常我们会这么用x来区分两组数据
```
x1: [1, 3, 5, 7]
x2: [2, 4, 6, 8]
```
> 这样画出来的柱状图会是等距的。那如果要挨在一起，骚骚的你估计已经想到了
```
x1: [1, 2, 3, 4]
x2: [1.35, 2.35, 3.35, 4.35]
```
> 这里的.35，看样子就是个经验值，为什么是这个数，也是先辈们调出来的，我们只管用

```python
ind = np.arange(len(red_proportions))  # 组的 x 坐标位置
# 关键代码
width = 0.35       # 条柱的宽度

# 绘制条柱
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# 标题和标签
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # x 坐标刻度位置
labels = ['3', '4', '5', '6', '7', '8', '9']  # x 坐标刻度标签
plt.xticks(locations, labels)

# 图例
plt.legend()
```