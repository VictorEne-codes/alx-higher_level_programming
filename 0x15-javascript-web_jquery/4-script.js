// script that toggles the class of the header
const $ = window.$;
$('#toggle_header').bind('click', function () {
  $('header').toggleClass('green red');
});
