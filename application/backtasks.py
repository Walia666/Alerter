
@periodic_task(run_every=(crontab(minute='*/15')), name="elast", ignore_result=True)
def elast(request):
    es=Elasticsearch()
    doc = {
        'size' : 2000,
        'query': {
            'match_all' : {}
                },
        
       
        }
    res = es.search(index='hazard', doc_type='post', body=doc)
    count1=[]
    count2=[]
    time=[]
    operator=[]
    
    for row in res['hits']['hits']:
        
        abc= row["_source"]["kibana_query"]
        s = Search().using(es).query("match", kibana_query=abc)
        response=s.execute()
        count=response.hits.total
        
        count1.append(count)
        
        
        for hit in response:
            kibana_query_count=hit.count
            timeframe=hit.time_frame
            conditionaloperator=hit.conditional_operator

        count2.append(kibana_query_count)
        time.append(timeframe)
        operator.append(conditionaloperator)
    
            

    return render(request,'application/hit.html',{'count':count1,'threshold':count2,'time':time,'operator':operator})
