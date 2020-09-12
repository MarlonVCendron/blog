document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

$(document).ready(function(){
  $('select').formSelect();
});

$("#lang").on('change', function() {
  const newLang = $('#lang input')[0].value;
  console.log(newLang);
});
