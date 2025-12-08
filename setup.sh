#!/bin/bash
# avatar-ui-core 環境セットアップスクリプト

set -e

echo "=========================================="
echo "avatar-ui-core 環境セットアップ"
echo "=========================================="

# 仮想環境作成
if [ ! -d "venv" ]; then
    echo "📦 仮想環境を作成中..."
    python3 -m venv venv
    echo "✅ 仮想環境作成完了"
else
    echo "ℹ️  仮想環境は既に存在します"
fi

# 仮想環境有効化
echo "🔄 仮想環境を有効化..."
source venv/bin/activate

# パッケージインストール
echo "📥 パッケージをインストール中..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "✅ セットアップ完了！"
echo "=========================================="
echo ""
echo "起動方法:"
echo "  source venv/bin/activate"
echo "  python app.py"
echo ""
echo "または:"
echo "  ./run.sh"
echo ""
