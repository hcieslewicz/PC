# Mario saving the princess

This project provide example of implementation 'Mario saving the princess' game using python and flask.

## Getting Started

Get the copy of this example using git:
```
git clone https://github.com/hcieslewicz/PC.git
```


### Prerequisites

To have it running You need to have:
* Python 3.7 - https://www.python.org/
* Python packages: Flask, Flask, Flask-SQLAlchemy, flask-restplus

To install required packages simply run:
```
pip install Flask, Flask-SQLAlchemy, flask-restplus
```

## Running the app

To run the flask app You have to call python with the main direcotry. On Windows open command prompt and type:

```
python.exe app.py
```

## API call examples
```angular2html
curl -X POST "http://127.0.0.1:5000/api/v1/games/mario" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"game_name\": \"mario\",  \"size\": 3,  \"grid\": [\"--m\", \"-x-\", \"p--\"]}"
```
## API documentation

API documenation is generated to swagger compatible by flask-restplus. It can be access under link:
```
http://127.0.0.1:5000/api/v1
```

## Authors

* **Hubert Cieslewicz** (https://github.com/hcieslewicz)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
