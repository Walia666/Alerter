function log_type_validate_csv()
        {
                var log_type = document.getElementById("log_type_id").value;
                if(log_type!="")
                {
                        document.getElementById("validate_log_type_form_csv").submit();
                }
                else
                {
                        alert("Select valid log type");
                }
        }



function loadModule()
                        {
                            var domainname = document.getElementById("domain").value;
                            if(domainname=='')
                            {
                              //  alert('Please select domain first');
                            }
                            else
                            {
                               // alert('you selected domain');
                                $.ajax({
                                                type: "POST", 
                                                url: "create_csv.php", 
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
                        }
						
						
 function validateform()
    {
	var log_type = document.getElementById("log_type_id").value;
        var domain = document.getElementById("domain").value;
        var module = document.getElementById("module").value;
        var level = document.getElementById("level").value;
        var from_date = document.getElementById("datetime_from").value;
        var to_date = document.getElementById("datetime_to").value;
    if(!log_type=='')
     {
        if (!domain=='') 
        {
                if (!module=='') 
                {
                    if (!level=='') 
                        {
                            if (!from_date=='') 
                                {
                                    if (!to_date=='') 
                                        {
                                                document.getElementById("submit_form").submit();  
                                                return true;

                                        }
                                        else
                                        {
                                            alert('Please select "To" date!!');
                                            document.getElementById("datetime_to").focus();
                                            return false;
                                        }
                                }
                                else
                                {
                                    alert('Please select "From" date!!');
                                    document.getElementById("datetime_from").focus();
                                    return false;
                                }
                        }
                        else
                        {
                            alert('Please select level!!');
                            document.getElementById("level").focus();
                            return false;
                        }
                }
                else
                {
                    alert('Please select module!!');           
                    document.getElementById("module").focus();
                    return false;
                }
        }
        else
        {
            alert('Please select domain!!');
            document.getElementById("domain").focus();
            return false;
        }
     }
    else
     {
	alert('Please select Log Type!!');
            document.getElementById("log_type_id").focus();
            return false;
     }

        //alert(from_date);

    }