"""
設定管理モジュール - .envファイルから全設定を読み込み

外部APIモード:
  CHAT_API_URL が設定されている場合、GEMINI_API_KEY/MODEL_NAME は不要です。
"""
import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# ===========================================
# 外部APIモード判定
# ===========================================
EXTERNAL_API_MODE = bool(os.getenv('CHAT_API_URL'))

# ===========================================
# AI設定（外部APIモードでは任意）
# ===========================================
if EXTERNAL_API_MODE:
    # 外部APIモード: Gemini設定は不要
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    MODEL_NAME = os.getenv('MODEL_NAME', '')
else:
    # 従来モード: Gemini設定は必須
    GEMINI_API_KEY = os.environ['GEMINI_API_KEY']
    MODEL_NAME = os.environ['MODEL_NAME']

# ===========================================
# 任意設定（デフォルト値あり）
# ===========================================

# アバター設定
AVATAR_NAME = os.getenv('AVATAR_NAME', 'Spectra')
AVATAR_FULL_NAME = os.getenv('AVATAR_FULL_NAME', 'Spectra Communicator')
AVATAR_IMAGE_IDLE = os.getenv('AVATAR_IMAGE_IDLE', 'idle.png')
AVATAR_IMAGE_TALK = os.getenv('AVATAR_IMAGE_TALK', 'talk.png')

# AI性格設定（AVATAR_NAMEに依存）
SYSTEM_INSTRUCTION = os.getenv(
    'SYSTEM_INSTRUCTION',
    f'あなたは{AVATAR_NAME}というAIアシスタントです。技術的で直接的なスタイルで簡潔に応答してください。回答は短く要点を押さえたものにしてください。'
)

# サーバー設定
SERVER_PORT = int(os.getenv('SERVER_PORT', '5000'))
DEBUG_MODE = os.getenv('DEBUG_MODE', 'True').lower() == 'true'

# UI設定
TYPEWRITER_DELAY_MS = int(os.getenv('TYPEWRITER_DELAY_MS', '50'))
MOUTH_ANIMATION_INTERVAL_MS = int(os.getenv('MOUTH_ANIMATION_INTERVAL_MS', '150'))

# サウンド設定
BEEP_FREQUENCY_HZ = int(os.getenv('BEEP_FREQUENCY_HZ', '800'))
BEEP_DURATION_MS = int(os.getenv('BEEP_DURATION_MS', '50'))
BEEP_VOLUME = float(os.getenv('BEEP_VOLUME', '0.05'))
BEEP_VOLUME_END = float(os.getenv('BEEP_VOLUME_END', '0.01'))
