from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline

documents = open('../../resources/4.out', 'r', encoding='UTF-8').readlines()
max_docs = int(len(documents) / 20)  # define the limit to parse
documents = documents[:max_docs * 2:2]  # remove spaces

# vectorize the text i.e. convert the strings to numeric features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# -------------KMeans (1)-------------
# cluster docs
true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
kmeans = model.fit(X)
clusters = kmeans.labels_.tolist()

# print top terms per cluster clusters
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
print("tf-idf matrix for features (doesn't relate to doc):")
print(model.cluster_centers_)

print("sort the features and get the indexes for each cluster:")
print(model.cluster_centers_.argsort()[:, ::-1])

terms = vectorizer.get_feature_names()
print("Top terms per cluster:")
for i in range(true_k):
    print("Cluster %d:" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print()

# -------------Another variant of KMeans(1*)--------------
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
])
X = pipeline.fit_transform(documents).todense()

pca = PCA(n_components=2).fit(X)
data2D = pca.transform(X)

dots_size = 2

scatter = plt.scatter(data2D[:, 0], data2D[:, 1], s=dots_size, c=clusters)
labels = np.unique(clusters)
handles = [plt.Line2D([], [], marker="o", ls="", color=scatter.cmap(scatter.norm(yi))) for yi in labels]
plt.legend(handles, labels)
# calculate and plot the cluster enters on this data
centers2D = pca.transform(kmeans.cluster_centers_)
plt.scatter(centers2D[:, 0], centers2D[:, 1], marker='x', s=200, linewidths=3, c='r')
plt.show()

# ------------- predicting with k-means --------------
lines_for_predicting = ['сегодня мы быть гореть сдавать землятресение санкт-петербург пожар конец',
                        'доллар рубль валюта обвал рынок конец финансы',
                        'землетрясение магнитуда происходить пятница ноябрь американский штат аляска это сообщать Fox News эпицентр землетрясение']

print(kmeans.predict(vectorizer.transform(lines_for_predicting)))

