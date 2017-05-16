$(document).ready(function() {

    var generateTweetButton = document.getElementById("generate-tweet");

    function generateTweetText() {
        var twitterHandle = document.getElementById("twitter-handle");
        $.get("/markovify", {"twitter-handle": twitterHandle}, displayTweet)
    }

    generateTweetButton.onclick = generateTweetText

});