function myFunction() {

    
    var log = document.getElementById("id_log_field").value;
     
    var arr=[]
    var val=[]
    var arry=[]

$.ajax({
    type: 'POST',
   data: { 
     log: log
  }, 
  url: '/crossdomainData/',
 
    success:function(data){
        for(var key in data)
          {
          arry.push(key)  
              
               }
         d1=arry[0]
         console.log(d1);
         console.log(data);
         var res = d1.split("2");
         var index=res[0]+"*"
         console.log(index);	
         if (index == "access_log-*") {
           result1=data[d1]['mappings']['access_log']['properties']
           }
         else if(index == "error_log-*" || index =="ssl_error-*"){
           result1=data[d1]['mappings']['error_log']['properties']
              }
         else if(index == "audit_log-*"){
           result1=data[d1]['mappings']['audit_log']['properties']
              }
         else if(index == "modsec_log-*"){
           result1=data[d1]['mappings']['modsec_log']['properties']
              }
	 else if(index == "ssl_request-*")
	{
          result1=data[d1]['mappings']['_default_']['properties']
 }   
         else if(index == "varnish_log-*")
        {
         result1=data[d1]['mappings']['varnish_log']['properties']

            
             }
         else if(index == "mysql-audit-*")
        {
         result1=data[d1]['mappings']['audit_mysql_log']['properties']


             }   
       else {
         result1=data[d1]['mappings']['app_log']['properties']

 }
    console.log(result1);

        
        for (var key in result1) {
            arr.push(key) 
        }
      var arrayLength = arr.length;
var container = document.getElementById("formfield");
    
 
           
            // Clear previous contents of the container
            while (container.hasChildNodes()) {
                container.removeChild(container.lastChild);
            }

 
            for (i=0;i<=arrayLength;i++){
    var newTextBoxDiv = $(document.createElement('checkbox'))
    if(arr[i] == "@timestamp")
       {
  newTextBoxDiv.after().html(
        ' <input type="checkbox" name="'+arr[i] + 
        '" id="m' + i + '" value="member' + i + '" onclick="return false;" checked> <label for ="m' + i + '">' + arr[i] +' </label>' )

}
else {

  newTextBoxDiv.after().html(
        ' <input type="checkbox" name="'+arr[i] + 
        '" id="m' + i + '" value="member' + i + '"  > <label for ="m' + i + '">' + arr[i] +' </label>' )


}
        

newTextBoxDiv.appendTo("#formfield");
 }
 
newTextBoxDiv.after().html(   '<input type="hidden" name="data" id="sms" value="'+ arr +'" >');
newTextBoxDiv.appendTo("#formfield")
  


    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){
        console.log(textStatus);
    }
});






}

   

