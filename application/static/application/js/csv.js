function validateform()
  {

      var logtype = document.forms["myform"]["log_field"].value;
    if (logtype == "1") {
        alert("Log type must be filled out");
         document.getElementById("id_log_field").focus();

        return false;
      }
       var kibana_query = document.forms["myform"]["kibana_query"].value;
    if (kibana_query == "") {
        alert("Kibana query must be filled out");
        document.getElementById("kibana_query_id").focus();
        return false;
      }
           var datefrom = document.forms["myform"]["datetime_from_name"].value;
    if (datefrom == "") {
        alert("Date must be filled out");
        document.getElementById("datetime_from").focus();
        return false;
      }

       var dateto = document.forms["myform"]["datetime_to_name"].value;
    if (dateto == "") {
        alert("Date must be filled out");
        document.getElementById("datetime_to").focus();
        return false;
      }
     
      var datechk = document.forms["myform"]["datetime_from_name"].value;
      if (!datechk.match(/^(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])-\d\d\d\d (0[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$/)) {
    alert('Date format is wrong');
    document.getElementById("datetime_from").focus();
      return false;       
  }
    var datechk1 = document.forms["myform"]["datetime_to_name"].value;
      if (!datechk1.match(/^(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])-\d\d\d\d (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$/)) {
    alert('Date format is wrong');
    document.getElementById("datetime_to").focus();
      return false;       
  }
}




