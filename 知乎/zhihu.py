import requests
import execjs
import urllib.parse



def main(input):
    encoded_input = urllib.parse.quote(input, encoding='utf-8')
    code = f'101_3_3.0+/api/v4/search_v3?gk_version=gz-gaokao&t=general&q={encoded_input}&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal+AYBR8KXGyhiPTm9j4SqSdUMMaFafpM6xKn0=|1718704925'
    zse_96 = execjs.compile(open('zse_96补环境.js', encoding="utf-8").read()).call("get_zse_96", code)
    print('zse_96:', zse_96)
    print('zse_96的长度:', len(zse_96))

    # 防止滥用，发包逻辑已删除


if __name__ == '__main__':
    # 搜索的关键字
    main('python')