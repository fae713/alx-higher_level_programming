//A JavaScript that toggles the class of the header element 
$('div#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
        $('header').removeClass('red').addClass('green');
    } else {
        $('header').removeClass('green').addClass('red');
    }
});
