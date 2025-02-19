// script that updates text of a header
const $ = window.$;
$('#update_header').bind('click', function () {
  $('header').replaceWith('New Header!!!');
});
