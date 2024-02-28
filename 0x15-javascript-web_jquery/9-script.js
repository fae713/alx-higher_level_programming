// script that fetches from 
// https://hellosalut.stefanbohacek.dev/?lang=fr
window.onload = function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
};
