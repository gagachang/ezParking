$(document).ready(
  function() {
    setInterval(function() {
      $.ajax({
        type: 'GET',
        url: 'Refresh',
        success: function(data) {

  }
     });
  }, 5000);
});
