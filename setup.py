from setuptools import setup, find_packages

setup(
    name='example_package',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='A short description of your package',
    long_description='A longer description of your package',
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/example_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.26.0',
        'flask>=2.0.2',
        'numpy>=1.21.5',
    ],
)
