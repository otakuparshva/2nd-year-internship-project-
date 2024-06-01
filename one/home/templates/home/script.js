$(document).ready(function() {
    $('#play-button').click(function() {
        // Handle the "Play Now" button click event
        console.log("Play Now button clicked!");
        alert("Let's play the game!");
    });

    // Additional animations or interactivity can be added here
    $('nav a').hover(function() {
        $(this).addClass('animate-pulse');
    }, function() {
        $(this).removeClass('animate-pulse');
    });
});
/* JavaScript */

// Button Pulse
setInterval(function() {
    $('#play-button').toggleClass('pulse');
}, 1000);
