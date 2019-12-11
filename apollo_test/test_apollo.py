#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_apollo.py
# @Author: Wade Cheung
# @Date  : 2019/12/11
# @Desc  : 调用apollo client, create_secret, create_configmap, update_configmap


import time

from pyapollo import ApolloClient

from apollo_test.test_k8s import K8s

APP_ID = 'test123'
URL = 'http://127.0.0.1:30005'
CYCLE_TIME = 3


def apollo_client():
    client = ApolloClient(app_id=APP_ID, config_server_url=URL, cycle_time=CYCLE_TIME, timeout=300)
    client.start()
    notification_num = 10000000000000

    while True:
        num = client._notification_map['application']
        if notification_num != num:
            notification_num = num
            res = client.get_value('hahaha')
            print('-------res', res)
            k8s = K8s()
            k8s.update_configmap({'hahaha': res})

        time.sleep(CYCLE_TIME)


if __name__ == '__main__':
    # k8s = K8s()
    # k8s.create_secret()
    # k8s.create_configmap()

    apollo_client()
