$(function() {
    product_select = $('#id_product_list');

    $.ajax({
        dataType: 'json',
        contentType: 'application/json',

        url: '/sales/proxy/',

        headers: {
            'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN
        }

    }).done(function(result) {

        $.each(result.products, function() {
            product_select.append($("<option />").val(this.id).text(this.title));
        });
    });

    $('#id_submit').on('click', function(e) {
        console.log(product_select.val().toString());
        var form = new FormData();
        form.append("shopify_product_id", 668209613);
        form.append("wish", WISH_ID);

        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "http://localhost:8000/api/v1/offers/",
            "method": "POST",
            "headers": {
                "authorization": "Token " + INTERNAL_ACCESS_TOKEN,
                "cache-control": "no-cache",
                "postman-token": "70ed18a6-aaea-38ab-4210-fec5b010fc7a"
            },
            'processData': false,
            'contentType': false,
            "mimeType": "multipart/form-data",
            "data": form
        }

        $.ajax(settings).done(function (response) {
            console.log(response);
        });

        e.preventDefault();
    });
});
