#! python
# (C) 2017 Ezhil Language Foundation
#  This code is released under public domain.
import os
import glob
import tamil
import codecs
import re
import pprint
from operator import itemgetter

FLIST = []

def get_words(filename):
    with codecs.open(filename,"r","UTF-8") as fp:
        data  = fp.read()
        words = re.split("\s+",data)
        nwords = len(words)
        njunk = 0
        for w in words:
            if re.search("^\d+",w):
                njunk+=1
            elif re.search("^[-|+|/|\(|\)|\[|\]]+",w):
                njunk+=1
        letters = tamil.utf8.get_letters(data)
        ntamil = len( tamil.utf8.get_tamil_words( letters ) )
        return (max(ntamil,nwords-njunk),ntamil)
    return (0,0)

def process(fd):
    if os.path.isdir(fd):
        for f_or_d in glob.glob(os.path.join(fd,'*')):
            if os.path.isdir( f_or_d): 
                for x in process( f_or_d ):
                    yield x
            else:
                yield f_or_d
    else:
        yield fd

def start(s_dir):
    md_files = filter(lambda x: x.endswith('.md'),list(process(s_dir)))
    fd_perc = { fd: handlefile(fd) for fd in md_files }
    return fd_perc

def handlefile(fd):
    if fd.endswith(u".md"):
        tot,tam=get_words(fd)
        a = tot-tam
        b = tam
        FLIST.append( [fd, {'lang_eng':a,'lang_tam':b,'perc':(b)/float(a+b)}] )
        #print(u"%s => %f %%"%(fd.replace(basename,''),100.0*float(b)/(a+b)))
        return 100.0*float(b)/float(a+b)
    return 0.0

basename = ''
if __name__ == u"__main__":
    basename = os.getcwd()
    fd_perc  = start(os.getcwd())

    fd_perc = [(k,v) for k,v in fd_perc.items()] 
    fd_perc2 = sorted(fd_perc,key=itemgetter(1))
    for it in fd_perc2:
        if it[1] < 0.0: continue
        print(u"%2.4f%% => %s"%(it[1],it[0]))
    
    print('completion => %f%%'%(100.0*sum([x[1]['perc'] for x in FLIST])/len(FLIST)))

    
    
