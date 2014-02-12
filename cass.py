from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

pool = ConnectionPool('TestSpace')

cf = ColumnFamily(pool, 'ColumnFamily1')

for i in range(1, 10):
   cf.insert(str(i), {str(i + i) : 'test'})

result = cf.multiget('1')

for col in result:
   print row['key']

print cf.get_count('row_key')
