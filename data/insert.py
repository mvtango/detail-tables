# coding: utf-8

import csv
import dataset
import pprint

src=csv.DictReader(open("source.csv"))
store=dataset.connect('sqlite:///data.db')

store.query("drop table dietes")
nameindex=dict()
pid=0

with dataset.connect('sqlite:///data.db') as store :
    while True :
        try :
            r=src.next()
        except StopIteration :
            break
        for k in r.keys() :
            if type(k)==type("") :
                r[k]=unicode(r[k],"utf-8")
            if len(r[k])>0 and r[k][0]==u"€" :
                r[k]=float(r[k][1:].replace(",",""))
            if (r[k]==u"") and k in ("retribucio","total","r2013") :
                r[k]=None
            if (r[k]==u"") and k in ("dieta","dietes") :
                r[k]=0.0
        if r["carrec"][0]=="|" :
            r["pos"]=r["carrec"][2:]
        else :
            r["pos"]=""
        if not r["nom"] in nameindex :
            nameindex[r["nom"]]=pid
            pid=pid+1
        r["pid"]=nameindex[r["nom"]]
        try :
            store['dietes'].insert(r)
        except Exception, e :
            print "Error %s inserting %s" % (e,pprint.pformat(r))
   



