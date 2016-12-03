# encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import jieba
import jieba.posseg
import jieba.analyse

print('='*40)
print('1. 分词')
print('-'*40)
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式
seg_list = jieba.cut("他来到了网易杭研大厦")
print(", ".join(seg_list))
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

print('='*40)
print('2. 添加自定义词典/调整词典')
print('-'*40)
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
#如果/放到/post/中将/出错/。
print(jieba.suggest_freq(('中', '将'), True))
#494
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
#如果/放到/post/中/将/出错/。
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
#「/台/中/」/正确/应该/不会/被/切开
print(jieba.suggest_freq('台中', True))
#69
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
#「/台中/」/正确/应该/不会/被/切开

print('='*40)
print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)
# s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
s = '''非常感谢大家，各位的每一条回复我都看了，我会反思自己的问题，顺便解释几句，通篇都说财务问题，是因为其他的我觉得都不是问题，篇幅有限，文章太长了很难读下去。好多人的分析很有道理，谢谢大家！
说说我的家庭问题：
     我和老公认识的时候他没有房子，认识后确定结婚东奔西跑拉着老公四处看房子，他父母担心我老公贷款压力大，就全款买了现在的婚房（估计是老公父母出了全款或者大部分，因为当时他们三人开会，没有叫我参加，所以老公是否也有钱出，我不清楚），当时老公爸爸纠结是写他名字还是写老公名字，后来考虑到遗产税会很高，写了老公名字。然后装修，婆婆全程参与做主，后来钱花超了，婆婆让我出，我说老公工资卡没给过我，彩礼钱也一分没给，之前提醒过他们装修差不多就得了，他们不听。后来我还是出了几万块，把婆婆已经交了订金的最后那部分家具拉回来了。
     他们家条件还不错，比小康要好一些，父母退休金加一起一万五左右（我估计的，从没问过），因为是异地，结婚时在北京办婚礼我部分亲戚朋友的随礼钱他们直接都收了（不算多，一万多吧），当时结婚时一分钱红包都没给，我妈和我说他们买房子装修也花了不少钱，也不容易，这些全凭心意，不给就算了。结婚旅游也是我出的大部分钱，结完婚第二天他爸在，我和他说要出去旅游了钱不够，他爸给拿了两千块钱。
     结婚到现在五年了，我老公的工资卡从没有交过我，他工资不高，估计不到一万，我一直比他略高些，之前给过我一个月，后来极度不乐意，就要走了，婆婆说他做业务，放我这花着不方便。平时水电、煤气、物业，出去吃饭、看电影、旅游大部分我出，或者说我出70%，有时候心理不愿意我就不买单，他会买一下。前两年和公公婆婆出来吃饭，都是我买单，不让他们买，后来觉得他们太抠门，这两年不请了。
     我父母都有工资，属于工薪阶层，我爸还在工作（事业单位），虽然不是高薪，但是吃穿和二三十万的积蓄还是有的，我想请大家帮我分析一下，现在的状况是我老公工资他一分不剩，信用卡还老欠债状态，我的衣服几乎都不用他买（偶尔一年买两三件便宜的，不敢让他花钱，怕他欠债更多），我现在觉得所有的都要靠自己承担（认识老公前我贷款买了个小房子，现在租出去了，房贷自己还），我理想的婚姻是找一个可以依靠的老公，哪怕他一个月赚5千块钱，可以给我3千，我们存起来，共同规划一下未来，可是现在这种状态，我觉得心凉了，该离婚吗？还是继续忍耐，过这样的日子…… '''
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))
print('-'*40)
print(' TextRank')
print('-'*40)
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

print('='*40)
print('4. 词性标注')
print('-'*40)
words = jieba.posseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))

print('='*40)
print('6. Tokenize: 返回词语在原文的起止位置')
print('-'*40)
print(' 默认模式')
print('-'*40)
result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
print('-'*40)
print(' 搜索模式')
print('-'*40)
result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))