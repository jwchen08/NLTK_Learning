# -*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud

# Read the whole text.
# 此处原为处理英文文本，我们修改为传入中文数组
# d = path.dirname(__file__)
# text = open(path.join(d, 'constitution.txt')).read()
frequencies = [(u'知乎',5),(u'小段同学',4),(u'曲小花',3),(u'中文分词',2),(u'样例',1)]
#frequencies = [('知乎'.decode('utf-8','ignore'),5),('小段同学'.decode('utf-8','ignore'),4),('曲小花'.decode('utf-8','ignore'),3),('中文分词'.decode('utf-8','ignore'),2),('样例'.decode('utf-8','ignore'),1)]

# Generate a word cloud image 此处原为 text 方法，我们改用 frequencies
# wordcloud = WordCloud().generate(text)
# Windows
# wordcloud = WordCloud(font_path='G:\Windows\Fonts\msyh').fit_words(frequencies)
# Mac OS
wordcloud = WordCloud(font_path='/System/Library/Fonts/STHeiti Light').fit_words(frequencies)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).fit_words(frequencies)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()