/**
 * Created by ericsato on 2/10/15.
 */
var main = function() {
    $(".handsup-button").click(function() {
        $(".hands-up").toggle(700);
        $(".section-title").toggle(700);
        $(".hands-are-up").toggle(700);
    });
    $(".hands-up").click(function() {
        $(".dont-touch-me").addClass("visible");
    })

};

$(document).ready(main);