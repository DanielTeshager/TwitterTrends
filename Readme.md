# Word Cloud Animation | Twitter Trends

This is a simple web application that generates a word cloud animation using the Twitter API. The application uses the `tweepy` library to access the Twitter API and retrieve trending topics for a specified location.

## Getting Started

To use the word cloud animation, you will need to have a Twitter developer account and obtain API keys and access tokens. You will also need to install the `tweepy` library using pip:

To run the application, clone the repository to your local machine and open the `index.html` file in your web browser. You can then enter a location (e.g. "New York") and click the "Generate Trends" button to generate a word cloud animation of the current trending topics for that location.

## How it Works

The application retrieves trending topics for a specified location using the Twitter API. The trending topics are returned as an array of JSON objects, which are then processed and displayed as a word cloud animation using HTML, CSS, and JavaScript.

The application uses the `fetch()` function to retrieve the trending topics data from the server, and then uses the `createWordElement()` function to create a DOM element for each trending topic in the word cloud. The `generateColor()` function is used to generate a random color for each word, and the `fadeInOut` CSS animation is applied to each word element to create the animation effect.
