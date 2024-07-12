function update_params() {
    var myObject = {};
    if ($('#select_order option:checked').length > 0) {
        myObject['order'] = $('#select_order option:checked').val()
    }
    if ($('#filter_rubric_list option:checked').length > 0) {
        myObject['filter_rubric'] = $('#filter_rubric_list option:checked').val()
    }
    window.location.href = location.protocol + '//' + location.host + location.pathname + '?' + decodeURIComponent( $.param( myObject ) );
}
$("#select_order").on("change", update_params );
$("#filter_rubric_list").on("change", update_params );