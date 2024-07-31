from setuptools import setup, find_packages

setup(
    name='huffman-zip',
    version='0.1',
    packages=find_packages(),
    py_modules=['huffman_compressor', 'cli'],
    install_requires=[
"bitarray==2.9.2",
"bitstring==4.2.3",
"setuptools==72.1.0"
    ],
    entry_points={
        'console_scripts': [
            'huffman-zip=cli:main',
        ],
    },
    author='Monica Smith',
    description='A Huffman compression text file zipper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/huffman-zip',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
