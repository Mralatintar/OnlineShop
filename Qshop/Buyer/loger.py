import logging                                                       #引入模块
logging_header=logging.FileHandler("test.log",encoding="utf-8")     #日志文件 文柄，指定文件名，指定文件编码方式，将日志信息输出到磁盘文件上。
stream_header=logging.StreamHandler()                               #能够将日志信息输出到sys.stdout, sys.stderr 或者类文件对象（更确切点，就是能够支持write()和flush()方法的对象）。

log_format="%(asctime)s【%(levelname)s】%(message)s"            #日志格式
time_formart="%Y-%m-%d %H:%M:%S"                                  #时间格式

logging.basicConfig(level=logging.DEBUG,format=log_format,datefmt=time_formart, #等级一下都要显示，格式为日志格式，时间格式，文柄
                    handlers=[logging_header,stream_header])
logging.debug("这是一个debug的information")                                         #输出到日志文件和控制台
logging.info("这是一个info的information")
logging.warning("这是一个warning的infomation")
logging.error("这是一个error的information")
logging.critical("这是一个critical的infomation")
