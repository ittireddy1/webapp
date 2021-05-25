#!/usr/local/bin/python3
import argparse
import os
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from snowpy import TableApi, datacenter, glide, oob

class QueryManager:
    def __init__(self):
        self.hi = TableApi('hiworker')
        self.dc = TableApi('datacenter')
        self.dc.set_auth(backend_names='prompt,keyring', use_mfa=True)
        self.hi.set_auth(backend_names='prompt,keyring', use_mfa=True)

        self._query = None

    def get_cage(self, server):
        self._query = f"name={server}"
        pod_name = datacenter.Server.load_one(self.dc, self._query)

        print(pod_name.last_discovered.display_value)


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-s", "--server", help="Provide cage name to get details",type=str)



    args = parser.parse_args()
    name = args.server

    query_manager = QueryManager()
    query_manager.get_cage(name)

if __name__ == '__main__':
    main()
