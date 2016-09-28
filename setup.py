from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='CloudExchange Plugin'

    version='0.1',
    author='jmadtha',
    author_email='jmadtha@vmware.com',
    description='ENTER-DESCRIPTION-HERE',

    # This must correspond to the actual packages in the plugin.
    packages=['cloudify_plugin'],

    install_requires=[
        "cloudify-plugins-common==3.1"
    ]
)