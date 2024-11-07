import { SentimentClient } from "./sentiment.mjs"

var messages = [
    "I loved staying at this hotel and will definitely come back again!",
    "This hotel was terrible and I want my money back."
]

var sentimentClient = new SentimentClient();
await sentimentClient.init();

for (var i = 0; i < messages.length; i++) {
    var sentiment = await sentimentClient.evaluate(messages[i]);
    console.log(`\nMessage: ${messages[i]}`);
    console.log(`Sentiment: ${JSON.stringify(sentiment)}`);
}