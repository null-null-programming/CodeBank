# オブジェクト指向プログラミング
origi_str = "aabcbaa"
str_list = list(origi_str)
str_list.reverse()
print("".join(str_list) == origi_str)

# 関数型プログラミング
origi2_str = "aabcbaa"
print("".join(reversed(origi2_str)) == origi2_str)
