# Copyright 2021 aditya
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



# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(

    name='ShortLinklib',
    version='0.1.0',
    description='Python library that act as a stand alone link shorten utility.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://aa-5.github.io/ShortLink',
    author='Aditya Ajay',
    author_email='adityaajay574@gmail.com',
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache License v2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'ShortLinklib'},  
    packages=find_packages(where='ShortLinklib'), 
    python_requires='>=3.6, <4',
    install_requires=['validators'],

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/aa-5/ShortLink/issues',
        'Source': 'https://github.com/aa-5/ShortLink',
    },
)