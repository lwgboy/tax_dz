# -*- coding:utf-8 -*-
from distutils.core import setup
import py2exe


#setup(console=['inv_import.py'
#				]
#			)

setup(windows=[{"script":"inv_import.py",
                "icon_resources":[(1, "auth.ico")]}]
)

#setup(name='Game EndPointService',
#			version='1.0',
#			description='Game Distribution Por',
#			author='scott',
#			author_email='zhangbin@5173.com',
#			url='',
#			#packages=['distutils', 'distutils.command'],
#			py_modules=['endpoint']
#			
#			)
