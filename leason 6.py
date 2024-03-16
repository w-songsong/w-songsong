import csv
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

file = open("/Users/yequ/TVComments.csv", "r")
reader = csv.reader(file)

data = []
for info in reader:
    data.append(info)

word = []
for row in data:
    text = row[0]
    ret = jieba.lcut(text)
    ret = ' '.join(ret)
    word.append(ret)

vect = CountVectorizer()
X = vect.fit_transform(word)
X = X.toarray()

y = []
for allInfo in data:
    label = allInfo[1]
    y.append(label)

result = train_test_split(X, y, train_size=0.8, random_state=1)
train_feature = result[0]
test_feature = result[1]
train_label = result[2]
test_label = result[3]

mlp = MLPClassifier()
mlp.fit(train_feature, train_label)

test_pred = mlp.predict(test_feature)
score = accuracy_score(test_pred,test_label)

comment = "自定义评论"

comment = jieba.lcut(comment)
comment =  [' '.join(comment)]
try_feature = vect.transform(comment)
try_feature = try_feature.toarray()
try_pred = mlp.predict(try_feature)

print(try_pred)
