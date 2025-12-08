#!/bin/bash
# avatar-ui-core 起動スクリプト

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# 仮想環境チェック
if [ ! -d "venv" ]; then
    echo "❌ 仮想環境がありません。先に setup.sh を実行してください。"
    echo "   ./setup.sh"
    exit 1
fi

# 仮想環境有効化
source venv/bin/activate

# 起動
echo "🚀 avatar-ui-core を起動中..."
python app.py
