import re

def analyze_match(cv_text, job_text):

    job_words = set(
        re.findall(r"\w+", job_text.lower())
    )

    cv_words = set(
        re.findall(r"\w+", cv_text.lower())
    )

    matched = list(cv_words.intersection(job_words))

    score = int(
        (len(matched) / len(job_words)) * 100
    )

    return {
        "score": score,
        "matched_keywords": matched[:20]
    }