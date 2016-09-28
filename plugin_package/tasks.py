from cloudify.decorators import operation

@operation 
def write_to_file(**kwargs):

def write_to_file(**kwargs):
    with open('/tmp/cloudify-plugin', 'w') as f:
        f.write('This simple example gives you '
                'the power to do amazing things.')