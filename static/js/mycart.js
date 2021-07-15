
$('.itee').click(function() {
    $('#myAlert').show('fade');

        setTimeout(function () {
            $('#myAlert').hide('fade');
        }, 5000);
    
    var id = $(this).attr("pid").toString();
    console.log(id)

    $.ajax({
        type:"GET",
        url:"/add_to_cart",
        data:{
            prod_id: id
        },
        success: function(data){
            console.log(data)
            console.log("Success")
            //document.getElementById("totalpurchased1").innerText = data.totalpurchased
        }
    })
})

$('.qty-plus').click(function(){
    var id=$(this).attr("pid").toString();
    //var eml=this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success: function(data){
            document.getElementById(id).value=data.quantity
            document.getElementById("amount").innerText="Rs."+data.amount
            document.getElementById("totalamount").innerText="Rs."+data.totalamount
            document.getElementById("discount").innerText="Rs."+data.discount
        }
    })

})

$('.qty-minus').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success: function(data){
            document.getElementById(id).value=data.quantity
            document.getElementById("amount").innerText="Rs."+data.amount
            document.getElementById("totalamount").innerText="Rs."+data.totalamount
            document.getElementById("discount").innerText="Rs."+data.discount
            if(data.quantity<=0)
                eml.parentNode.parentNode.parentNode.remove()
        }
    })

})

$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    
    var eml=this
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success: function(data){
            document.getElementById(id).value=data.quantity
            document.getElementById("amount").innerText="Rs."+data.amount
            document.getElementById("totalamount").innerText="Rs."+data.totalamount
            document.getElementById("discount").innerText="Rs."+data.discount
            eml.parentNode.parentNode.remove()
        }
    })

})

$(document).ready(function () {
    $('#btnSubmit1').click(function () {
        $('#myAlert1').show('fade');

        setTimeout(function () {
            $('#myAlert1').hide('fade');
        }, 5000);

    });

    $('#linkClose1').click(function () {
        $('#myAlert1').hide('fade');
    });
});