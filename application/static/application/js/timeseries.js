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
	
	function validateform()
	{
		var log_type = document.getElementById("log_type_id").value;
		var alert_name = document.getElementById("alert_name_id").value;
		var time_frame = document.getElementById("time_frame_id").value;
		var domain_name= document.getElementById("domain").value;
		var module_name = document.getElementById("module").value;
		var level_name = document.getElementById("level").value;
		var error_name = document.getElementById("error_name").value;
		var comp1_time_series = document.getElementById("comp1_time_series_id").value;
		var comp2_time_series = document.getElementById("comp2_time_series_id").value;
		var comp1_threshold = document.getElementById("comp1_threshold_id").value;
		var comp2_threshold = document.getElementById("comp2_threshold_id").value;
		var email1 = document.getElementById("email1").value;
		var sms1 = document.getElementById("sms1").value;
		var call1 = document.getElementById("call1").value;
		var severity = $('input[name=severity]:checked').val();

	if(!log_type==0)
	{
		if (!alert_name==0||null) 
		{
			if (!time_frame==0||null) 
			{
				if (!domain_name==0||null) 
				{
					if (!module_name==0||null) 
					{
						if(!level_name==0||null)
						{
							if (((!comp1_time_series == 0 || null) && (!comp1_threshold == 0 || null))|| ((!comp2_time_series == 0 || null) && (!comp2_threshold == 0 || null))){
							  if (severity=='low' || severity=='moderate' ||severity=='high') {
 							     if(!email1==0 ||!email1==null||!sms1==0||!sms1==null||!call1==0||!call1==null){
                                                	              document.getElementById("submit_form").submit();
							     }
							     else{
								 alert("Select notification method !!");
							     }
							  }
							  else{
							     alert("Select alert severity!!!");
							  }
							}
							else{
							   alert("Select Comparison 1 or Comparison 2!!!");
							   document.getElementById("comp1_time_series_id").focus();
							}
						}
						else{
						   alert("Enter error level!!!");
						   document.getElementById("level").focus();
						}
					}
					else{
					  alert("Enter module name!!!");
						document.getElementById("module").focus();
					}
				}
				else
				{
					alert("Select domain name!!!");
					document.getElementById("domain").focus();
				}
			}
			else
			{
				alert("Select time frame first!!!");
				document.getElementById("time_frame_id").focus();
			}
		}
		else
		{
			alert("Please Enter valid alert name!!!");
			document.getElementById("alert_name_id").focus();
		}
	       }
             else
	      {
		alert("Select log type");
	      }
 	}

	function loadModule()
						{
							var domainname = document.getElementById("domain").value;
							if(domainname=='')
							{
								//alert('Please select domain first');
							}
							else
							{
								$.ajax({
					                            type: "POST", 
					                            url: "home.php", 
					                            data:{'module_value_for_domain':domainname},   
					                            success: function(finalresult)
					                            {
					                            	var finalresult=JSON.parse(finalresult);
					                            	//alert(finalresult['0']);
					                            	var options = '';

													  for(var i = 0; i < finalresult.length; i++)
					 options += '<option value="'+finalresult[i]+'" >'+finalresult[i]+'  </option>';
													  document.getElementById('module').innerHTML = options;


					                            }
					 				});
							}
							//alert(domainname);
						
						}