    body={
         
  "trigger" : {
    "schedule" : { 'interval':'20s' }},
  "input" : {
    "search" : {
      "request" : {
        "indices" : [
          indexmain
        ],
        "body" : {
          "query" : {
            "bool" : {
              "query_string": {
            "query":kibana  }
                }
              },
              "filter" : {
                "range": {
                  "@timestamp": {
                    "from": tme[time],
                    "to": "now"
                  }
                }
              }
            }
          }
        }
      },
    
  
  "condition" : {
    "compare" : { "ctx.payload.hits.total" : { "gt" : 0 }}
  },
   "actions": {
        "log" : {
       "logging" : {
         "text" : "alert was sent"
       }
     }
  } })



'condition': {  'compare': { countint:{"gt": thresh} } },