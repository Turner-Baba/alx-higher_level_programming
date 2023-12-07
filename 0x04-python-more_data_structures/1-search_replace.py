#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nwlist = list(map(lambda itm: replace if itm == search else itm, my_list))
    return (nwlist)
