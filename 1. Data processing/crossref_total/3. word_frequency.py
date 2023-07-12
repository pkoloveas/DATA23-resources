# import libraries
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')

top_N = 1000

df = pd.read_csv(r'/Users/GeoFot/data/crossref_total/crossref_total500.csv',      
                 usecols=['abstract'])   # title                           

stopwords = nltk.corpus.stopwords.words('english')
# RegEx for stopwords
RE_stopwords = r'\b(?:{})\b'.format('|'.join(stopwords))
# replace '|'-->' ' and drop all stopwords
words = (df.abstract     # title                                         
           .str.lower()
           .replace([r'\|', RE_stopwords], [' ', ''], regex=True)
           .str.cat(sep=' ')
           .split()
)
# generate df out of Counter
rslt = pd.DataFrame(Counter(words).most_common(top_N),
                    columns=['Word', 'Frequency']).set_index('Word')
print(rslt)

rslt.to_excel (r'C:\Users\GeoFot\data\crossref_total\crossref_total_top500.xlsx', index = True, header=True)