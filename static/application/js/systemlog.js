//========================================Textboxes for Emails starts here==============================================
$(document).ready(function(){


//Key press event in time taken for integer or float value only
$('#time_taken_id').keypress(function(event) {
  if ((event.which != 46 || $(this).val().indexOf('.') != -1) && event.which != 8 && (event.which < 48 || event.which > 57)) {
    event.preventDefault();
  }
});


//Key press event in time taken for integer or float value only
$('#match_field_count').keypress(function(event) {
  if ((event.which != 46 || $(this).val().indexOf('.') != -1) && event.which != 8 && (event.which < 48 || event.which > 57)) {
      event.preventDefault();
  }
});


    var time_series_control = $('input[name=time_series]:checked').val();
    if(time_series_control == 'time_series_disable'){
	$('#comp_div').hide();
    }
    $('input[type=radio][name=time_series]').change(function() {
        if (this.value == 'time_series_disable') {
	    $('#comp_div').hide();
	    $('#rm_div').show();
        }
        else if (this.value == 'time_series_enable') {
	    $('#comp_div').show();
	    $('#rm_div').hide();
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

	

function validatelist()
	{
		var log_type = document.getElementById("log_type_id").value;

		if(log_type=="")
		{
			alert("Select List");
			return false;
		}
		else
		{
			return true;
		}
	
		
	}

function deleteAlert(alertname)
{
	var alert_name = alertname;
	var user_id = '<?php echo $userid; ?>';
//	alert(user_id);

	var r = confirm("Do you want to delete this alert!!!");
if (r == true) 
	{
			$.ajax({
                            type: "POST", 
                            url: "deleteAlert.php", 
                            data:{'userid':user_id,'alertname':alert_name},   
                            success: function(finalresult)
                            {
                            	//var finalresult=JSON.parse(finalresult);
                            	location.reload();
                            	//alert(finalresult);
                            }
 				});
	} 
	else 
	{
    //x = "You pressed Cancel!";
	}	
}



	function log_type_validate()
	{
		var log_type = document.getElementById("log_type_id").value;
		if(log_type!="")
		{
			document.getElementById("validate_log_type_form").submit();
		}
		else
		{
			alert("Select valid log type");
		}
	}



	function load_fields(userid, userlevel)
	{
		var log_type = document.getElementById("log_type_id").value;
		var log_index = document.getElementById("log_index_id").value;
		var user_id = userid;
		if(log_index == "")
		{
			alert("Select Valid Index");
		}
		else if(userlevel =="1" || userlevel =="2")
		{
			alert("You cannot set alert at this user level");
			document.getElementById("log_index_id").disabled=true;
			 document.getElementById("log_type_id").disabled=true;
			document.getElementById("mySubmit").disabled=true;
		}
		else
		{
                    $.ajax({
                            type: "POST",
                            url: "otheralert_to_database.php",
                            data:{'userid':user_id,'logtype':log_type,'logindex':log_index},
                            success: function(finalresult)
                            {
				console.log(finalresult);
                                var finalresult=JSON.parse(finalresult);
				console.log(finalresult);
				var options = '';
					options += '<option value="" >Select Field</option>';
				 for(var i = 0; i < finalresult.length; i++)
                                    options += '<option value="'+finalresult[i]+'" >'+finalresult[i]+'  </option>';
                                document.getElementById('other_field1_select_id').innerHTML = options;
				document.getElementById('other_field2_select_id').innerHTML = options;
				document.getElementById('other_field3_select_id').innerHTML = options;
				document.getElementById('other_field4_select_id').innerHTML = options;
                            }
                             });
		}
	}
	



 function validateform()
  {
    var log_index =document.getElementById("log_index_id").value; 
    var alert_name =document.getElementById("alert_name_id").value;
    var field1select =document.getElementById("other_field1_select_id").value;
    var textfield1 =document.getElementById("other_field1_id").value;
    var field1logical =document.getElementById("field1_logical").value;

    var field2select =document.getElementById("other_field2_select_id").value;
    var textfield2 =document.getElementById("other_field2_id").value;
    var field2logical =document.getElementById("field2_logical").value;

    var field3select =document.getElementById("other_field3_select_id").value;
    var textfield3 =document.getElementById("other_field3_id").value;
    var field3logical =document.getElementById("field3_logical").value;

    var field4select =document.getElementById("other_field4_select_id").value;
    var textfield4 =document.getElementById("other_field4_id").value;
    var field4logical =document.getElementById("field4_logical").value;

    var conditional_operator_name = document.getElementById("conditional_operator_id").value;
    var count_name = document.getElementById("match_field_count").value;
    var timeframe = document.getElementById("other_time_frame_id").value;

    var timetype = document.getElementById("time_type_select_id").value;
    var timeoperator = document.getElementById("time_operator_id").value;
    var time_taken_value = document.getElementById("time_taken_id").value;


    var email1 = document.getElementById("email1").value;
    var sms1 = document.getElementById("sms1").value;
    var severity = $('input[name=severity]:checked').val();
    var time_series_control = $('input[name=time_series]:checked').val();
    var comp1_time_series = document.getElementById("comp1_time_series_id").value;
    var comp2_time_series = document.getElementById("comp2_time_series_id").value;
    var comp1_threshold = document.getElementById("comp1_threshold_id").value;
    var comp2_threshold = document.getElementById("comp2_threshold_id").value;
    var time_taken_vaidate = false;
    var field1_validated = false;
    var field2_validated = false;
    var field3_validated = false;
    var field4_validated = false;
if(!log_index=="")
{
  if(!alert_name=="")
  {
               if(time_series_control == "time_series_disable" )
               {
                if(conditional_operator_name == "")
                {
                 alert("Select Conditional Operator!!!");
                 document.getElementById("conditional_operator_id").focus();
                 return false;
                }
                else if(count_name == "")
                {
                alert("Enter Count!!!");
                document.getElementById("match_field_count").focus();
                return false;
                }
               }else{
                  conditional_operator_name = '';
                  count_name = '';
                }
                /*Field filter validation starts here*/
              if(field1select != '' || field2select != '' || field3select != '' || field4select != '')
              {
                if(field1select!=""){
                  if(textfield1!=""){
                    if(field1logical!=""){
                      field1_validated = true;
                    }else{
                      alert("Select Logical operator!!!");
                      document.getElementById("field1_logical").focus();
                      return false;
                     }
                  }else{
                    alert("Enter Value!!!");
                    document.getElementById("other_field1_id").focus();
                    return false;
                  }
                }
                if(field2select!=""){
                  if(textfield2!=""){
                    if(field2logical!=""){
                      field2_validated = true;
                    }else{
                      alert("Select Logical operator!!!");
                      document.getElementById("field2_logical").focus();
                      return false;
                     }
                  }else{
                    alert("Enter Value!!!");
                    document.getElementById("other_field2_id").focus();
                    return false;
                  }
                }
                if(field3select!=""){
                  if(textfield3!=""){
                    if(field3logical!=""){
                      field3_validated = true;
                    }else{
                      alert("Select Logical operator!!!");
                      document.getElementById("field3_logical").focus();
                      return false;
                     }
                  }else{
                    alert("Enter Value!!!");
                    document.getElementById("other_field3_id").focus();
                    return false;
                  }
                }
                if(field4select!=""){
                  if(textfield4!=""){
                    if(field4logical!=""){
                      field4_validated = true;
                    }else{
                      alert("Select Logical operator!!!");
                      document.getElementById("field4_logical").focus();
                      return false;
                     }
                  }else{
                    alert("Enter Value!!!");
                    document.getElementById("other_field4_id").focus();
                    return false;
                  }
                }
              }
              else{
                  alert("Select atleast one from Field filter!!!");
                  return false;
              }
              /*Field filter validation ends here*/
        if(timeframe!="")
        {
         if(timetype == 'time_s' || timetype == 'time_ms'){
          if(timeoperator != ''){
           if(time_taken_value != ''){
             time_taken_validate = true;
           }
           else{
               alert("Enter time!!!");
               document.getElementById("time_taken_id").focus();
               return false;
           }
          }
          else{
              alert("Select time operator!!!");
              document.getElementById("time_operator_id").focus();
              return false;
          }
         }
        if(email1!="" || sms1!="")
        {
         if(time_series_control == "time_series_enable" ){
          if (((!comp1_time_series == 0 || null) && (!comp1_threshold == 0 || null))|| ((!comp2_time_series == 0 || null) && (!comp2_threshold == 0 || null))){ var time_series_validate = true;  }else{ 
            alert("Select time series and threshold!!!");
            return false; }}
         if(severity=='low' || severity=='moderate' ||severity=='high')
         { 
          if(field1_validated === true || field2_validated === true || field3_validated === true || field4_validated === true){
              document.getElementById("submit_form").submit();
              return true;
          }
          else{
            alert("Select Field filter");
            return false;
          }
         }
         else
         {  
            alert("Select severity!!!");
            return false;
         }
        }
        else
        {  
          alert("Enter alert method!!!");
          document.getElementById("email1").focus();
          return false;
        }
        }
      else
      { 
       alert("Select timeframe!!!");
       document.getElementById("other_time_frame_id").focus();
       return false;
      }  
  }
  else
  {
  alert("Enter Alert name!!!");
  document.getElementById("alert_name_id").focus();
  return false;
  }
  }
  else
{
alert("Select log index!!!");
document.getElementById("log_index_id").focus();
return false;
}

}
