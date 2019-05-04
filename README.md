# Dockerize ML Model

A more updated app with simple ui is on simple-ui branch 

Hosted image:
http://ec2-54-154-230-55.eu-west-1.compute.amazonaws.com:8080/

.tar file:
https://drive.google.com/open?id=1GecOt-fEgKeY6lBPplPm50wWpgfKoYlZ

How to build and run the image
```
docker build -t pred_app:latest .
docker run -d -p 8080:8080 pred_app
```
```
docker ps
docker stop <CONTAINER_ID>
```
```
docker ps -a
docker logs XXX
```
```
docker rm $(docker ps -a -q)
```

Kill and remove running container
```
docker rm <containerid> -f
```

### Testing
"/pred_well"
{
    "Liquid_x": "6275",
    "Water_x": "1632",
    "DaysOn_x": "0",
    "Liquid_y": "5105",
    "Water_y": "2070",
    "DaysOn_y": "0",
    "Liquid": "5260",
    "Water": "744",
    "DaysOn": "0",
    "LATERAL_LENGTH_BLEND": "0.0"
}	

"/pred_well_arr"
{
    "API":["42177330040000", "33053037420000"],
    "Liquid_x": ["8186","39363"],
    "Water_x": ["11917","5082"],
    "DaysOn_x": ["0","30"],
    "Liquid_y": ["7593","25359"],
    "Water_y": ["11054","3028"],
    "DaysOn_y": ["0","31"],
    "Liquid": ["5573","18911"],
    "Water": ["8113","1791"],
    "DaysOn": ["0","25"],
    "LATERAL_LENGTH_BLEND": ["0.0", "0.0"]
}	

### Useful links 
https://iasaglobal.org/debugging-a-container-that-wont-start/
https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481