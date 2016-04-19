from whoosh import qparser
from whoosh.index import create_in
from whoosh.fields import *
import io
import shutil
from whoosh import scoring
import os
import whoosh.index as index
import codecs

enc='utf-8'
path="ACD IN LOCAL FOLDER"

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
ix = create_in("indexdir", schema)
writer = ix.writer()
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if filename.endswith('.txt'):

           f=codecs.open(filename,"r+",encoding=enc)
           content=f.read()


           x=(os.path.splitext(os.path.basename(filename))[0])
           path=('ACD\\'+x+".html")
           path = unicode(path, "utf-8")
           filename = unicode(filename, "utf-8")
           writer.add_document(title=filename, path=path,content=content)
           f.close()
writer.commit()


writer = ix.writer()

#ix = index.open_dir("indexdir")
from whoosh.qparser import QueryParser
with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
     query = QueryParser("content", ix.schema).parse("Modi's ")
     results = searcher.search(query,sortedby="content")
     for hits in results:
         print(hits["title"])
         print(hits["path"])
         print(hits.highlights("content"))

