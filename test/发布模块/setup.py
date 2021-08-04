from distutils.core import setup

setup(name="package_name",  # 包名
      version="1.0",  # 版本
      description="description",  # 描述信息
      long_description="Full description",  # 完整描述信息
      author="author",  # 作者
      author_email="1425868653@qq.com",  # 作者邮箱
      url="https://www.cnblogs.com/Jery-9527/",  # 主页
      py_modules=["TestMsg.sendmsg", "TestMsg.recvmsg"])

# python setup.py build  #执行这个命令进行构建
#python setup.py sdist 进行打包压缩


#-------------------------------------------
#打包后的使用
#把文件解压出来 然后在文件目录 执行 python setup.py install 包就会被安装到系统路径