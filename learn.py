# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:14:58 2021

@author: a
"""


for_table = this_product.copy()
                for_table['PartitionKey'] = p_key
                for_table['RowKey'] = '{}-{}'.format(item_numer, str(datetime.datetime.now()))
                for_table['ItemNumber'] = item_numer

                table_service.insert_or_replace_entity(table_insertion, for_table)

                print(this_product)




def get_and_insert(asin, account_n, table_prefix, path_to_file, title='', brand='', model='', ):
    partition_key = '{}'.format(account_n)
    already_in = TABLE_SERVICE.query_entities('{}{}'.format(table_prefix, PRODUCT_CATALOG_TABLE),
                                              filter="RowKey eq '{}'".format(asin),
                                              select='RowKey')