# import requests
# import os
# import numpy as np
'''
get actions summary by account name
'''
import bos_data_apis as api
from tqdm import tqdm
import deal_with_actions as actions_parser
import json

accounts = list()
f = open("account_list.txt")
for line in f.readlines():
    line = line.replace("\n", "")
    accounts.append(line)
f.close()

for account in tqdm(accounts[0:1000]):
    try:
        actions = api.get_action(account, -1, -50)
        print(len(actions))
        f, action_stat, time_dist_seq, time_seq, n = actions_parser.extract_feature_from_actions(actions)
        if f:
            data = {
                "action_stat": action_stat,
                "time_seq": time_seq,
                "time_dist_seq": time_dist_seq,
                "n": n
            }

            fp = open("data/" + account + ".json", "w")
            json.dump(data, fp)
            fp.close()

    except Exception as e:
        print(str(e))

    # action_types = api.get_action_types(account)
    # account_tokens = api.get_tokens(account)
    # account_permission = api.get_permission(account)
    # print(action,action_types,account_permission,account_tokens)

# account = sub_list[0]
# actions = api.get_action(account, -1, -50)
# n = len(actions)
#
# action_types = api.get_action_types(account)
# account_tokens = api.get_tokens(account)
# account_permission = api.get_permission(account)



    # print(unixtime)
    # print(type(unixtime))
