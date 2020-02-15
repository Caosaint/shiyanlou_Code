"""Factorial project"""
from setuptools import find_packages, setup

setup(name = 'my_first_project',  # 注意这里的name不要使用factorial相关的名字，易重复
    version = '0.1',
    description = "Factorial module.",
    long_description = "A test module for our book.",
    platforms = ["Linux"],
    author="Bracy",
    author_email="736340716@qq.com",
    url="https://www.shiyanlou.com/courses/596",
    license = "MIT",
    packages=find_packages()
    )
