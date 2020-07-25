# gitlab-runner setup for deploy
if you want to deploy your code with a runner, you must install a runner on the host, and set it up with shell executer

after that add this to sudo visudo


gitlab-runner ALL=(ALL) NOPASSWD: /usr/local/bin/docker-compose,/usr/bin/docker


then

sudo su gitlab-runner

sudo docker login registry.gitlab.com