from fabric.api import run, env, put
from fabric.decorators import parallel

env.use_ssh_config = True
env.disable_known_hosts = True
#env.hosts = ['10.0.1.11','10.0.1.12','10.0.1.13','10.0.1.14'.'10.0.1.15']
env.hosts = ['54.64.229.107']
env.user = 'ec2-user'
env.key_filename = '~/.ssh/moritata.pem'

def jmeter_chown():
    run('chmod a+x /home/ubuntu/apache-jmeter-2.11/bin/jmeter')

def jmeter_properties():
    run('sed -i s/^#server.rmi.localport/server.rmi.localport=4000/ /home/ubuntu/apache-jmeter-2.11/bin/jmeter.properties')

@parallel
def jmeter_server():
    run('/home/ubuntu/apache-jmeter-2.11/bin/jmeter-server')

def upload():
    put('config','/home/ec2-user/config')

def deploy_jmx():
    put('jmx/*.jmx','/home/ubunt-user/deploy_jmx')

