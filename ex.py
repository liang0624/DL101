# -*- coding: utf-8 -*-


def str_filter(string):
    string = string.replace('，', ' ')
    string = string.replace('。', ' ')
    string = string.replace('“', ' ')
    string = string.replace('”', ' ')
    string = string.replace('?', ' ')
    string = string.replace('；', ' ')
    string = string.replace('：', ' ')
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
    string = string.replace('―', ' ')
    return string.replace('　', ' ')


def fun(file_name):
    # 读取文档内容
    with open(file_name) as file_link:
        file_content = file_link.read()

    # 去除标点符号按空格切割
    words_list = str_filter(file_content).split()

    # 统计二元词组
    words_dict = {}
    for i in range(0, len(words_list)-1):
        key = words_list[i] + " " + words_list[i+1]
        if key in words_dict:
            words_dict[key] += 1
        else:
            words_dict[key] = 1

    sorted_list = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:10]


result = fun('happiness_seg.txt')
for s in result:
    print "词组[%s]  %d 次" % (s[0], s[1])

# 词组[的 人]  930 次
# 词组[他 的]  503 次
# 词组[自己 的]  480 次
# 词组[上 的]  356 次
# 词组[他们 的]  335 次
# 词组[人 的]  293 次
# 词组[的 时候]  261 次
# 词组[就 会]  225 次
# 词组[的 东西]  207 次
# 词组[都 是]  206 次
