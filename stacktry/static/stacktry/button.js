$(document).ready(function () {
    $('.increase-participation').on('click', function () {
        var button = $(this);
        var url = $(this).data('url') + '?_=' + new Date().getTime();

        var csrftoken = getCookie('csrftoken');

        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function (data) {
                console.log(data.updated_counts);

                var originalButtonText = button.text();
                button.text(originalButtonText + ' +1 参加増やした');
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown);
                console.log(jqXHR);
            }
        });
    });

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2) return parts.pop().split(";").shift();
    }
});


       document.addEventListener("DOMContentLoaded", function(event) {
          var targetElement = document.getElementById("scroll-target");

          if (targetElement) {
             targetElement.scrollIntoView({ behavior: 'smooth' });
          }
       });