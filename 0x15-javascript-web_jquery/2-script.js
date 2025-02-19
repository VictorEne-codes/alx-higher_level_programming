// JavaScript script that updates the text color to red
const $ = window.$;
$('#red_header').bind('click', function () {
  $('header').css({ color: '#FF0000' });
});
