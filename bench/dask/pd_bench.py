#!/usr/bin/env python

import dask.dataframe as dd
df = dd.read_csv('../../../data.csv')
df.mean().compute()
