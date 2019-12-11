#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_k8s.py
# @Author: Wade Cheung
# @Date  : 2019/12/12
# @Desc  : k8s的configmap, secret 创建和更新


from os import path

import yaml
from kubernetes import client, config

CONFIGMAP_NAME = 'config-test'
SECRET_NAME = 'secret-test'


class K8s:
    def __init__(self):
        config.load_kube_config()

    def create_configmap(self):
        with open(path.join(path.dirname(__file__), "test_configmap.yaml")) as f:
            dep = yaml.safe_load(f)
            resp = client.CoreV1Api().create_namespaced_config_map(body=dep, namespace="default")
            print(resp)

    def update_configmap(self, configmap_dict):
        config_map = client.V1ConfigMap(
            api_version="v1",
            kind="ConfigMap",
            metadata=client.V1ObjectMeta(name=CONFIGMAP_NAME, namespace='default'))
        config_map.data = configmap_dict

        api_response = client.CoreV1Api().patch_namespaced_config_map(
            name=CONFIGMAP_NAME,
            namespace="default",
            body=config_map)
        print(api_response.data)

    def create_secret(self):
        with open(path.join(path.dirname(__file__), "test_secret.yaml")) as f:
            dep = yaml.safe_load(f)
            resp = client.CoreV1Api().create_namespaced_secret(body=dep, namespace="default")
            print(resp)

    def update_secret(self, secret_dict):
        secret = client.V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=client.V1ObjectMeta(name=SECRET_NAME, namespace='default'))
        secret.data = secret_dict

        api_response = client.CoreV1Api().patch_namespaced_secret(
            name=SECRET_NAME,
            namespace="default",
            body=secret)
        print(api_response.data)
