import pandas as pd
from tqdm import tqdm
import constants as c
import nltk
nltk.download('punkt')
nltk.download("stopwords")
tqdm.pandas()


sw = nltk.corpus.stopwords.words('swedish')

def filter_stop_words(tokens):
    lst = []
    for word in tokens:
        if word not in sw:
            lst.append(word)
    return lst

def propagate_dict(freq_dict, tokens):
    for word in tokens:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

if __name__ == '__main__':
    """ Read conv data """
    print("Read input dataframe...", end="")
    df = pd.read_csv(c.data_path)
    print("Done!")
    df.info()
    
    """ Filter out NULL data """
    df = df[df['msg'].notnull()]
     
    """ Tokenize data """
    df['msg'] = df.progress_apply(lambda row: str.lower(row['msg']), axis=1)
    df['tokenized_sents'] = df.progress_apply(lambda row: nltk.word_tokenize(row['msg']), axis=1)
    
    """ Filter out swedish stop-words """
    df['cleaned_sents'] = df.progress_apply(lambda row: filter_stop_words(row['tokenized_sents']), axis=1)

    """ Create Word frequency distribution """
    freq_dist = {}
    df.progress_apply(lambda row: propagate_dict(freq_dist, row['cleaned_sents']), axis=1)
    
    """ Sort Dict by value """
    sorted_dict = dict(sorted(freq_dist.items(), key=lambda item: item[1], reverse=True))

    """ Convert Dict to DF """
    df = pd.DataFrame(sorted_dict.items(), columns=["word", "count"])

    """ Write Dict to csv """
    df.to_csv(c.dist_path, index=False)
    




