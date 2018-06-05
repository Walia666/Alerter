function validateform()
{
      var kibana_query = document.getElementById("kibana_query_id").value;
    if (kibana_query == "") {
        alert("Kibana query must be filled out");
        document.getElementById("kibana_query_id").focus();
        return false;
      }
  }