$(document).ready(function() {
    $('#confirmButton').click(function() {
        var userText = $('#inputArea').val();
        $.ajax({
            url: '/get_response',
            data: { 'input': userText },
            type: 'POST',
            success: function(response) {
                $('#displayArea').html(response.table);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
  });
  
