from setuptools import setup

setup(name='watson_cognitive_facebook_bot',
      version='1.0',
      description='Watson cognitive Facebook bot',
      author='Ruslan Iakhin',
      author_email='ruslan.k.yakhin@gmail.com',
      url=None,
      packages=['watson_cognitive_facebook_bot'],
      install_requires=['speechrecognition', 'fbchat', 'watson_developer_cloud', 'pyaudio'],
      dependency_links=["https://github.com/yakhira/fbchat/archive/master.zip#egg=fbchat"]
     )
