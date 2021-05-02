exercicio de docker com 2 container
1 - mysql 5.7 
2 - flask web

  docker pull mysql:5.7
  docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=mudar123 -p 3307:3307 -d mysql:5.7
  docker ps
  docker network inspect bridge
  mysql -uroot -p --host=172.17.0.7

 docker image build -t python-web .
 docker run -p 5001:5000 -d python-web

