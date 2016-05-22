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
            product_select.append($('<option />').val(this.id).text(this.title));
        });
    });

    $('#id_submit').on('click', function(e) {
        var form = new FormData();
        form.append('shopify_product_id', product_select.val().toString());
        form.append('wish', WISH_ID);

        $.ajax({
            'async': true,
            'crossDomain': true,
            'url': '/api/v1/offers/',
            'method': 'POST',
            'headers': {
                'authorization': 'Token ' + INTERNAL_ACCESS_TOKEN,
                'cache-control': 'no-cache'
            },
            'processData': false,
            'contentType': false,
            'mimeType': 'multipart/form-data',
            'data': form,

            success: function() {
                alert('Your offer was submited.')
            },

            error: function() {
                alert('We have a problem processing your request, please try again later.');
            },
        });

        product_select.prop('disabled', true);
        $(this).prop('disabled', true);

        e.preventDefault();
    });
});
