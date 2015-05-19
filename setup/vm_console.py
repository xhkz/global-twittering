#!/usr/bin/env python
"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""
__requires__ = 'boto==2.34.0'
import argparse
import time

from boto.ec2.connection import EC2Connection
from boto.ec2.regioninfo import RegionInfo

EC2_ACCESS_KEY = '38aa6ac0953443f5831398a4cc8757a0'
EC2_SECRET_KEY = 'c1385348cf7e4b01b82601c2c2f7d61f'
DEFAULT_IMAGE_ID = 'ami-000022b3'
DEFAULT_KEY_PAIR = 'xhuang'
DEFAULT_PLACE = 'melbourne-np'

conn = EC2Connection(aws_access_key_id=EC2_ACCESS_KEY,
                     aws_secret_access_key=EC2_SECRET_KEY,
                     is_secure=True,
                     region=RegionInfo(name="NeCTAR", endpoint="nova.rc.nectar.org.au"),
                     validate_certs=False,
                     port=8773,
                     path="/services/Cloud")


def create_instances(count=1):
    # ami-000022b3 NeCTAR Ubuntu 14.04 (Trusty) amd64
    instance_list = []
    for c in range(count):
        instance_list.append(
            conn.run_instances(DEFAULT_IMAGE_ID,
                               key_name=DEFAULT_KEY_PAIR,
                               instance_type='m1.small',
                               security_groups=['default'],
                               placement=DEFAULT_PLACE)
        )

    return map(lambda x: x.instances[0], instance_list)


def get_all_instance_ids():
    return map(lambda x: x.instances[0].id, conn.get_all_instances())


def get_instance(instance_id):
    return conn.get_all_instances(instance_id)[0].instances[0]


def check_status(instance_id):
    print 'checking status of [%s]...' % instance_id
    return get_instance(instance_id).state


def wait_status(instance_id, status, max_loop=20):
    loop = 0

    while loop < max_loop:
        time.sleep(15)
        if check_status(instance_id) == status:
            return True
        loop += 1

    return False


def terminate_instance(instance_id):
    return get_instance(instance_id).terminate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=1, help='instance count')
    parser.add_argument('-o', type=str, help='start or terminate')
    args = parser.parse_args()

    if not args.o:
        parser.print_help()
        exit(1)

    if args.o.lower() == 'start':
        for ins in create_instances(args.n):
            if wait_status(ins.id, 'running'):
                instance = get_instance(ins.id)
                print instance.id, instance.ip_address, instance.state
            else:
                print 'create %s failed.' % ins.id
    elif args.o.lower() == 'terminate':
        # Terminating all instances
        for ins_id in get_all_instance_ids():
            terminate_instance(ins_id)
    else:
        parser.print_help()
