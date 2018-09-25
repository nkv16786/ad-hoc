import json
def linux_cpustats():
    '''
        linux specific implementation of cpustats
    '''
    ret = {}
    try:
        with open('/proc/stat', 'r') as fp_:
            stats = fp_.read()
    except IOError:
        pass
    else:
        for line in stats.splitlines():
            if not line:
                continue
            comps = line.split()
            if comps[0] == 'cpu':
                ret[comps[0]] = {'idle': comps[4],
                                 'iowait': comps[5],
                                 'irq': comps[6],
                                 'nice': comps[2],
                                 'softirq': comps[7],
                                 'steal': comps[8],
                                 'system': comps[3],
                                 'user': comps[1]}
    return {"output":ret['cpu'],"additional_attributes":ret['cpu']}
print linux_cpustats()
