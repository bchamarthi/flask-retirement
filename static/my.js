$(document).ready(function () {
    $(function () {
        $('#addBtn').on('click', function () {
            $("#cntr_list").prepend('<li><label><input type="checkbox" value="ON" class="test" />' + $('#userInput').val() + '</label></li>');
        });
    });
});


  