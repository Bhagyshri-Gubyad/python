# python
#first build cusstom image using  docker
 docker build -f pydkf -t pyimg .
 # create and run container 
 docker run -d -n pythoncontainer -p80:80 pyimg
 # see the running container 
 docker ps
