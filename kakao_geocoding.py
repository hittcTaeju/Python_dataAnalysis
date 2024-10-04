import json
import requests

api_key = "025a9daf28cfcd9cf53bfa78eb3418c8"

def addr_to_lat_lon(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query={address}'.format(address=addr)
    headers = {"Authorization": "KakaoAK " + api_key}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address']
    return float(match_first['x']), float(match_first['y'])
'''
tmp = addr_to_lat_lon("서울특별시 마포구 상암동 1709")
tmp2 = addr_to_lat_lon("서울특별시 마포구 연남동 482-21")
tmp3 = addr_to_lat_lon("서울특별시 마포구 연남동 260-65")

print(tmp2)
print(tmp3)
'''