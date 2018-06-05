 #Converting Query to kibana query using escapes starts here
    newquery=""
    for x in kibana_query1[0]:
            temp = x
            
            if(x== '"'):
              temp=temp.replace('"','\"')

              newquery +=temp
            elif(x=='\\'):
              temp=temp.replace('\\','\\\\')
              newquery +=temp
            else:
              newquery += x 