"""Webアプリケーション

外部APIモード:
  環境変数 CHAT_API_URL を設定すると、チャットリクエストを外部APIに転送します。
  例: CHAT_API_URL=http://localhost:8081/api/chat python app.py

従来モード:
  環境変数未設定の場合、Gemini APIを直接使用します。
"""
from flask import Flask, render_template, request, jsonify
import os
import settings

app = Flask(__name__)

# 外部APIモード判定
EXTERNAL_CHAT_API = os.getenv('CHAT_API_URL')

# 従来モード: Gemini直接（外部API未設定時のみ初期化）
chat = None
if not EXTERNAL_CHAT_API:
    import google.generativeai as genai
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel(
        model_name=settings.MODEL_NAME,
        system_instruction=settings.SYSTEM_INSTRUCTION
    )
    chat = model.start_chat()


@app.route('/')
def index():
    """メインページ表示"""
    config = {
        'typewriter_delay': settings.TYPEWRITER_DELAY_MS,
        'avatar_name': settings.AVATAR_NAME,
        'avatar_full_name': settings.AVATAR_FULL_NAME,
        'mouth_animation_interval': settings.MOUTH_ANIMATION_INTERVAL_MS,
        'beep_frequency': settings.BEEP_FREQUENCY_HZ,
        'beep_duration': settings.BEEP_DURATION_MS,
        'beep_volume': settings.BEEP_VOLUME,
        'beep_volume_end': settings.BEEP_VOLUME_END,
        'avatar_image_idle': settings.AVATAR_IMAGE_IDLE,
        'avatar_image_talk': settings.AVATAR_IMAGE_TALK
    }
    return render_template('index.html', config=config)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """ユーザー入力を受信しAI応答を返す
    
    外部APIモード: CHAT_API_URL に転送
    従来モード: Gemini APIを直接使用
    """
    message = request.json['message']
    
    if EXTERNAL_CHAT_API:
        # 外部APIに転送
        import requests
        try:
            resp = requests.post(
                EXTERNAL_CHAT_API,
                json={'message': message},
                timeout=60  # LLM応答を待つため長めに設定
            )
            resp.raise_for_status()
            return jsonify(resp.json())
        except requests.exceptions.Timeout:
            return jsonify({'response': 'エラー: 応答がタイムアウトしました'}), 504
        except requests.exceptions.ConnectionError:
            return jsonify({'response': 'エラー: 外部APIに接続できません'}), 503
        except Exception as e:
            return jsonify({'response': f'エラー: {e}'}), 500
    else:
        # 従来モード: Gemini直接
        response = chat.send_message(message)
        return jsonify({'response': response.text})


if __name__ == '__main__':
    # 起動モード表示
    if EXTERNAL_CHAT_API:
        print(f"🔗 External API Mode")
        print(f"   → Forwarding to: {EXTERNAL_CHAT_API}")
    else:
        print(f"🤖 Gemini Direct Mode")
        print(f"   → Model: {settings.MODEL_NAME}")
    
    print(f"🌐 Starting server on port {settings.SERVER_PORT}...")
    app.run(debug=settings.DEBUG_MODE, port=settings.SERVER_PORT)
