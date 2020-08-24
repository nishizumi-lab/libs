$('.button').on('click', function(){
  $.ajax({
    url: $(this).parent('form').attr('action'),
    type: 'post',
    data: $(this).parent('form').serialize()
  });
});