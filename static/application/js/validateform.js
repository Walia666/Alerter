function validateform()
  {
    
    var log_type = document.getElementById("log_type_id").value;
    var alert_name = document.getElementById("alert_name_id").value;
    var time_frame = document.getElementById("time_frame_id").value;
    var level_name = document.getElementById("level").value;
    var error_name = document.getElementById("error_name").value;
    var conditional_operator_name = document.getElementById("conditional_operator_id").value;
    var count_name = document.getElementById("match_field_count").value;
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
            if(!level_name==0||null)
            {
              if (!conditional_operator_name==0||null) 
              {
                if (!count_name==0||null) 
                {
                  if (severity=='low' || severity=='moderate' ||severity=='high') 
                  {
                       if(!email1==0 ||!email1==null||!sms1==0||!sms1==null||!call1==0||!call1==null)
                    {
                                                                                document.getElementById("submit_form").submit();
                    }
                    else
                    {
                      alert("Select notification method first!!");
                    }
                  }
                  else
                  {
                    alert("Select alert severity!!!");
                  }
                }
                else
                {
                  alert("Enter valid count to match!!!");
                  document.getElementById("match_field_count").focus();
                }
              }
              else
              {
                alert("Select match operator first!!!");
                document.getElementById("conditional_operator_id").focus();
              }
            }
            else
            {
              alert("Enter error level!!!");
              document.getElementById("level").focus();
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
