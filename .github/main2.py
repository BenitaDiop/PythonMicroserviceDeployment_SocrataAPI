from datetime import datetime
from elasticsearch import Elasticsearch
import os, sys
import json 
import argparse
from sodapy import Socrata 

domain = 'data.cityofnewyork.us'
client_id = 'nc67-uf89'
plug  = Socrata(domain, os.getenv("APP_KEY"))
data_count = plug.get(client_id, select ='COUNT(*)')
count = int(data_count[0]['COUNT'])


def get_stats():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--page_size', help= "To input records to request API", type=int)
    parser.add_argument('-n', '--num_pages', help= "The number of times to query for data",type=int)
    parser.add_argument('-o', '--output', default = None, help = "To print as .json or stdout")
    
    return parser.parse_args() 
    
 options = get_stats()



def its_elastic():
    es = Elasticsearch()
    try:
        es.indices.create('bigdata1')
    except:
        pass
    return es    

its_elastic()


def get_data(options, es):
    i = 0
    if not options.num_pages:
        options.num_pages = count // options.page_size + 1 

    if options.output and '.json' in options.output:
        with open(options.output, 'w') as results:
            pass

    for runs in range(options.num_pages):
        offset = options.page_size*runs
        outfile = plug.get(client_id, 
                         limit=options.page_size, 
                         offset=offset) #list        
        for r in outfile: 
            date = None
            time = None
            timestamp = datetime(1, 1, 1, 1, 1)
            for key, value in r.items(): 
                if "date" in key: 
                    date = datetime.strptime(value, '%m/%d/%Y').date()           
                if "time" in key: 
                    time = datetime.strptime(value+'M', '%I:%M%p').time()
                if 'amount' in key: 
                    r[key] = float(value)
            if date and time:
                timestamp = datetime.combine(date, time)
            if date and not time:
                timestamp = date
            if not date and time:
                timestamp = time
            r['timestamp'] = timestamp 
            
            i += 1
            
            res = es.index("bigdata", id=i, body = r)
get_data(options, es)
