#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");

import os
import commands
import sys
from conf import conf


def up2hadoop(path, hadoop_dir):
    print ">>>up2hadoop", path, hadoop_dir
    local_path = os.path.abspath(path)
    local_path = path
    hadoop_path = os.path.join(hadoop_dir, os.path.split(path)[-1])
    if not hadoop_dir.endswith('/'):
        hadoop_dir = hadoop_dir + '/'
    cmd = "hadoop fs -mkdir {hadoop_dir}".format(hadoop_dir=hadoop_dir)
    os.system(cmd)
    cmd = "hadoop  fs -put {path} {hadoop_path}"
    cmd = cmd.format(path=path, hadoop_path=hadoop_path)
    print cmd
    s = os.system(cmd)

    def get_hadoop_file_size(path):
        hcmd = "hadoop fs -ls {path}".format(path=path)
        rst = commands.getoutput(hcmd)
        print rst
        size = rst.strip().split('\n')[-1].split()[4]
        print path, ":", size
        return int(size)

    if get_hadoop_file_size(hadoop_path) == os.stat(path).st_size:
        os.remove(path)
        print ">>> remove", path
        return cmd
    else:
        raise


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    ptime = sys.argv[2]
    hadoop_dir = conf['hadoop_dir'] .format(year=ptime[:4],
                                            month=ptime[4:6],
                                            day=ptime[6:8],
                                            hour=ptime[8:10])
    up2hadoop(path, hadoop_dir)
