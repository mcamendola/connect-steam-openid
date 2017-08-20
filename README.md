# connect-steam-openid
Sample python web application using flask-openid to integrate with Steam OpenID Provider.

## Dependencies

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Running

To run the application you need to create a file called **settings.cfg**, based on [settings.cfg_default](/web-app/src/settings.cfg_default) in the root of the directory [/web-app/src](/web-app/src).

You can create this file running the following command:

```bash
sudo cp web-app/src/settings.cfg_default web-app/src/settings.cfg 
```

After that open the file **settings.cfg** and edit the value of the property **STEAM_API_KEY** with your [Steam Web API Key](http://steamcommunity.com/dev/apikey).

```python
# Steam Configurations
STEAM_API_KEY = '{PUT_YOUR_STEAM_API_KEY}'
```

Finally, you can run application running:

```bash
sudo docker-compose up -d
```

## Testing

Open a browser of your preference and access the url [http://0.0.0.0:5000](http://0.0.0.0:5000).