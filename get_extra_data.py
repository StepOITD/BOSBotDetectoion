import os
import bos_data_apis as api
from tqdm import tqdm
import json
accounts = os.listdir("data/")

for account in tqdm(accounts):
    try:
        data = dict()
        account = account.replace(".json", "")
        action_types = api.get_action_types(account)
        for action_type in action_types['data']['types']:
            data[action_type] = 1

        # print("=======================")
        account_tokens = api.get_tokens(account)
        # print(account_tokens)
        for budget in account_tokens['data']['tokens']:
            data[budget['exec_account'] + "_" + budget['symbol']] = float(budget['balance'])

        # print("=======================")
        account_permission = api.get_permission(account)
        for permission in account_permission['data']['permissions']:
            data[permission['name'] + "_" + permission['parent']] = permission['threshold']

        f = open("extra_data/"+account+".json", 'w')
        json.dump(data, f)
        f.close()

    except Exception as e:
        print(str(e))
