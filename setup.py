from setuptools import setup

def _post_install() :
 pass

setup(
 name='shotio',
 version='0.1',
 description='FrameIO / Shotgun API Integration by Boxel Studio',
 author='Dexter Scott Belmont',
 author_email='xedret@gmail.com',
 py_modules=['shotio'],
 package_dir={'':'src'},
 install_requires=[
  'shotgun_api3', ''
 ],
 classifiers=[
  'Development Status :: 3 - Alpha',
  'Programming Language :: Python :: 3.9',
  'Natural Language :: English',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Operating System :: Operating System :: OS Independent',
  'Programming Language :: Python',
  'Programming Language :: Python :: 2',
  'Programming Language :: Python :: 3',
  'Topic :: Multimedia',
  'Topic :: Utilities',
]
)

_post_install()