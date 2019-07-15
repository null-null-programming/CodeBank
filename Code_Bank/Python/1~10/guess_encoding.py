# バイト型の文字列を受けとりエンコードを判定する。


def guess_encoding(s):
    encodings = ["ascii", "utf-8", "shift-jis", "euc-jp"]
    for enc in encodings:
        try:
            s.decode(enc)
        except UnicodeDecodeError:
            continue
        else:
            return enc
    else:
        return ""  # 成功したエンコードがない場合は空文字列を返す。
