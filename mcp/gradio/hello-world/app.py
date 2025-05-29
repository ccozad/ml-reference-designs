import gradio as gr

def letter_counter(word, letter):
    """Count the occurrences of a specific letter in a word.
    
    Args:
        word: The word or phrase to analyze
        letter: The letter to count occurrences of
        
    Returns:
        The number of times the letter appears in the word
    """
    return word.lower().count(letter.lower())

demo = gr.Interface(
    fn=letter_counter,
    inputs=["text", "text"],
    outputs="number",
    title="Letter Counter",
    description="Count how many times a letter appears in a word"
)

demo.launch(mcp_server=True)