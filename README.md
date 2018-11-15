
<h1 align="center">
  <br>
  <a href="https://www.instagram.com/ispnsp/?hl=en"><img src="https://i.imgur.com/fizxyvk.jpg" alt="Markdownify" width="200"></a>
  <br>
  Laika
  <br>
</h1>

  <h4 align="center">Near Space Program's dashboard that calculates, predicts and communicates with the capsule that is in the stratosphere</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#Files/Folders Structure">Files/Folders Structure</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://i.gyazo.com/ed388bc12102b219a22f597950a09050.png)

## Key Features

* Radar map of current capsule location
  - See the current location of the capsule in different types of maps, like a Radar Map, Google Maps, Leaflet Maps
* Interaction with sensors in capsule
  - While the capsule is in space, we can communicate and give orders to the capsule to turn off or on sensors, components, GPS, ...
* Reports and Logs
  - We receive logs and reports from the capsule including the consumed kWh and kWh left in the battery, temperature outside, how the sensors are consuming electricity, traffic consumption (how many MB of information receiving)
* Live Photos and Videos from Capsule
* Predictor
  - Predictor that calculates using advanced equations to calculate the landing, when the globe explode, the flight path
* Different themes
* Room Managment
* Previous Logs
* Charts and Graphs made automatically
  - You can download the charts to a google sheet
* Customizable settings
* Connection to the capsule via satellite or radio antenna
* Cross-platform
  - Windows, Mac, and Linux ready.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/ISPNearSpace/Laika.git

# Go into the repository
$ cd laika

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python manage.py runserver
```

### Note: The website is hosted on localhost:4200

## Files/Folders Structure
Here is a brief explanation of the template folder structure and some of its main files usage:

```
└── dashboard                   # dashboard app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for dashboard
│   └── __init__.py             # init file for dashboard
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── files                       # dashboard app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for files
│   └── __init__.py             # init file for files
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── home                        # restframework app
│   │   └── migrations          # Folder for models migrations
│   └── __init__.py             # init file for home
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│   └── serializers .py         # Django rest framework settings
│
└── landing                     # landing app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for landing
│   └── __init__.py             # init file for landing
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── live                        # live app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for live
│   └── __init__.py             # init file for live
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── mapbox                      # mapbox app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for mapbox
│   └── __init__.py             # init file for mapbox
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── nsp                         # main project settings
│   └── __init__.py             # all setings for project
│   └── settings.py             # database models.
│   └── urls.py                 # creates the urls and connects them to apps
│   └── wsgi.py                 # not important rn
│
└── predictor                   # predictor app
│   │   └── migrations          # Folder for models migrations
│   │   └── static/predictor    # Static files
│   │   └── templates/predictor # contains index file
│   │   │   └── index.html      # Main html for predictor
│   └── __init__.py             # init file for predictor
│   └── apps.py                 # apps config file
│   └── models.py               # database models.
│   └── urls.py                 # url config for app
│   └── views.py                # connects url to index file
│
└── .gitignore                  # Ignore specific files
└── .manage.py                  # Django file that runs project
└── requirements.txt            # Requirements that need to be installed to rundev
└── runtime.txt                 # Heroku run file
└── Procfile                    # details for heroku
└── db.sqlite3                  # database
└── LICENSE                     # License for project
```

## Credits

This software uses code from several open source packages.
- [CUSF](http://www.cusf.co.uk/) - Cambridge University Spaceflight
- [HabHub](http://habhub.org/)
- [Monchi Estevez](https://github.com/monchiestevez) - Dev and Founder
- [Diego Estevez](https://github.com/diegoestevez) - Dev and Founder

## Contributing

Please contact me before planning to contribute.

## Help

If you need help with anything or you have a suggestion contact me, If it is a bug or an error post it in the Issues tab.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ISPNearSpace/laika/LICENSE.md) file
