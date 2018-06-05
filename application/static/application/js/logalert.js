//========================================Textboxes for Emails starts here==============================================
$(document).ready(function(){

  var time_series_control = $('input[name=time_series]:checked').val();
    if(time_series_control == 'time_series_disable'){
        $('#comparison_div').hide();
    }
    $('input[type=radio][name=time_series]').change(function() {
        if (this.value == 'time_series_disable') {
            $('#comparison_div').hide();
            $('#operator_count_div').show();
        }
        else if (this.value == 'time_series_enable') {
            $('#comparison_div').show();
            $('#operator_count_div').hide();
        }
     });       


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
function validateform()
  {
     
       var logtype = document.forms["myform"]["log_field"].value;
    if (logtype == "1") {
        alert("Log type must be filled out");
        document.getElementById("id_log_field").focus();
        return false;
      }
 
       var kibana_query = document.forms["myform"]["kibana_query_name"].value;
    if (kibana_query == "") {
        alert("Kibana query must be filled out");
        document.getElementById("kibana_query_id").focus();
        return false;
          }       

    var alert_name = document.forms["myform"]["alert_name"].value;
    if (alert_name == "") {
        alert("Alert name must be filled out");
        document.getElementById("alert_name_id").focus();
        return false;
    }
   
    var time_frame = document.forms["myform"]["time_frame_name"].value;
    if (time_frame == "") {
        alert("Time frame must be filled out");
        document.getElementById("time_frame_id").focus();
        return false;
      }
       var operator = document.forms["myform"]["conditional_operator"].value;   
       var timeseries = document.forms["myform"]["time_series"].value;
    if( timeseries == "time_series_disable")
      {
    if (operator == "") {
        alert("Conditional operator must be filled out");
        document.getElementById("conditional_operator_id").focus();
        return false;
      }
        
        var count = document.forms["myform"]["match_field_count_name"].value;
    if (count == "") {
        alert("Count must be filled out");
        document.getElementById("match_field_count").focus();
        return false;
      }
        }
     var sms1 = document.forms["myform"]["contact_sms_name1"].value;
     var email1 = document.forms["myform"]["email_name1"].value;
     if(sms1 == "" && email1 == "")
        {
          alert("Select Notication method");
          document.getElementById("email_td").focus();
          document.getElementById("sms_td").focus();
          return false;
         }   

    var y = document.getElementById("match_field_count").value;

    
    if (isNaN(y)) {
        alert("Count not valid");
          document.getElementById("match_field_count").focus();
        return false;


}

 var z1 = document.forms["myform"]["email_name1"].value;
    var atpos = z1.indexOf("@");
    var dotpos = z1.lastIndexOf(".");
    if(email1 != "")
        {
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z1.length) {
        alert("Not a valid e-mail address");
        document.getElementById("email1").focus();
        return false;
    }
      }

    var x1 = document.getElementById("sms1").value;

    if(sms1 != "")
        {    
    if (isNaN(x1) || x1.length < 10 || x1.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms1").focus();
        return false;

}
}
var z2 = document.forms["myform"]["email_name2"].value;
    var atposi = z2.indexOf("@");
    var dotposi = z2.lastIndexOf(".");
    if (atposi<1 || dotposi<atposi+2 || dotposi+2>=z2.length) {
        alert("Email 2 is not valid");
        document.getElementById("email2").focus();
        return false;
    }
var x2 = document.getElementById("sms2").value;

    
    if (isNaN(x2) || x2.length < 10 || x2.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms2").focus();
        return false;

}
var z3 = document.forms["myform"]["email_name3"].value;
    var atposk = z3.indexOf("@");
    var dotposk = z3.lastIndexOf(".");
    if (atposk<1 || dotposk<atposk+2 || dotposk+2>=z3.length) {
        alert("Email 3 is not valid");
        document.getElementById("email3").focus();
        return false;
    }
var x3 = document.getElementById("sms3").value;

    
    if (isNaN(x3) || x3.length < 10 || x3.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms3").focus();
        return false;

}
var z4 = document.forms["myform"]["email_name4"].value;
    var atposm = z4.indexOf("@");
    var dotposm = z4.lastIndexOf(".");
    if (atposm<1 || dotposm<atposm+2 || dotposm+2>=z4.length) {
        alert("Email 4 is not valid");
        document.getElementById("email4").focus();
        return false;
    }
var x4 = document.getElementById("sms4").value;

    
    if (isNaN(x4) || x4.length < 10 || x4.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms4").focus();
        return false;

}
var z5 = document.forms["myform"]["email_name5"].value;
    var atposn= z5.indexOf("@");
    var dotposn = z5.lastIndexOf(".");
    if (atposn<1 || dotposn<atposn+2 || dotposn+2>=z5.length) {
        alert("Email 5 is not valid");
        document.getElementById("email5").focus();
        return false;
    }
var x5 = document.getElementById("sms5").value;

    
    if (isNaN(x5) || x5.length < 10 || x5.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms5").focus();
        return false;

}





      }
