import os
import json
import pandas as pd


filenames = os .listdir('extra_data/')

headers = list()
for filename in filenames:
    f = open('extra_data/' + filename)
    data = json.load(f)
    f.close()
    headers.extend(list(data.keys()))
    headers = list(set(headers))


df_dict = dict()
df_dict['account'] = list()
for header in headers:
    df_dict[header] = list()

for filename in filenames:
    f = open('extra_data/' + filename)
    data = json.load(f)
    f.close()
    for header in headers:
        if header in data.keys():
            df_dict[header].append(data[header])
        else:
            df_dict[header].append(0)
    df_dict['account'].append(filename.replace(".json", ""))


# for header in headers:
#     print(header, len(df_dict[header]))
df = pd.DataFrame(data=df_dict)
df.to_csv("extra_data.csv", index=0)

action_names = list()
for filename in filenames:
    f = open('data/' + filename)
    data = json.load(f)
    action_stat = data['action_stat']
    f.close()
    # print(data)
    action_names.extend(list(action_stat.keys()))
    action_names = list(set(list(action_names)))

df_dict2 = dict()
for action_name in action_names:
    df_dict2[action_name] = list()
df_dict2['account'] = list()

for filename in filenames:
    f = open('data/' + filename)
    data = json.load(f)
    data = data['action_stat']
    f.close()
    for action_name in action_names:
        if action_name in data.keys():
            df_dict2[action_name].append(data[action_name])
        else:
            df_dict2[action_name].append(0)
    df_dict2['account'].append(filename.replace(".json", ""))

df2 = pd.DataFrame(data=df_dict2)
df2.to_csv('data.csv',index=0)