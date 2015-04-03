/**
 * Created by gregorylevin on 3/30/15.
 */




function cword(w) {

    var count = 0;
    var words = w.split(" ");

    for (i = 0; i < words.length; i++) {
        // inner loop -- do the count
        if (words[i] != "")
            count += 1;
        }
    }



$(document).ready(function(){

        var js_text = $(".text").text();
        console.log(js_text);
        console.log(cword(js_text));

//        $.ajax({
//            url: "http://text-processing.com/api/sentiment/",
//            data: {'text':js_text},
//            type: "POST",
//            success: function(result) {
//                console.log(result)
//            }
//        });

});