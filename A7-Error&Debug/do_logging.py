#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用logging进行调试
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
