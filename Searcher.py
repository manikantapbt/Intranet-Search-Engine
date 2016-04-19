from whoosh import qparser
from whoosh.index import create_in
from whoosh.fields import *
import io
import shutil
from whoosh import scoring
import os
import whoosh.index as index
import termcolor
enc='utf-8'
'''
f=io.open('ACD.txt',"r+",encoding=enc)
f1=io.open('ACD.txt',"r+",encoding=enc)
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
ix = create_in("indexdir", schema)



writer = ix.writer()
writer.add_document(title=u"ACD", path=u"/a",
                     content=f.read())
writer.add_document(title=u"ACD1", path=u"os.path.abspath(f1)",
                     content=f1.read())
f.close()
f1.close()

writer.commit()


writer = ix.writer()
'''
os.system("color 17")

ix = index.open_dir("indexdir")

from whoosh.qparser import QueryParser
with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
     query = QueryParser("content", ix.schema).parse("modi")
     results = searcher.search(query,sortedby="content")
     for hits in results:
         print(hits["title"])
         termcolor.cprint(hits["title"], "blue")
         print(hits["path"])
         #f=(hits["path"])

         termcolor.cprint(hits["path"], "blue")
         path=hits["path"]
         path1 = path.encode('ascii')
         #print type(path)
         #print type(path1)
         print(hits.highlights("content"))
