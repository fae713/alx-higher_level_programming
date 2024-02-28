//script that adds a <li> element to a list 
document.querySelector('div#add_item').click(function () {
    $('ul.my_list').first().append('<li>Item</li>');
});
