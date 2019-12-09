- **更新日期：2019年12月9日，知乎排个版是真累**

``` python
from Poppy import Charge
# reader.location.setCloseToWall(True)
Charge.cdtime(0)
print('Heroic Head Comes!!')
Charge.E
```

# 这是一篇指导一名啥也不会的临床医学硕士撰写一篇应用机器学习决策树模型的毕业论文的故事

> **本文所述所有内容均为俺们个个儿修仙做梦胡白话的瞎写文字，也是刚入门做做笔记所用，若因本文造成您日后被拒稿/无法毕业/不会科研/被老板骂/误入歧途等，本人概不负责！！**

## 序

- **适合阅读本文的人群**：需要快速撰写毕业论文的临床医学本科生/硕士研究生
- **不适合阅读本人的人群**：打开MmHelper链接后一看就懂的人，手里无数核心/SCI论文的人
- **本文提供的知识能够**：
    - 帮助你快速撰写医学论文的初稿，领你入门
    - 让你的导师茫然不知所措，对你刮目相看
    - 在你的同学朋友里面傲视群雄，指点江山
- **本文提供的知识不能够**：
    - 撰写完整医学论文
    - 顺利通过答辩
    - 保证论文外审评价>>C

## 引言

- **撰写医学论文要“快”**：为什么你感觉自己不会写论文，因为你不知道自己要做什么；那要是给了题目或者自己憋出个题目却还是写不出东西呢，那是因为你没有去实践操作一下；那要是实践操作数据也有了却还是憋了半天也写不出来呢，那就是因为你不够“快”了！为什么不快，让我帮你分析一下原因：（1）不知道该干啥，真写论文的时候才想起需要学学统计学的方法，知道方法了还得去学学EXCEL/SPSS啥的用法，等初步弄明白了某一步的做法又忘了前一步的做法，结果出来了也不知道该看哪行的数据；（2）不知道数据能说明啥，卡方值大了小了，两组间是不是一回事；（3）不知道结果有没有意义，这点尤为重要，因为发现不了关系，那这个论文岂不是废掉了，所以也没有写下去的动力了，大好时光就这样白白浪费了。写论文需要的“快”，就是要迅速得到可能得到的结果，看到好结果动力就有了，心情也好了，写起来也就来劲了。因此，在这里推荐使用Jupyter Notebook/Lab，它的特点就是导入数据后直接看到设定好的步骤和结果，也就几秒的功夫就得到你想要的，这时要忽略所有那些怎么写论文好/如何写论文的经验和知识，“失之毫厘，谬以千里”在统计学上出现的概率还没有那么高吧。（4）现在毕业论文最容易做的就是搜集临床资料做回顾性分析，而这个正好符合机器学习的运作流程，收集好数据标准归纳好就可以用了。
***
- **撰写医学论文要“厚”**：厚，不是说拷贝粘贴得来的厚。真想厚的话，用我的[MrHelper](https://zhuanlan.zhihu.com/p/47755088)简单多选些相关文章，然后自动归个类就能做到国外“形”似的超长篇大综述，但那个糊弄人还行，实际用起来好像还差点。真想写厚的话当然全靠自己写，一直推荐闭眼睛想到啥就写上啥，跟YY一样的感觉，不过那样写完文字量是够了，但是写不出啥东西，所以大纲还是要先列一下的，这样每条都写完后尽管就是一篇长篇大白话，但是成就感满满的。回到现实当中，其实写厚就是因为两条：（1）写多了往少了删好删，不就是把白话文改成文言文，把俗语改成公文什么的，意思在那里怎么改都方便；（2）毕业论文么，就是练习一下做做学问，写的越细越好，写的越厚让外审的专家觉得你很认真，至少没对付。所以这里推荐的就是你要写的厚，还想不用太动脑子，或者时间太紧再不写就毕业不了了，那就用scikit-learn机器学习的方法，因为步骤很多，每一步都会有计算有解释，而每一个解释都是你讨论部分的一个点，切记这也是为什么真正搞计算机的不可能写出你能写出的文章，因为他们不了解医学相关的东西，而你能。
***
- **撰写医学论文要“玄”**：玄，让人看着听着都玄妙。这种玄妙的感觉是建立在听的人不是很懂的基础之上的，这就会让人产生一种你弄的东西很深奥的感觉，所以这里再次推荐在方法和结果部分都按照机器学习的分析过程来写。这有两点原因：（1）机器学习，我相信真正的临床医生去研究这个东西的人很少，也就是说你写的东西肯定在投稿外审或者毕业答辩时遇到的专家不会很多，你可以大谈人工智能、谈AI、谈各种乱七八糟的统计学方法，那种高大上的感觉肯定能出来；（2）机器学习的基本理论知识都是建立在经典的统计学方法之上的，在sklearn的FAQ里面明确说了“We only consider well-established algorithms for inclusion. A rule of thumb is at least 3 years since publication, 200+ citations and wide use and usefulness.”，所以对于其内涉及的统计方法你也可以在答辩的时候大胆去谈，因为听的人不懂。可是，对于某些算法你也没看懂怎么办呢，那么不要担心，因为你你你都大学生了，如果看了半天都没懂，你认为参加答辩的搞临床的老师看了几下就能懂么，这就是“玄”的真谛啊。记住，如果碰到这个时候，就要避重就轻，大谈你懂的算法，例如决策树，末了再加上点随机森林，保证答辩效果爆棚，人生得意啊。那外一有真正的专家来了呢，那就实话实说哪个算法那公式怎么怎么复杂，怎么怎么较难理解，不过效果还是可以经得过考验的，等等... 我相信80%的专家会帮你解释的，因为这也是专家显露身手的时候了，嘿嘿嘿...
***
- **撰写医学论文要“用”**：论文是要用到实际应用中的，所以不管自己写还是别人看，最终都会问到一个问题，你写的这个东西是干啥用。这也正是机器学习最擅长的东西，简单说就是分类、回归等等。分类的概念其实很广的，最常用的就是给个花瓣的长度宽度啥的预测是哪类花，再就是用泰坦尼克游客的相关数据预测是否生存什么的。医学论文里面用的最多的就是实验组、对照组，然后列个四个表或者列联表的计算下卡方，然后说明两组间有差别再讨论讨论的，结论也就是这种方法比那种要好些，文章也就结束了。但如果你又加上了后面一大堆的统计数据，然后在讨论结论部分又说了你有90%的把握新的资料能预测结果，这样带给人的震撼绝对够的上是具有临床实际意义的论文了吧。这里的“用”还有另一个含义，有的时候可能感觉盲目的堆砌统计方法是否会降低文章的水平，我觉得不去算算就不会知道数据里面的含义，只有用过了才能体会到数据的美妙，即使最终里面的结果数据图片什么的都没用，也会让你在心里埋下这种方法的种子，对以后的实验设计绝对有好处，而且你可以自豪的给自己一个响亮时尚的头衔“数据分析师”，然后自信满满的搜集各种数据去计算明天双色球的号码或者股票的涨跌了，切，不就是个特征工程么...
***
- **撰写医学论文要“看”**：以前一直认为现在教你如何写论文的文章没啥用处，因为教的都是很抽象的东西，譬如说要多看大牛的文章、多看经典的文章，我在这个领域刚入门，我哪里知道谁是大牛谁是经典，所以尝试写了写[MrHelper](https://zhuanlan.zhihu.com/p/47755088)的东西，不过到了一定程度写不下去了，因为不知道该往哪个方向去弄了，这个时候才发现那些文章细细品味还是很有内涵的。所以尽管我下面要写的东西也是想让需要的人一下子就能利用上，但是到了一定程度后你会觉得不够用了，这时候就要多看看相关的文章吧，该收藏就收藏该关注就关注啥的，尤其对于文章后面的特征工程、调参、效果评价等等，我也是略知一二、无法详尽啊，好在网络上文章很多，多看看对答辩是非常有用的，知识不嫌多么... 在CNKI上面你可以搜一下，文献分类选择“医药卫生科技”，篇名选择“机器学习”，然后选择“中文文献”。你可以看看，截至2019年11月26日，一共就三百多篇，博士论文18篇，硕士100篇，期刊170篇，绝大多数都是2017年开始出现的，而且绝大部分都是非医学专业写的文章，看看这些硕士论文，看的多了你就很自信了，因为讨论的都是模型的构架和比较，而对医学内容本质的分析真的很浅很皮毛。看的多了你可以把方法拿来用在你的文章里面，不过讨论的一定要贴近医学的本质了。

## 材料与方法

### 1. 软件准备

- **下载最新的[WinPython](http://winpython.github.io)**，里面版本很多，一般下载没有Zero/Ps2/cod标记的那个64位版本，如果没把握也可以用我这个SourceForge的[Winpython64-3.7.4.1.exe](https://sourceforge.net/projects/winpython/files/WinPython_3.7/3.7.4.1/Winpython64-3.7.4.1.exe/download)链接直接下载。正常安装即可，绿色软件开箱即用。打开后是这个样：<img> 看不到图片么？不要紧，因为我还没传呢。
- **下载最新的[mmhelper](https://github.com/dearfad/mmhelper/releases/download/v0.1.0-alpha/mmhelper-v0.1.0-alpha.zip)**，解压缩得到文件mmhelper.ipynb。![WinPython](https://github.com/dearfad/mmhelper/blob/master/img/winpython.png) 什么，里面没多少代码啊，我还没弄完呢。

### 2. 使用

- 点击安装目录里面的**Jupyter Notebook.exe**，会出现一个命令窗口并自动打开一个浏览器的网页，就在网页里面进行操作。如图<img>
- 点击**Upload**，上传**mmhelper.ipynb**和**data.xlsx**，上传后文件位于winpython目录下的notebooks目录内，可视情况改动。
- （可选）或者直接指定你的工作目录，编辑WinPython\scripts\settings\winpython.ini在最后添加路径。如图<img>
- 点击**mmhelper.ipynb**，打开后点击右上角使之变为“可信的”。如图<img>
- 点击Cell-Run All，当右侧Python 3旁边的空心圆不再闪烁即运行完毕。或者按顺序单独执行某一个单元格**shift+enter**或者**ctrl+enter**。
- 快速去掉注释符号“#”，可使用快捷键CTRL+"/"

### 3. 数据准备

- **如果有手里有数据**，可以**录入Excel表格**，第一列必须设定为分组情况，分类资料用0、1等表示阴性和阳性结果，此列为以后预测分类的指标。其他列为与第一列相关的其他因素或指标。计数资料用具体数字即可，为了减少处理缺失值的麻烦，所有数据尽量完整。保存为data.xlsx文件。如图<img>
- **如果你手里没有数据**，可以在里面找到这样的代码，全选后按CTRL+"/"去掉注释“#”符号，执行一下这个格子，CTRL+ENTER，就会在你的目录下面生成一个demo.xlsx的文件。后面都是用这个来进行演示和说明。
```python
import numpy as np
import pandas as pd
np.random.seed(1)
data = pd.DataFrame({
    'label': np.random.randint(0, 2, 500),
    'age': np.random.randint(18, 70, 500),
    'sex': np.random.randint(0, 2, 500),
    'height': np.random.randint(140, 200, 500),
    'weight': np.random.randint(40, 100, 500)
})
data.to_excel('demo.xlsx', index=False)
```
### 4. 定义问题

- 为了尽量减少对内容的更改，数据表的第一列定义为分组或者分类的目标，例如我想用年龄和绝经与否来预测是否有病，那么第一列tumor就应该设为有病或者无病两个分组，那么我们的目标就是通过第2列age和第3列menopause来预测给定的新病例是否有病。当然每一列的名字可以自行按需更改。举个例子，我有十个患者资料，（恶性，45岁，绝经）（良性，35岁，未绝经）（恶性，50岁，绝经）... 通过构建模型以后，如果又给你了十个患者资料（30岁，未绝经）（46岁，未绝经）... 模型对这十个新患者进行预测给出了（恶性）（良性）等等的预测结果，跟实际的结果进行对比，达到了75%的预测准确率，这就是机器学习预测的目的，而整个后续处理的目标就是尽量达到准确率的最高值。在这里需要明确的是，进行后续处理的前提是我们要对数据有一定的认识，例如判定良恶性确实跟年龄和是否绝经有一定的关系，尽管这种关系我们可能说不清或者冥冥之中似有联系，都可以进行下一步的处理；或者可以基于以往的研究结果，例如癌症跟年龄/月经/初潮/妊娠等等都有关系，这样数据表可能非常大也没有关系，都是可以的。但是对于那种给你1000组双色球的数据，让你预测下一组球的号码来说，就无能为力了，因为每一个位置的号码和最终中奖之间都是随机的，这样的学习结果可能在模型里面可以达到非常高的准确率，但是对于新数据做预测来说就不可能准确了。
***
- 用**demo.xlsx**的数据来做一下说明。假设我收集了500个人的资料，分别有年龄、性别、身高、体重，然后我根据她们的这四个基本情况做了一下标记，标记什么呢，当然是“美”和“丑”了，或者是“有病”和“没病”，或者她们本身身上就写着“美”和“丑”，都可以了哈，反正你自己要预测的这一列最重要，通常就是我们收集到的恶性良性，有变化没变化这类的结果。对于咱们这里刚刚入门的肯定首选二分类的预测了，既是“有”或者“无”这样的分类。label是咱们需要预测的结果，age就是实际年龄18-69，不包括70了，其余类似，sex是0/1，height 140-199厘米，weight 40-99公斤，共500组数据。这样我们的目标，就是论文的目的很明确了，我要通过机器学习现有的数据建立模型，然后如果给我一个新的人，25岁，女，身高165厘米，体重45公斤，模型就能够按照我的审美来做出美或者丑的评价。

## 结果

### 1. 随机数据

- 打开mmhelper.ipynb，找到下面这些代码。看到里面的demo.xlsx了吧，改成你的数据表文件名或者就用我给你的试一试。点中那个单元格，然后狂按CTRL+ENTER，结果的数字就代表你的模型预测的准确率。
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

datafile = 'demo.xlsx'
data = pd.read_excel(datafile)
X, y = data.values[:, 1:], data.values[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
result = accuracy_score(y_test, y_predict)
print(result)
```
- 感觉如何，我最高按到了0.6，你呢？ 都随机的跟抛硬币是一样的，所以正常机器预测的结果就是0.5上下哈。

### 2. 指定数据

- 这次我将上面的代码改一下，可不用随机的美丑标准了，身高155以上吧，也不能太高180吧，体重45公斤以上70公斤一下，这样的才算美的，label设置为1。能找到多加的那两行代码吧？

```python
import numpy as np
import pandas as pd
np.random.seed(1)
data = pd.DataFrame({
    'label': np.random.randint(0, 2, 500),
    'age': np.random.randint(18, 70, 500),
    'sex': np.random.randint(0, 2, 500),
    'height': np.random.randint(140, 200, 500),
    'weight': np.random.randint(40, 100, 500)
})

data['label'] = data['height'].apply(lambda x : 1 if x in range(155,180) else 0) & \
                data['weight'].apply(lambda x : 1 if x in range(45,70) else 0)

data.to_excel('demo.xlsx', index=False)
```

- 这次怎么样，最低我到过0.93，说明什么呢？机器是不知道你的标准的，不过如果给我一个新的数据，年龄23性别1身高140体重65，可以在最后面新开个格子，然后加入如下代码，或者你自己设定个值实验下。

```python
test = pd.DataFrame({
    'age':[23],
    'sex':[1],
    'height':[140],
    'weight':[65]
})
print(model.predict(test))
```

## 讨论

### 1. 对于机器学习的理解

- 经过上面的操作不知道你对于机器学习是否有了一个模糊的概念呢，只要你的数据是从真实世界中获取的，经过一些影响因素而发生改变的，那么通常情况下是可以建立一个模型进行研究的，而那种本来都是随机的特征最后反应到你的分类那也是随机的结果。

### 2. 对于数据的信心

- 写临床的毕业论文搞个几千几万例的资料除非积累的很好，否则就毕业前的那点时间很难攒到很大的数量，通常都是查了几百例的资料吧，真正需要多少还得看你追求的目标了，一般建议至少400例比较好吧。如果关系非常理想，100-200例也可以得到很好的结果了。

### 3. 这样就可以写毕业论文了么？

- **是的**。可以返回去看看上面的代码，读取数据，分类训练和测试数据，建立模型，训练模型，模型预测。就单单这几个步骤，然后你讨论讨论，一篇本科毕业论文也就足够了，看看CNKI医学类机器学习的期刊文章，很多都是材料方法那里写了很多，结果把主要结果说完，然后讨论讨论就结束了，所以就用上面这些也足够你去发表一篇文章了。但是就像前面写道的，既然要弄个硕士级别的高大上的机器学习毕业论文，你就得在这上面添砖加瓦，让整本论文厚实起来。不要怕没有东西可写，你做的每个步骤都是可以找到书写的理由的，完全在你的掌控之中。

### 4. 如何来确定分类呢？

- 就像刚才定义问题中说的，重点中的重点就是要定义好你的分类目标。有的时候可能你看着你的数据想，我这数据杂乱无章我也不知道该怎么分类啊，这个时候你就要注意单看你的每一条数据里面你都记录了什么。一种是在其中的字段找一个作为分类的标志，譬如说性别，只有男和女，或者其他的如年龄，可以人为的以35岁作为分界点分成两类等等。另一种就是新建一个字段，然后你按照你的想象标准列为0或者1，就像你看到一封电子邮件分为有用的邮件和垃圾邮件一样，反正就是找出个可以预测的有意义的地方，这个非常灵活。也许我没说清楚，就当草稿看吧，以后细改改。

***

## 卡方检验

- 正式开始之前咱们先来热个身吧，做个卡方检验看看效果。即使以后不做机器学习的事，最起码能看到这里的人都是想学到一些东西的，不会SPSS可以用这个算一算也不白看这么长时间了。

```python
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_excel('demo.xlsx')
cross_table = pd.crosstab(data['label'], data['sex'], margins=True)
print(cross_table)

# cross_table = np.array([
#     [43, 96],
#     [28, 84]
#     ])

result = chi2_contingency(cross_table, correction=False)  # Pearson Test
# result = chi2_contingency(cross_table, correction=True) # 连续性校正
# result = fisher_exact(cross_table) # Fisher's Test

print(pd.DataFrame(result[3]))
print(f'X2= {round(result[0],3)}, p= {round(result[1],3)}')
```

## t 检验

- 再送一个独立样本t检验，检验前别忘了做Levene's test看方差是否齐啊，有了卡方和t检验，即使本文没看懂也可以用来做做常规数据分析了写写文章了。

```python
from scipy import stats
import pandas as pd

data = pd.read_excel('demo.xlsx')

group = 'label'
feature = 'height'
print(round(data.groupby(group).mean(),2))

group_0, group_1 = data[data[group]==0], data[data[group]==1]
levene_p = round(stats.levene(group_0[feature], group_1[feature])[1], 3)
print("Levene's Test p =", levene_p)

if levene_p > 0.05:
    test = 'Student'
    statistic, pvalue = stats.ttest_ind(group_0[feature], group_1[feature], equal_var=True) # if p>0.05 Student's t-test
else:
    test = 'Welch'
    statistic, pvalue = stats.ttest_ind(group_0[feature], group_1[feature], equal_var=False) # if p<0.05 Welch's t-test 

print(f'test = {test}, stat = {round(statistic,4)}, p = {round(pvalue,3)}')
```

***



**以下内容请勿观看**

```
- 查看预测分组与相关变量的关系：例如需要预测tumor出现的机率，首先看一下tumor和其他变量的相互关系，正相关或者负相关都是可以的，当然是其中某一个越高越好，其他作为辅助这样得到的预测准确率就能高很多。然后，就是显示你专业水平的时候了！！！医学理论专业分析因果，这也是为什么计算机或者统计专业搞数学的无法独立完成我们的机器学习医学论文的原因，因为她们不明白各个因素之间的关系，所以也无法进行降维、特征选择等等了。看相关的图表很简单，这里主要是确认一下我们的数据有没有很明显的问题，像gestation和abortion是0.9就很合理啊。
- 查看交叉验证和准确率结果：如果上面两个没有太大的问题，接着就大概看一下如果进行机器学习预测风险的话，我们大概能得到一个什么样的结果，这是通过我们最原始数据得到的，没有进行特征工程、调参一类的事情，如果这个时候就能得到一个完美的结果，感觉80%以上吧，10个里面我能才对8个就应该很好，除非是那种特别完美的数据集。这样临床应用就足够了，如果需要达到95%以上才能应用于临床我感觉用机器学习就不太合适了。
- 查看学习曲线：无论原始的预测结果如何，都要首先看一下各个模型的学习曲线。通常的学习书籍都把这个放到最后模型选择的部分，但是对于需要快速完成论文的研究生来说就不合适了，边看边学到最后一看有问题了那可就慌的一P了。简单说，上面红线就是训练集得分，下面是用验证数据得分，就想象为准确率吧。横轴是病例数量，纵轴是得分。一般随着病例数增加红绿线逐渐收拢至一起，下图再增加数量也就65%左右了，再多查病例弄数据也就那样了，所以就没必要再去收集，专心研究别的模型就可以了，这对我们选择模型和确认学习数量是否合理非常必要。
- 抉择：如果上面的预测结果相对较高，或者跟你文章结论预期准确率差不多，那么就可以继续按正式稿写下去了；否则要么初始预测不高结论不是很好，要么临床要求准确率必须达到一个程度才行，那就别走机器学习的路子了，赶快换别的写作方向吧；如果你用这个比较熟练了，也可以按照下面的方法继续弄一弄，看看准确率能否再升高一些达到预期水平。
```