#coding=utf-8
import os,sys
import jieba
import jieba.analyse
import operator
from collections import Counter
import matplotlib.pyplot as plt

input_path = 'output.txt'
output_path = 'test_result.txt'
stopwords_path = 'STOPWORD.txt'
test_result_path = r'test_result_path.txt'

# 设置停用词
print('start read stopwords data.')
stopwords = []
with open(stopwords_path, 'r', encoding='utf-8') as f:
    for line in f:
        if len(line)>0:
            stopwords.append(line.strip())

def tokenizer(s):
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords:
            words.append(word)
    return words
# 删除已存在的输出文件
if os.path.exists(output_path):
    os.remove(output_path)
#读取文件数据，分词，并输出到文件
with open(output_path,'w',encoding='utf-8') as o:
    print('input_path:', input_path)
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            s=tokenizer(line.strip())
            o.write(" ".join(s)+"\n")

# 使用TF-IDF方法提取关键词
with open(output_path, 'r', encoding='utf-8') as fn:
    content = fn.read()
    num_keywords = 10  # 默认获取前10个关键词

    # 检查是否传入了命令行参数
    if len(sys.argv) > 1:
        num_keywords = int(sys.argv[1])  # 获取命令行参数中指定的关键词数量

    keywords = jieba.analyse.extract_tags(content, topK=num_keywords)

# 打印权重最大的关键词
print(f"Top {num_keywords} keywords:")
for keyword in keywords:
    print(keyword)



fn = open(output_path,'r', encoding='utf-8')
data = jieba.cut(fn.read())
data = dict(Counter(data))
sorted_data = sorted(data.items(),key = operator.itemgetter(1),reverse = True)
f = open(test_result_path,'w+',encoding="utf-8")
for k,v in sorted_data:
    f.write("%s,%d\n" % (k,v))
f.close()

from wordcloud import WordCloud
# 生成词云图像
font_path = 'Genshin_default_fonts.ttf'  # 字体文件路径
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate(content)

# 显示词云图像
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
