import time
import dateutil.parser


def extract_feature_from_actions(actions):
    actions = actions['actions']
    n = len(actions)
    if n == 0 or n == 1:
        return False, None, None, None, None
    action_stat = dict()
    time_seq = list()
    for action in actions:
        time_str = action['block_time']
        unix_timestamp = time.mktime(dateutil.parser.parse(time_str).timetuple())
        time_seq.append(unix_timestamp)
        act = action['action_trace']['act']
        # print(act)
        action_account = act['account']
        action_name = act['name']
        key = action_account + "_" + action_name
        if key in action_stat.keys():
            action_stat[key] += 1
        else:
            action_stat[key] = 1

    time_dist_seq = list()
    for i in range(0, len(time_seq)-1, 1):
        time_dist_seq.append(time_seq[i+1]-time_seq[i])
    return True, action_stat, time_dist_seq, time_seq, n

