# URL SHORTERNER
Tested on:
- Description: Ubuntu 22.04.2 LTS
- Release: 22.04
- Codename: jammy
- Python: 3.10.6
- pip: 22.1.2 
- env: (GNU coreutils) 8.32

Instructions:
1. Clone the repository
2. ```cd venv && source venv/bin/activate```
3. ```python3 url.py```
4. On Postman:
- set METHOD to POST
- set the url to ```http://localhost:5000```
- set key to ```url```
- set value to <any_url>```http://www.youtube.com```
- send and generated link is stored inside url_map.txt
5. On Curl:
- ```curl -d "url=http://www.youtube.com" -X POST http://localhost:5000/```
6. On Docker:
- ```cd dockerized```
- ```docker build -t my-shortener-app .```
- ```docker run -p 5000:5000 my-shortener-app```
7. To test the service, run the bash script:
- make sure the service is up and running
- from ```venv``` folder, make the test file executable ```sudo chmod +x test.sh```
- then run ```./test.sh```

