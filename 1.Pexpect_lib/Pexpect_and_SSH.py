from pexpect import pxssh

child = pxssh.pxssh()
child.login('172.16.1.20', 'cisco', 'cisco', auto_prompt_reset=False)
child.sendline('show version | i V')
child.expect('iosv-1#')
child.before
child.logout()