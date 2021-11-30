from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

#Создаем запрос на корневой адрес, используем метод POST
@app.route('/', methods=["POST"])
def start():
    logging.info(request.json)
    spisok_citat_1_vopros = ["Очевидно, что ничего не очевидно!", "Здорово, бандиты!", "Где деньги, Лебовски?"]
    citata_velikih = ["Счастье - это не обладание тем, чего желаешь, а желание того, чем обладаешь.", "Чудеса - там, где в них верят, и чем больше верят, тем чаще они случаются.", "Веди себя так, будто ты уже счастлив, и ты действительно станешь счастливее."]
    bye = ["Уже уходите? Очень жаль.", "До скорой встречи", "Буду с нетерпением вас ожидать вновь"]
    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False

        }
    }

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Какую цитату тебе вывести?"
    else:
        if req["request"]["original_utterance"].capitalize() in ["Для важных переговоров"]:
            response["response"]["text"] = random.choice(spisok_citat_1_vopros)
        elif req["request"]["original_utterance"].capitalize() in ["Цитата великих"]:
            response["response"]["text"] = random.choice(citata_velikih)
        elif req["request"]["original_utterance"].capitalize() in ["Спасибо", "Пока", "Увидимся"]:
            response["response"]["text"] = random.choice(bye)
            response["response"]["end_session"] = True

    return json.dumps(response)

# if __name__ == '__main__':
#     app.run()
