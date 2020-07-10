# config files
squid_users
env file

# ansible run

ansible servers -i hosts -m ping

ansible-playbook  -i hosts init.yml


# pgadmin req

sudo chown -R 5050:5050 /data/pgadmin