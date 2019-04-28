# ---------------------------------------------
# ------------- hierarchy ---------------------
# ---------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.metrics.pairwise import cosine_similarity

documents = open('../../resources/4.out', 'r', encoding='UTF-8').readlines()
max_docs = int(len(documents) / 1000)  # define the limit to parse
documents = documents[:max_docs * 2:2]  # remove spaces

# vectorize the text i.e. convert the strings to numeric features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)[:]  # too many docs - thus limit the output to see anything

dist = 1 - cosine_similarity(X)
linkage_matrix = ward(dist)  # define the linkage_matrix using ward clustering pre-computed distances
print(linkage_matrix)

fig, ax = plt.subplots(figsize=(15, 20))  # set size
ax = dendrogram(linkage_matrix, orientation="right", labels=documents)

plt.tick_params(
    axis='x',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom='off',  # ticks along the bottom edge are off
    top='off',  # ticks along the top edge are off
    labelbottom='off')

plt.tight_layout()  # show plot with tight layout

# uncomment below to save figure
# plt.savefig('ward_clusters.png', dpi=200)  # save figure as ward_clusters
plt.show()
