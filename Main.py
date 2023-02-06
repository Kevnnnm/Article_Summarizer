import Extract_Text

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import textwrap
import nltk
nltk.download('punkt')

#git pull
#git push -u origin master
#just use menu bar commands

def summarize_text(context, n_sentences = 10):
    parser = PlaintextParser.from_string(context, Tokenizer('english'))

    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count = n_sentences)

    # for sentence in summary:
    #     print(sentence)

    return summary

def main(pdf):
    summary_text = '*' * 160 + '\n\n'
    text = Extract_Text.pdf_main(pdf)
    summarized_article = summarize_text(text)
    for sentence in summarized_article: #creates summary as a string
        sentence = textwrap.fill(str(sentence).replace('\\n', '').replace('.', '.\n'), 160)
        summary_text += sentence
        summary_text+= '\n\n'
    #print(summary_text)
    return summary_text


print(main('https://www.nature.com/articles/453028a.pdf'))