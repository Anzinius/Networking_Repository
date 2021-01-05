import pexpect

host = '172.16.1.0'
name = 'user'
password = '****'

def ssh(host):
    return 'ssh %s@%s' % (name, host)

def wait_password(host):
    return '%s@%s\'s password :' % (name, host)

child = pexpect.spawn(ssh(host))
child.setwinsize(400,400)
child.expect(wait_password(host))
child.sendline(password)
child.interact()
child.close()
