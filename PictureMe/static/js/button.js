window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        document.getElementById("upHere").style.display = "block";
        document.getElementById("upHere").style.opacity = 1;
    } else {
        document.getElementById("upHere").style.display = "none";
        document.getElementById("upHere").style.opacity = 0;
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
