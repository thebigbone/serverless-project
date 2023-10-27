import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    text = req.params.get('text')
    specific_words = req.params.get('specific_words')

    if text and specific_words:
        words = text.lower().split()
        specific_words = specific_words.split(',')

        word_count = {word: words.count(word) for word in specific_words}
        return func.HttpResponse(body=str(word_count), mimetype="application/json")
    else:
        return func.HttpResponse("Invalid input. Please provide 'text' and 'specific_words' parameters in the URL.", status_code=400)
