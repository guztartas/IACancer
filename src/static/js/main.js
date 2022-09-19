$(document).ready(function() {

    $(".custom-file-input").change(function() {
        var fileName = $(this).val().split("\\").pop();
        $(this).siblings(".custom-file-label").addClass("selected").html(fileName);
    });

    $('#upload-file').submit(function(event) {
        if (document.getElementById("customFile").files.length == 0) {
            event.preventDefault();
            alert("Insira uma imagem antes de fazer o teste");
        }
    });

    $('#submit-url').submit(function(event) {
        if (document.getElementById("url-input").value == "") {
            event.preventDefault();
            alert("Insira uma imagem antes de fazer o teste");
        }
    });
});