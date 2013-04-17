import os
import sys
DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(DIR_PATH, 'hivepy'))
from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from conf import conf

def execsql(sql):
    try:
        transport = TSocket.TSocket(conf['hive']['host'], conf['hive']['port'])
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        client = ThriftHive.Client(protocol)
        transport.open()
        print "hive connect"

        client.execute(sql)
        print client.fetchAll()

        transport.close()
        print "close hive connect"
        return True

    except Thrift.TException, tx:
        print '%s' % (tx.message) 
        return False

if __name__ == "__main__":
    import sys
    import os
    import re
    import datetime
    hour=sys.argv[1]
    hadoop_path=sys.argv[2]
    hadoop_path = os.path.join(os.path.split(hadoop_path)[0],'*')
    datetime.datetime.strptime(hour,'%Y%m%d%H') 
    print hadoop_path
    sql = "load data inpath '{hadoop_path}' into table diaodulog_v0_paritioned PARTITION (day='{day}',hour='{hour}')"
    sql = sql.format(hadoop_path=hadoop_path,day=hour[:8],hour=hour)
    print sql
    execsql(sql)
