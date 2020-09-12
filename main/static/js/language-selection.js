var lang = "EN";

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

$(document).ready(function(){
  $('select').formSelect();
  lang = $('#lang input')[0].value;
  updateLanguage();
});

$('#lang').on('change', function() {
  lang = $('#lang input')[0].value;
  updateLanguage();
});

function updateLanguage(){
  if(lang == 'EN'){
    $('*[lang=en]').css('display', 'block');
    $('*[lang=de]').css('display', 'none');
    $('*[lang=pt]').css('display', 'none');
  }else if (lang == 'DE'){
    $('*[lang=en]').css('display', 'none');
    $('*[lang=de]').css('display', 'block');
    $('*[lang=pt]').css('display', 'none');
  }else{
    $('*[lang=en]').css('display', 'none');
    $('*[lang=de]').css('display', 'none');
    $('*[lang=pt]').css('display', 'block');
  }
}
