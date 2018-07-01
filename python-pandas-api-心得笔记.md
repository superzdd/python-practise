# 心得
1. 当操作整体矩阵时，优先调用pd来使用api，而不是df
2. 当要对所有列进行处理时，应该对df操作，而不是对df.columns操作

# API
### 导入pandas
```python
import pandas as pd
```

### pandas 读取csv，使用分隔符
```python
# 常规读取形式
df_red = pd.read_csv('winequality-red.csv')

# 使用分隔符的形式
df_red = pd.read_csv('winequality-red.csv',sep=';')
```

### 使用matplotlib
```python
% matplotlib inline

df.hist(figsize=(8,8));
df.plot(kind='hist')
df.plot(kind='bar')
```

### dataFrame保存csv文件
```python
wine_df = red_df.append(white_df)

wine_df.to_csv('winequality_edited.csv',index=False)
```

### 修改列名
```python
red_df.rename(columns={'total_sulfur-dioxide':'total_sulfur_dioxide'},inplace=True)
```

### 输出dataframe的行数和列数
```python
df.shape
# output
(100,20)
```
100 为行数，20 为列数

### 输出所有列的数据类型
```python
df.dtypes
# output
id                          int64
diagnosis                  object
radius_mean               float64
texture_mean              float64
perimeter_mean            float64
area_mean                 float64
smoothness_mean           float64
compactness_mean          float64
```

### 某列中值一共出现过多少次
```python
df['education'].value_counts()
```

### 某列中一共出现过多少个值
```python
df['education'].unique
```

### 横向合并两个矩阵
```python
# 创建标准误差数据框
se_list = [df.iloc[:,:2],df.iloc[:,12:22]]
df_se = pd.concat(se_list,axis=1)

# 查看前几行，确认是否成功
df_se.head()
```
> 注意，iloc中的:是前闭后开区间

### 填充缺失值，并修改自身
```python
# 用均值填充缺失值
s_m_mean = df['smoothness_mean'].mean()
df['smoothness_mean'].fillna(s_m_mean,inplace=True)
# 用 info() 确认修改
df.info()
```
### 查看矩阵中重复的行
> 只有每一列数据都相同时，才被认为是重复行
```python
# 检查数据中的重复
sum(df.duplicated())
```

### 删除矩阵中重复的行,并修改自身
```python
df.drop_duplicates(inplace=True)
```

### 列重命名
```python
# 从列名称中移除 "_mean"
new_labels = []
for col in df.columns:
    if '_mean' in col:
        new_labels.append(col[:-5])  # 不包括最后 6 个字符
    else:
        new_labels.append(col)

# 列的新标签
new_labels

# 为数据框中的列分配新标签
df.columns = new_labels

# 显示数据框的前几行，确认更改
df.head()
```

### 列重命名
> rename

> http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
```python
# 在 2008 数据集中用下划线和小写标签代替空格
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# 确认更改
df_08.head(1)
```

### pandas增加列
> 可以先把数据生成好，增加列时，没有特殊的声明，直接赋值操作也是可以的
```python
# 为红葡萄酒数据框创建颜色数组
color_red = np.repeat('red',len(red_df))

red_df['color'] = color_red
red_df.head()
```

### 列排序
> 将表格按某一/几列的值排序，可以指定升序或降序（可以是bool型列表）
```python
df.sort_values(by=['col1'])
df.sort_values(by=['col1', 'col2'])
df.sort_values(by='col1', ascending=False)
```

### 画类似正态分布图
> 常规做法，用`bar`来绘制
```python
def make_plot(col):
    df.sort_values(by=col,inplace=True)
    un = df[col].unique()
    vc = df[col].value_counts()[un]
    vc.plot(kind='bar',figsize=(10,8));
    return

make_plot('fixed_acidity')
```

> 骚操作，`hist`绘制，可以跳过给每个值计数的过程
```python
# 表格有多少列，下面这个方法就会画多少张图
df.hist(bins=100,figsize=(12,12));

# 画单列
df['col'].hist(bins=100,figsize=(12,12));
```

### 踩坑，柱状图(hist)，绘出的图形，横纵坐标与原始数据不对应
> 比如原始如下

|  | LENGTH | WIDTH |
| - | - | - |
| pig | 1.5 | 0.7 |
| rabbit | 0.5 | 0.2 |
| duck | 1.2 | 0.15 |
| chicken | 0.9 | 0.2 |
| horse | 3 | 1.1 |

> 我们使用matplotlib绘图，单独绘制LENGTH和WIDTH列。
> 在我们的直觉里，绘制出的图，横坐标应该是[pig,rabbit,...],纵坐标是[1.5,0.5...]，（或者横纵坐标相反）
> 但是用hist是不同的，hist横坐标是值域，机[0,3]区间，使用`bins`属性在[0,3]区间中分隔横坐标的具体数量,纵坐标是每个值的出现次数，而不是值本身
#### 重要提示：hist只关心数值的出现次数，横坐标的标记没有意义(这里是[pig,rabbit...]这些内容)

### cut 列切分
> 将某一列中的所有值按照其值所在范围划分区间，或者上固定标记
> 下面这种情况，应该是使用最多的情况
```python
# 按照pH列的值，划分区间，并新建一列以展示区间

# bin_edges 划分区间数组，用数组已经是比较复杂的了，最初级的使用方法bin_edges=3,将按照值域平均分为3组
# 对用于把数据“分割”成组的边缘进行分组
bin_edges = [ 2.72, 3.11, 3.21, 3.32, 4.01] # 用刚才计算的五个值填充这个列表，通过df.describe()得到的[ min, 25%, 50%, 75, max ]5个值

# 四个酸度水平组的标签
bin_names = [ 'p1', 'p2', 'p3', 'p4'] # 对每个酸度水平类别进行命名

# 创建 acidity_levels 列
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)
```

### 用groupby拆分数据
> 使用dataFrame直接操作groupby，而不是对某一列操作
```
df.groupby('color',as_index=False)['quality'].mean()

# 拆分多个的示意
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
```

### 查询行
```python
# selecting malignant records in cancer data
df_m = df[df['diagnosis'] == 'M']
df_m = df.query('diagnosis == "M"')

# selecting records of people making over $50K
df_a = df[df['income'] == ' >50K']
df_a = df.query('income == " >50K"')

# 稍微真实点的例子，首先获取这列的中位数，然后选择所有小于以及大于等于中位数的行

# 获取中位数
al_avg = df_des.loc['50%','alcohol']

# 选择酒精含量小于平均值的样本
# 注意这里有类型转换
low_alcohol = df.query('alcohol < ' + str(al_avg))

# 选择酒精含量大于等于平均值的样本
high_alcohol = df.query('alcohol >= ' + str(al_avg))
```

### matplotlib.pyplot初体验画图
> 想要图画的好，`pyplot`和`seaborn`是不能缺少的
> 这是第一个例子，看起来只要导入了`pyplot`和`seaborn`，都是全局画图都生效的，不需要额外指定调用这两个类，进行画图操作
```python
import matplotlib.pyplot as plt
import seaborn as sns
% matplotlib inline

colors = ['red','white']
color_means = df.groupby('color')['quality'].mean()
color_means.plot(kind = 'bar', title = 'Average by Color', color = color_means, alpha = .7)
plt.xlabels = ('Color', fontsize = 18)
plt.ylabels = ('Quality', fontsize = 18)
```

### 数据处理的办法：将百分比来处理数值进行绘图，可以避免数据之间样本量不足造成的差异
```python
# 获取每个等级和颜色的数量
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']

# 获取每个颜色的总数
color_totals = wine_df.groupby('color').count()['pH']

# 将红葡萄酒等级数量除以红葡萄酒样本总数，获取比例
red_proportions = color_counts['red'] / color_totals['red']

# 将白葡萄酒等级数量除以白葡萄酒样本总数，获取比例
white_proportions = color_counts['white'] / color_totals['white']
```

### 中位数
```python
df['alcohol'].median()
```

### 丢弃多余列，删除列
>用`drop`,注意`axis`为`0`时，删除行，为`1`时，删除列
```python
# 从 2008 数据集中丢弃列
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)
```

### 丢弃两个数据集中有任何空值的行
```python
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)
```

### 批量给某一列的数据赋值
```python
df_08.loc[df_08['air_pollution_score'] == "6/4",'air_pollution_score'] = 1.5
```

### 整列类型转换
> 注意，在进行类型转换前，要保证这一列的数据可以正确转换到目标类型上，否则在转换时可能会出现错误，导致转换失败
```python
# 将air_pollution_score由object类型转换成float类型
# 这列中，6/4这样的值，无法一次性转到float型，需要单独处理
df_08.loc[df_08['air_pollution_score'] == "6/4",'air_pollution_score'] = 1.5

# 进行类型转换，注意这里需要列赋值
df_08['air_pollution_score'] = df_08['air_pollution_score'].astype(float)
```

### 某个单元格中存在多个值，将这个单元格中的值拆分到多行中
> 例如，一个单元格的内容是： `16/25`，其实它要说明其中有`16`和`25`两个值，所以要将`16`和`25`拆开，当做两行处理
```python
# 首先，获取 2008 年的所有混合动力
hb_08 = df_08[df_08['fuel'].str.contains('/')]

# 创建 2008 混合动力数据框的两个副本
df1 = hb_08.copy()  # 每个混合动力车第一种燃料类型的数据
df2 = hb_08.copy()  # 每个混合动力车第二种燃料类型的数据

# 将被 "/" 分割的列
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

# 对每个数据框副本的每个列应用分割功能
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# 将数据框组合，添加到原始数据框中
new_rows = df1.append(df2)

# 丢弃原始混合动力行
df_08.drop(hb_08.index, inplace=True)

# 添加新分割的行
df_08 = df_08.append(new_rows, ignore_index=True)

# 检查含有 "/" 的所有原始混合动力行是否都已删除
df_08[df_08['fuel'].str.contains('/')]
```

# 类型转换
> 直接将类型写在要转换的数值前面
```python
a = 3.2
a = int(a)
print(a)
```

#列分隔字符串
> 当单元格中的值，由好几个数值组成并且指定分隔符时，比如`Action|Drama|Fiction`，将这个值按照分隔符`|`拆分成三行的办法

| Class |
| - |
| piAction\|Adventure\|Science Fiction\|Thriller |

> 需要用到的几个方法
- `drop` 用于删除原来的Class列，注意其中的`axis`变量，必须为`1`才是删除列，否则默认`0`是删除行
- `join` 用于添加新的Class列
- `split` 分隔字符串，注意其中的`expand`变量，这个属性可以将分隔之后的数组转化为n列
- `stack` 列行转换，将列转换成行
- `reset_index` 将行序号转换为一列，当`drop=True`时，代表删除这个序号，改用`0,1,2....n`作为新序号,`level=1`代表多级行序号和第二层

```python
df.drop('Class', axis=1).join(df['Class'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('Class'))
```