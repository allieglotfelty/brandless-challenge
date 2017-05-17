$(document).ready(function() {

    var generateTweetButton = document.getElementById("generate-tweet");

    function generateTweetText() {
        var twitterHandle = document.getElementById("twitter-handle").value;
        $.get("/markovify", {"twitter-handle": twitterHandle}, displayTweet);
    }

    function displayTweet(results) {
        console.log(results);
    }

    generateTweetButton.onclick = generateTweetText;

});