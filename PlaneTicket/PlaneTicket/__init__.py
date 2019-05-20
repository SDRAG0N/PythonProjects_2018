# 在项目的init文件中编写下列代码：
# 这样整个项目都能使用pymysql，就不用再每个文件都导入pymyqsl

import pymysql
pymysql.install_as_MySQLdb()
