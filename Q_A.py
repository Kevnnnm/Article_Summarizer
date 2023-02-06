from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import yake

#takes in question to be answered by article in form
# QA_input = {
#       'question': 'How do I use this function?',
#       'context': article
# }
def get_answer_transformer(QA_input):
    model_name = "deepset/roberta-base-squad2"

    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    res = nlp(QA_input)
    # print(res)
    return res


def fetch_keywords(context, max_ngram_size=1, deduplication_threshold=0.1,
                   numOfKeywords=5, language="en"):
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(context)
    print(keywords)
    keywords = ' , '.join([key for key, score in keywords])
    return keywords