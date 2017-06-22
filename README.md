# Technical Test 

In the following file shows the step by step how to deploy an application made in Flask using Ansible in an Ubuntu 14 server

## Getting Started

  1. install Ansible
  
```
 $ sudo apt-get install ansible 
 $ sudo apt-get update 
```

 2. generating key to access via ssh without a password
```
 $ cd ~/.ssh/
  $ ssh-keygen -t rsa -b 2048 -v     
  
  Enter file in which to save the key:ormuco
  Enter passphrase (empty for no passphrase):nothing, empty
  
  $ ssh-copy-id -i ormuco.pub root@your-ip-address
```
  3. Edit the host file on our computer
  
```
sudo nano /etc/ansible/hosts

output example
[webservers]
#alpha.example.org
#beta.example.org
*192.168.1.100
  add you ip
```
  4. clone repository ansibleFlask
  ```
  $ cd /home
  $ git clone https://github.com/andrescoulson/ansibleFlask.git
```

  5. edit file constant.yml 
```
 $ cd ansibleFlask
 $ nano constant.yml
 
 output example
  server_ip: 104.236.237.75
              replace you ip
 
```
  6. run ansible-playbook webserver.yml
```
 $ cd ansibleFlask
 $ ansible-playbook webserver.yml 
 
```
  7. test deploy
```
 http://your-ip
 
```

  
