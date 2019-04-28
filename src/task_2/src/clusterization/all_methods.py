from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

f = open('../../resources/4.out', 'r', encoding='UTF-8').readlines()
max_docs = int(len(f) / 100)  # define the limit to parse
f = f[:max_docs * 2:2]  # remove spaces

bow_vectorizer = CountVectorizer()
corpus = f
X = bow_vectorizer.fit_transform(corpus)
kmeans = KMeans(n_clusters=2).fit(X)
bow = [kmeans.predict(bow_vectorizer.transform([f[i]])) for i in range(0, len(f))]

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus)
kmeans = KMeans(n_clusters=2).fit(tfidf)
tfidf_pred = [kmeans.predict(tfidf_vectorizer.transform([f[i]])) for i in range(0, len(f))]

tfidf_often = TfidfVectorizer(max_features=10000)  # top %
tfidf_o = tfidf_often.fit_transform(corpus)
kmeans = KMeans(n_clusters=2).fit(tfidf_o)
tfidf_o_pred = [kmeans.predict(tfidf_often.transform([f[i]])) for i in range(0, len(f))]

file = open('./results/bow.txt', 'w')
for val in bow:
    file.write(str(val[0]) + '\n')
file.close()

file = open('./results/tfidf.txt', 'w')
for val in tfidf_pred:
    file.write(str(val[0]) + '\n')
file.close()

file = open('./results/tfidf_often.txt', 'w')
for val in tfidf_o_pred:
    file.write(str(val[0]) + '\n')
file.close()

# #########################################
# ########## take metrics #################
# #########################################
from sklearn.metrics import silhouette_score

file = open('./results/scores.txt', 'w')

test_bow = bow_vectorizer.transform(f[:len(f)])
score = silhouette_score(test_bow, np.array(bow).ravel(), metric='euclidean')
file.write('bow\t\t\t' + str(score) + '\n')

tfidf_test = tfidf_vectorizer.transform(f[:len(f)])
score = silhouette_score(tfidf_test, np.array(tfidf_pred).ravel(), metric='euclidean')
file.write('tfidf\t\t' + str(score) + '\n')

tfidf_o_test = tfidf_often.transform(f[:len(f)])
score = silhouette_score(tfidf_o_test, np.array(tfidf_o_pred).ravel(), metric='euclidean')
file.write('tfidf_often\t' + str(score) + '\n')

file.close()

# #########################################################################
bow_vectorizer = CountVectorizer()
corpus = f
X = bow_vectorizer.fit_transform(corpus)
file = open('./results/clusters_measurements.txt', 'w')
for j in range(3, 10):
    kmeans = KMeans(n_clusters=j, n_jobs=10).fit(X)
    bow = [kmeans.predict(bow_vectorizer.transform([f[i]])) for i in range(0, len(f))]
    test_bow = bow_vectorizer.transform(f[:len(f)])
    score = silhouette_score(test_bow, np.array(bow).ravel(), metric='euclidean')
    file.write(str(j) + '\t' + str(score) + '\n')
file.close()
