import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/ros2SonyaBurg/Practice02/src/task02/install/task02'
