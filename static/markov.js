$(document).ready(function() {

    var generateTweetButton = document.getElementById("generate-tweet");

    function displayTweet(results) {
        var handle = results["twitter_handle"];
        var tweet = results["new_tweet"];
        alert(handle + ": " + tweet);
    }

    function generateTweetText() {
        var twitterHandle = document.getElementById("twitter-handle").value;
        $.get("/markovify", {"twitter-handle": twitterHandle}, displayTweet);
    }

    generateTweetButton.onclick = generateTweetText;

});