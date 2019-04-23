from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from bot import train_nlu, train_dialogue_embed, train_dialogue_keras
from testRasa import Load_model,get_res

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app, supports_credentials=True)

agent = Load_model()

@app.route('/', methods=['GET'])
def ping_pong():
    """
    测试
    :return:
    """
    return jsonify('Hello World!你好')  # （jsonify返回一个json格式的数据）


@app.route('/test', methods=['POST'])
def ping_pong2():
    """
    保存修改的意图信息
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]
        with open('Data/user_info.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            print("write json file success!")
    return "success"


@app.route('/testSlot', methods=['POST'])
def confirmSlot():
    """
    保存修改的词槽信息
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]
        with open('Data/slot_info.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            print("write json file success!")
        # for line in data:
        #     print(line)
    return "success"


@app.route('/getData', methods=['GET'])
def getdata():
    """
    获取意图信息
    :return:
    """
    data = {}
    with open("Data/user_info.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/getSlotData', methods=['GET'])
def getSlotdata():
    """
    获取词槽信息
    :return:
    """
    data = {}
    with open("Data/slot_info.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/upload', methods=['POST'])
def uploadDic():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save("Data/"+filename)
        print(file.filename)
    return "success"


@app.route('/upload_train', methods=['POST'])
def uploadTrain():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save("Data/training_"+filename)
        print(file.filename)
    return "success"


@app.route('/getActionData', methods=['GET'])
def getActionData():
    """
    获取行为配置
    :return:
    """
    data = {}
    with open("Data/action_info.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/testAction', methods=['POST'])
def confirmAction():
    """
    保存修改的行为信息
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]
        with open('Data/action_info.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            print("write json file success!")
        # for line in data:
        #     print(line)
    return "success"


@app.route('/saveStory', methods=['POST'])
def saveStory():
    """
    保存Story
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]
        print(data)
        with open('Data/story.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            print("write json file success!")
    return "success"

@app.route('/trainModel', methods=['POST'])
def trainModel():
    """
    训练模型
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]
        print(data)
        train_nlu()
        if data == "Embedding":
            train_dialogue_embed()
        else:
            train_dialogue_keras()
    return "success"

@app.route('/getReply', methods=['POST'])
def getReply():
    """
    获取答案
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()["data"]["data"]["text"]
        print(data)
        result = ""
        if data is not None:
            res = get_res(agent, data)
            if res != "":
                for i in range(len(res)):
                    result += res[i]['text']
            else:
                result = "不知道"
    return result


if __name__ == '__main__':
    app.run()
