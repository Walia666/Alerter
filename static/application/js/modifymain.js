$(document).ready(function(){

    var counter = 2;
    
    $("#addSms").click(function () {
  if(counter>5){
            alert("Only 5 Contacts are allowed for SMS!!!");
            return false;
  }   
  var newTextBoxDiv = $(document.createElement('div'))
       .attr("id", 'SmsDiv' + counter);
  newTextBoxDiv.after().html(   '<input type="text" name="contact_sms_name' + counter + 
        '" id="sms' + counter + '" value="" placeholder="Enter mobile no. '+counter+'" >');
  newTextBoxDiv.appendTo("#sms_td");        
  counter++;
     });



     $("#removeSms").click(function () {
  if(counter<3){
          alert("Last Sms contact box can't be removed");
          return false;
       }   
        
  counter--;
      
        $("#SmsDiv" + counter).remove();
      
     });
    
     $("#getSmsValues").click(function () {
    
  var msg = '';
  for(i=1; i<counter; i++){
      msg += "\n Textbox #" + i + " : " + $('#textbox' + i).val();
  }
        alert(msg);
     });
  });

//========================================Textboxes for Emails starts here==============================================
$(document).ready(function(){



    var counter = 2;
    //$('[data-toggle="tooltip"]').tooltip(); 
    $("#addEmails").click(function () {
  if(counter>5){
            alert("Only 5 Emails allowed!!!");
            return false;
  }   
  var newTextBoxDiv = $(document.createElement('div'))
       .attr("id", 'EmailDiv' + counter);
  newTextBoxDiv.after().html(
        '<input type="text" name="email_name' + counter + 
        '" id="email' + counter + '" value="" placeholder="Enter Email '+counter+'" >');
  newTextBoxDiv.appendTo("#email_td");        
  counter++;
     });

     $("#removeEmails").click(function () {
  if(counter<3){
          alert("Last Email box can't be removed");
          return false;
       }   
        
  counter--;
      
        $("#EmailDiv" + counter).remove();
      
     });
    
     $("#getEmailValue").click(function () {
    
  var msg = '';
  for(i=1; i<counter; i++){
      msg += "\n Textbox #" + i + " : " + $('#textbox' + i).val();
  }
        alert(msg);
     });
  });


 function validateform()
  {

    var alert_name = document.forms["myform"]["alert_name"].value;
    if (alert_name == "") {
        alert("alert name must be filled out");
        return false;
    }
    var time_frame = document.forms["myform"]["time_frame_name"].value;
    if (time_frame == "") {
        alert("time frame must be filled out");
        return false;
      }
     var kibana_query = document.forms["myform"]["kibana_query"].value;
    if (kibana_query == "") {
        alert("kibana query must be filled out");
        return false;
      }
       var operator = document.forms["myform"]["conditional_operator"].value;
    if (operator == "") {
        alert("conditional operator must be filled out");
        return false;
      }
        var count = document.forms["myform"]["match_field_count_name"].value;
    if (count == "") {
        alert("count must be filled out");
        return false;
      }
          var email = document.forms["myform"]["email_name1"].value;
    if (email == "") {
        alert("email must be filled out");
        return false;
      }
           var call = document.forms["myform"]["contact_call_name1"].value;
    if (call == "") {
        alert("number must be filled out");
        return false;
      }
         var severity = document.forms["myform"]["severity"].value;
    if (severity == "") {
        alert("severity must be filled out");
        return false;
      }

   var y = document.getElementById("match_field_count").value;

    
    if (isNaN(y)) {
        alert("count not valid");
        return false;

}
   var z = document.forms["myform"]["email_name1"].value;
    var atpos = z.indexOf("@");
    var dotpos = z.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z.length) {
        alert("Not a valid e-mail address");
        return false;
    }
 
var x = document.getElementById("sms1").value;

    
    if (isNaN(x) || x.length < 10 || x.length > 11) {
        alert("phone number not valid");
        return false;

}
var a = document.getElementById("call1").value;

    
    if (isNaN(a) || a.length < 10 || a.length > 11) {
        alert("phone number not valid");
        return false;

}


 }