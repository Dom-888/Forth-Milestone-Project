// Replace all elements that have a data-feather attribute with a Feather icon
feather.replace();

// Show toast messages
$('.toast').toast('show');

// toTopButton

// When the user scrolls down 20px from the top of the document, show the return-to-top button
window.onscroll = function() { scrollFunction(); };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $("#toTopButton").show();
    } else {
        $("#toTopButton").hide();
    }
}

//  When the user clicks on the return-to-top button, scroll to the top of the document
function returnToTop() {
    $('html,body').animate({ scrollTop: 0 }, 'slow');
    console.log("porcoddio")
}