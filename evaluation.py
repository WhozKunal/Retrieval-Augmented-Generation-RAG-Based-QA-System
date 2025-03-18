from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu

def evaluate(actual, generated):
    # ROUGE Score
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(actual, generated)

    # BLEU Score
    bleu_score = sentence_bleu([actual.split()], generated.split())

    return rouge_scores, bleu_score
