import gensim.downloader as api
from gensim.models.word2vec import Word2Vec

embeds = api.load("glove-wiki-gigaword-50") # 66MB

v1 = embeds['king']
v2 = embeds['man']
v3 = embeds['woman']
v4 = embeds['queen']

gm = v1 + v4
sims = embeds.similar_by_vector(gm)

print(sims)
