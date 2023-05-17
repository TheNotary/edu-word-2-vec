import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50") # 66MB

v1 = embeds['good']
v2 = embeds['morning']
gm = v1 + v2
sims = embeds.similar_by_vector(gm)

print(sims)

