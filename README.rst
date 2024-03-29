========
Motswadi
========

Parent education involvement through mobile messaging.

Getting Started
===============

Create and install environment packages by executing the following commands::

    $ virtualenv --no-site-packages ve
    $ . ve/bin/activate
    $ pip install -r requirements.pip


Starting Vumi App
=================

Start the Vumi transport worker manually by executing the following command::

    $ twistd -n --pidfile=transportworker.pid start_worker --worker-class=vumi.transports.xmpp.XMPPTransport --config=./motswadi/transport.yaml

Start the Vumi application worker by executing the following command::

    $ twistd -n --pidfile=applicationworker.pid start_worker --worker-class=motswadi.application.MotswadiApplicationWorker --config=./motswadi/worker.yaml

Deploying
=========

Remote Host Fabric Deploy
-------------------------

Provision
+++++++++
To provision a new Motswadi instance on a remote host run the following command using a user with superuser privileges on the remote host:: 
    
    $ fab -H hostname:port -u user provision

After the provision access Motswadi by hitting the hostname in your browser.

Release
+++++++
To release new Motswadi code on an existing instance run the following command using a user with superuser privileges on the remote host:: 
    
    $ fab -H hostname:port -u user release

This will pull the latest code from the ``master`` branch and restart the instance.

Restart
+++++++
To restart a remote Motswadi instance previously provisioned run the following command using a user with superuser privileges on the remote host:: 
    
    $ fab -H hostname:port -u user restart

This will restart `Nginx <http://wiki.nginx.org/Main>`_ and reload `Supervisor <http://supervisord.org/>`_, thus restarting Motswadi.

Local Vagrant Deploy
--------------------
Deploy a local Vagrant instance like so::
    
    you@host$ git clone https://github.com/praekelt/motswadi.git
    you@host$ cd motswadi
    you@host$ vagrant up
    you@host$ vagrant ssh
    vagrant@lucid32$ sudo -i
    vagrant@lucid32$ su ubuntu
    ubuntu@lucid32$ cd /var/praekelt/motswadi
    ubuntu@lucid32$ . ve/bin/activate
    (ve)ubuntu@lucid32$ ./motswadi/manage.py syncdb
    (ve)ubuntu@lucid32$ ./motswadi/manage.py migrate
    (ve)ubuntu@lucid32$ ./motswadi/manage.py collectstatic
    (ve)ubuntu@lucid32$ exit
    root@lucid32$ /etc/init.d/nginx restart
    root@lucid32$ supervisorctl reload

Then access the Motswadi dashboard on `localhost port 4567 <http://localhost:4567>`_.

