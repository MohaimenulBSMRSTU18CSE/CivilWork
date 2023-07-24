var buttonclick = document.getElementById('add_more_field');
var counter = 1;
buttonclick.addEventListener('click',()=>{
    counter += 1;
    var html='<div class="row" id="row'+counter+'">'+
                    '<div class="col-6">'+
                        '<label>Number of Pieces</label>'+
                        '<input type="number" name="number'+counter+'" class="form-control" placeholder="000">'+
                    '</div>'+
                    '<div class="col-6">'+
                        '<label>Length</label>'+
                        '<input type="number" name="lenght'+counter+'" class="form-control" placeholder="... in Feets">'+
                    '</div>'+
                '</div>';
    const total_form =  document.getElementById('total_form');
    total_form.value = counter
    $('#total_form').val(counter)
    $('#product_form').append(html)

})