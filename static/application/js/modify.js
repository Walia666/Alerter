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
function validateform(alert_id)
  { 

      var kibana_query =document.getElementById("kibana_query_id"+alert_id).value;
    if (kibana_query == "") {
        alert("Kibana query must be filled out");
        document.getElementById("kibana_query_id"+alert_id).focus();
        return false;
      }

    var alert_name = document.getElementById("alert_name_id"+alert_id).value;
    if (alert_name == "") {
        alert("Alert name must be filled out");
        document.getElementById("alert_name_id"+alert_id).focus();
        return false;
    }
    var time_frame = document.getElementById("time_frame_id"+alert_id).value;
    if (time_frame == "") {
        alert("Time frame must be filled out");
        document.getElementById("time_frame_id"+alert_id).focus();
        return false;
      }
   
          var email1 = document.getElementById("email1"+alert_id).value;
           var sms1 = document.getElementById("sms1"+alert_id).value;
      if(sms1 == "" && email1 == "")
        {
          alert("Select Notication method");
          document.getElementById("sms1"+alert_id).focus();
          document.getElementById("sms1"+alert_id).focus();
          return false;
         } 

    var y = document.getElementById("match_field_count"+alert_id).value;

    
    if (isNaN(y)) {
        alert("Count not valid");
        document.getElementById("match_field_count"+alert_id).focus();
        return false;


}
 var z1 = document.getElementById("email1"+alert_id).value
    var atpos = z1.indexOf("@");
    var dotpos = z1.lastIndexOf(".");
    if(z1 != "")
     {
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z1.length) {
        alert("Not a valid e-mail address");
        document.getElementById("email1"+alert_id).focus();
        return false;
    }
     }
    var x1 = document.getElementById("sms1"+alert_id).value;

    if (x1!="")
      {
    if (isNaN(x1) || x1.length < 10 || x1.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms1"+alert_id).focus();
        return false;

}
}
var z2 = document.getElementById("email2"+alert_id).value
if(z2 != "")
{
    var atpos = z2.indexOf("@");
    var dotpos = z2.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z2.length) {
        alert("Email 2 is not valid");
        document.getElementById("email2"+alert_id).focus();
        return false;
    } }
var x2 = document.getElementById("sms2"+alert_id).value;
if(x2 != "")
{
    
    if (isNaN(x2) || x2.length < 10 || x2.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms2"+alert_id).focus();
        return false;

} 
}

var z3 = document.getElementById("email3"+alert_id).value
if(z3 != "")
{
    var atpos = z3.indexOf("@");
    var dotpos = z3.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z3.length) {
        alert("Email 3 is not valid");
        document.getElementById("email3"+alert_id).focus();
        return false;
    }
  }
var x3 = document.getElementById("sms3"+alert_id).value;
if (x3 != "")
{
    
    if (isNaN(x3) || x3.length < 10 || x3.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms3"+alert_id).focus();
        return false;

}
}

var z4 = document.getElementById("email4"+alert_id)
if (z4 != "")
{
    var atpos = z4.indexOf("@");
    var dotpos = z4.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z4.length) {
        alert("Email 4 is not valid");
        document.getElementById("email4".alert_id).focus();
        return false;
    }
  }
var x4 = document.getElementById("sms4"+alert_id).value;
if (x4 != "")
{
    
    if (isNaN(x4) || x4.length < 10 || x4.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms4").focus();
        return false;

}
}

var z5 = document.getElementById("email5"+alert_id)
if (z5 != "")
{
    var atpos = z5.indexOf("@");
    var dotpos = z5.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=z5.length) {
        alert("Email 5 is not valid");
        document.getElementById("email5").focus();
        return false;
    }
  }
var x5 = document.getElementById("sms5"+alert_id).value;
if (x5 != "")
{
    
    if (isNaN(x5) || x5.length < 10 || x5.length > 11) {
        alert("Phone number not valid");
        document.getElementById("sms5"+alert_id).focus();
        return false;

}
}
}

function postponeAlert(alert_id,alertname)
{
                                var alert_id = alert_id;
                                var alert_name = alertname;
                                var postpone_id = alert_id + 'a';
                                var postpone_for = document.getElementById(postpone_id).value; 
                              
                                                     

		        var r = confirm("Do you want to Postpone this alert!!!");
                                if (r == true)
                                {

                                                $.ajax({
                                                    type: 'POST',
                                                    url: '/postpone/',
                                                    data:{'alertid':alert_id,'alert_name':alertname,'postpone_for':postpone_for},
                                                    success: function(finalresult)
                                                    {
                                                        var finalresult=JSON.parse(finalresult);
							alert("Alert has been postponed");
					//		console.log(finalresult);
                                                        location.reload();
                                                    }
                                                        });

                                }
                                else
                                {
                                }

 }





$(document).ready(function() {
    $('#maintable').DataTable( {
    } );
} );

$(document).ready(function() {
    $('#modifytable').DataTable( {
    } );
} );

