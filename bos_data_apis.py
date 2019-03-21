import requests
import json


def get_action(account: "str", pos: "int", offset: "int")-> 'dict':
    data = {
        "account_name": account,
        "pos": pos,
        "offset": offset,
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url="https://hapi.bos.eosrio.io/v1/history/get_actions", data=json.dumps(data), headers=headers)
    return json.loads(res.text)


def get_tokens(account: 'str')-> 'dict':
    url = "https://bos.eospark.com/api/account/" + account + "/tokens"
    res = requests.get(url)
    return json.loads(res.text)


def get_action_types(account: 'str')-> 'dict':
    url = "https://bos.eospark.com/api/account/" + account + "/actions/types"
    res = requests.get(url)
    return json.loads(res.text)


def get_permission(account: 'str')-> 'dict':
    url = "https://bos.eospark.com/api/account/" + account + "/permission"
    res = requests.get(url)
    # print(res.content)
    return json.loads(res.text)


# print(get_action("zyxsvncdavcs", -1, -50))
# print(get_tokens("zyxsvncdavcs"))
# print(get_permission("zyxsvncdavcs"))
