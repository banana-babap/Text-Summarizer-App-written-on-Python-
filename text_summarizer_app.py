import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Function to summarize the text
def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    summarized_text = ' '.join(str(sentence) for sentence in summary)
    return summarized_text

# Streamlit App UI
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝")
st.title("📝 AI Text Summarizer")
st.subheader("Summarize long articles into a few sentences instantly!")

# Text input
input_text = st.text_area("Enter the text you want to summarize:", height=300)

# Sentence count slider
sentence_count = st.slider("How many sentences do you want in the summary?" , 1 , 10 , 3)

# Button to trigger summarization
if st.button("Summarize"):
    if input_text.strip() != "":
        summary = summarize_text(input_text, sentence_count)
        st.subheader("Summary:")
        st.success(summary)
    else:
        st.warning("Please enter some text to summarize!")

#Footer
st.markdown("---")
st.caption("Built with ❤️ using Python and AI")
