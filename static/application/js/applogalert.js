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
//====================================================================================================================
//========================================Textboxes for Emails ends here==============================================


//========================================Textboxes for SMS starts here==============================================
$(document).ready(function(){



    var counter = 2;
    //$('[data-toggle="tooltip"]').tooltip(); 
    $("#addSms").click(function () {
  if(counter>5){
            alert("Only 5 Emails allowed!!!");
            return false;
  }   
  var newTextBoxDiv = $(document.createElement('div'))
       .attr("id", 'SmsDiv' + counter);
  newTextBoxDiv.after().html(
        '<input type="text" name="contact_sms_name' + counter + 
        '" id="sms' + counter + '" value="" placeholder="Enter sms '+counter+'" >');
  newTextBoxDiv.appendTo("#sms_td");        
  counter++;
     });

     $("#removeSms").click(function () {
  if(counter<3){
          alert("Last Email box can't be removed");
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
//====================================================================================================================
//========================================Textboxes for SMS ends here==============================================

//========================================Textboxes for Call starts here==============================================
$(document).ready(function(){

    var counter = 2;
    
    $("#addCall").click(function () {
  if(counter>5){
            alert("Maximum 5 contacts can be called!!!!!");
            return false;
  }   
  var newTextBoxDiv = $(document.createElement('div'))
       .attr("id", 'CallDiv' + counter);
  newTextBoxDiv.after().html(     '<input type="text" name="contact_call_name' + counter + 
        '" id="call' + counter + '" value="" placeholder="Enter mobile no. '+counter+'">');
  newTextBoxDiv.appendTo("#call_td");       
  counter++;
     });



     $("#removeCall").click(function () {
  if(counter<3){
          alert("Last call contact can't be removed!!!");
          return false;
       }   
        
  counter--;
      
        $("#CallDiv" + counter).remove();
      
     });
    
     $("#getCallValues").click(function () {
    
  var msg = '';
  for(i=1; i<counter; i++){
      msg += "\n Textbox #" + i + " : " + $('#textbox' + i).val();
  }
        alert(msg);
     });
  });
//====================================================================================================================
//========================================Textboxes for Calls ends here==============================================

  function log_type_validate()
  {
    var log_type = document.forms["listform"]["log_type_name"].value;
    if (log_type == "") {
        alert("log type must be filled out");
        return false;
    }

}

  
  
 function validateform()
  {

    var alert_name = document.forms["myform"]["alert_name"].value;
    if (alert_name == "") {
        alert("Alert name must be filled out");
        return false;
    }
    var time_frame = document.forms["myform"]["time_frame_name"].value;
    if (time_frame == "") {
        alert("Time frame must be filled out");
        return false;
      }
     var kibana_query = document.forms["myform"]["kibana_query"].value;
    if (kibana_query == "") {
        alert("Kibana query must be filled out");
        return false;
      }
       var operator = document.forms["myform"]["conditional_operator"].value;
    if (operator == "") {
        alert("Conditional operator must be filled out");
        return false;
      }
        var count = document.forms["myform"]["match_field_count_name"].value;
    if (count == "") {
        alert("Count must be filled out");
        return false;
      }
          var email1 = document.forms["myform"]["email_name1"].value;
    if (email1 == "") {
        alert("Email must be filled out");
        return false;
      }
      

           var call1 = document.forms["myform"]["contact_call_name1"].value;
    if (call1 == "") {
        alert("Number must be filled out");
        return false;
      }
          var sms1 = document.forms["myform"]["contact_sms_name1"].value;
    if (sms1 == "") {
        alert("SMS must be filled out");
        return false;
      }
      var sms2 = document.forms["myform"]["contact_sms_name2"].value;
    if (sms2 == "") {
        alert("SMS must be filled out");
        return false;
      }
       var email2 = document.forms["myform"]["email_name2"].value;
       if (email2 == "") {
        alert("Email must be filled out");
        return false;
      }

          var call2 = document.forms["myform"]["contact_call_name2"].value;
    if (call2 == "") {
        alert("Number must be filled out");
        return false;
      }
      var sms3 = document.forms["myform"]["contact_sms_name3"].value;
    if (sms3 == "") {
        alert("SMS must be filled out");
        return false;
      }
          var email3 = document.forms["myform"]["email_name3"].value;
    if (email3 == "") {
        alert("Email must be filled out");
        return false;
      }

           var call3 = document.forms["myform"]["contact_call_name3"].value;
    if (call3 == "") {
        alert("Number must be filled out");
        return false;
      }
      var sms4 = document.forms["myform"]["contact_sms_name4"].value;
    if (sms4 == "") {
        alert("SMS must be filled out");
        return false;
      }
       var email4 = document.forms["myform"]["email_name4"].value;
    if (email4 == "") {
        alert("Email must be filled out");
        return false;
      }

           var call4 = document.forms["myform"]["contact_call_name4"].value;
    if (call4 == "") {
        alert("Number must be filled out");
        return false;
      }
      var sms5 = document.forms["myform"]["contact_sms_name5"].value;
    if (sms5 == "") {
        alert("SMS must be filled out");
        return false;
      }
      var email5 = document.forms["myform"]["email_name5"].value;
    if (email5 == "") {
        alert("Email must be filled out");
        return false;
      }

           var call5 = document.forms["myform"]["contact_call_name1"].value;
    if (call5 == "") {
        alert("Number must be filled out");
        return false;
      }

       var severity = document.forms["myform"]["severity"].value;
    if (severity == "") {
        alert("Severity must be filled out");
        return false;
      }

   var y = document.getElementById("match_field_count").value;

    
    if (isNaN(y)) {
        alert("Count not valid");
        return false;

}
   var z1 = document.forms["myform"]["email_name1"].value;
    var atpos = z1.indexOf("@");
    var dotpos = z1.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z1.length) {
        alert("Not a valid e-mail address");
        return false;
    }

    var x = document.getElementById("sms1").value;

    
    if (isNaN(x) || x.length < 10 || x.length > 11) {
        alert("Phone number not valid");
        return false;

}
    var a = document.getElementById("call1").value;

    
    if (isNaN(a) || a.length < 10 || a.length > 11) {
        alert("Phone number not valid");
        return false;

}







 }