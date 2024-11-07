import { pipeline } from "@xenova/transformers"

class SentimentClient {
    constructor() {
        this.sentimentPipe = null;
    }

    async init() {
        this.sentimentPipe = await pipeline('sentiment-analysis');
    }

    async evaluate(input) {
        if (!this.sentimentPipe) {
            throw new Error('SentimentClient not initialized');
        } else {
            return await this.sentimentPipe(input);
        }
    }
}

export { SentimentClient };