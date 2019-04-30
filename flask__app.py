from flask import Flask, request
import logging
import json
# ����������� ������� �� ������ ������� ����� geo
from translator import translate_word
 
app = Flask(__name__)
 
# ��������� ����������� � ����. ����� ����� ����, 
# ��������� �� pythonwhere � ������ files, �� ����� � �������� �����
logging.basicConfig(level=logging.INFO, filename='app.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
 
 
@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Request: %r', response)
    return json.dumps(response)
 
 
def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = \
            '������! � ���� ���������� �����!'
        return
    
    text = req['request']['original_utterance'].lower()
    word = text.split()
    word = word[-1]
    
    if '��������' in text:
        res['response']['text'] = translate_word(word)
    else:
        res['response']['text'] = '�� �������!'
 
 
if __name__ == '__main__':
    app.run()