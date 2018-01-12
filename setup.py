import setuptools


setuptools.setup(
    name='boids',
    version='0.0.1',
    long_description='',
    author='David Buckley',
    url='https://github.com/buckley-w-david/boids',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: David Buckley',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    entry_points='''
        [console_scripts]
        boids=boids.cli:cli
    '''
)
