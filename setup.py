# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

# python3.7 setup.py bdist_wheel

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

setup(
    name='reprod_log',
    version='1.0.0',
    install_requires=requirements,
    license='Apache License 2.0',
    keywords='reprod_log',
    description="TBD",
    url='https://github.com/WenmuZhou/reprod_log',
    author='wenmuzhou',
    author_email='wenmuzhou@gmail.com',
    packages=find_packages(), )
