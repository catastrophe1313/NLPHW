import time
import os
from pathlib import Path
import spacy
from collections import Counter


def preProcess(type, path):
    if type == 'train':
        f = open('train.txt', 'w')
    else:
        f = open('test.txt', 'w')
    folderList = os.listdir(path)
    for folder in folderList:
        if folder == 'rec.autos' or folder == 'comp.sys.mac.hardware':
            fileList = os.listdir(path + '/' + folder)
            for file in fileList:
                print('writing' + file)
                content = Path(path + '/' + folder + '/' + file).read_text(encoding='utf-8', errors='ignore')
                nlp = spacy.load('en_core_web_sm')
                doc = nlp(content)
                tokenList = []
                for token in doc:
                    if token.is_alpha and not token.is_stop:
                        tokenList.append(token.lemma_)
                freqDict = dict(Counter(tokenList))
                for k, v in freqDict.items():
                    f.write(str(k) + ':' + str(v) + ' ')
                f.write('#label#:' + folder + '\n')
    f.close()


if __name__ == '__main__':
    starttime = time.time()
    preProcess('train', '20news-bydate/20news-bydate-train')
    preProcess('test', '20news-bydate/20news-bydate-test')
    endtime = time.time()
    print(endtime - starttime)