
<h1 align="center">
  <br>
  <a href="https://www.instagram.com/ispnsp/?hl=en"><img src="https://i.imgur.com/fizxyvk.jpg" alt="Markdownify" width="200"></a>
  <br>
  Laika
  <br>
</h1>

  <h4 align="center">Near Space Program's dashboard that calculates, predicts and communicates with the capsule that is in the stratosphere</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
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

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/ISPNearSpace/Laika.git

# Go into the repository
$ cd Laika

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python manage.py runserver
```

### Note: The website is hosted on localhost:4200

## Files/Folders Structure
Here is a brief explanation of the template folder structure and some of its main files usage:

```
└── src                         # Contains all template source files.
│   └── assets                  # Contains JS, CSS, images and icon fonts.
│   │   └── scripts             # Contains all JavaScript files.
│   │   │   └── charts          # Chart.js, Sparkline & Pie Chart plugins init.
│   │   │   └── chat            # All chat app JS code.
│   │   │   └── constants       # Template constant values like color values.
│   │   │   └── datatable       # Date table plugin init.
│   │   │   └── datepicker      # Bootstrap datepicker init.
│   │   │   └── email           # All email app code.
│   │   │   └── fullcalendar    # Fullcalendar plugin init.
│   │   │   └── googleMaps      # Google maps API integration code.
│   │   │   └── masonry         # Masonry layout code.
│   │   │   └── popover         # Bootstrap popover plugin init.
│   │   │   └── scrollbar       # Perfect scrollbar plugin init.
│   │   │   └── search          # Topbar toggle search init.
│   │   │   └── sidebar         # Sidebar JS code.
│   │   │   └── skycons         # Animated icons plugin init.
│   │   │   └── utils           # Basic utils used for proper rendering.
│   │   │   └── vectorMaps      # Vector maps plugin init.
│   │   │   └── index.js        # Indicator file.
│   │   │
│   │   └── static              # Contains the non-code files.
│   │   │   └── fonts           # Contains icon fonts.
│   │   │   └── images          # Contains all template images/svg.
│   │   │
│   │   └── styles              # Contains all SCSS files.
│   │       └── spec            # Contains custom SCSS files.
│   │       │   └── components  # Contains all template components.
│   │       │   └── generic     # Contains basic scaffolding styles.
│   │       │   └── screens     # Contains views specific styles.
│   │       │   └── settings    # Contains all template variables.
│   │       │   └── tools       # Contains all mixins.
│   │       │   └── utils       # Contains helper classes.
│   │       │   └── index.scss  # Indicator file.
│   │       │
│   │       └── vendor          # Contains all plugin files & custom styles.
│   │       └── index.scss      # Indicator file.
│   │
│   └── *.html                  # All HTML pages files .
└── webpack                     # Contains Webpack init code.
│   └── plugins                 # Contains all Webpack plugins config.
│   └── rules                   # Contains Loaders config code.
│   └── config.js               # Contains Webpack config object.
│   └── devServer.js            # Webpack dev server config code.
│   └── manifest.js             # All build system constants.
│
└── .editorconfig               # Keep same coding styles between code editors.
└── .gitattributes              # Git Attributes.
└── .gitignore                  # Ignored files in Git.
└── .stylelintrc.json           # SCSS/CSS Linting.
└── .travis.yml                 # Travis file
└── angular.json                # Angular main files
└── karma.conf.js               # Configuration file for Karma and Angular
└── browserslist                # Supported Browsers.
└── package.json                # Package metadata.
└── package-lock.json           # Exact tree that was generated for modules
└── protractor.conf.json        # Config files for Protractor
└── tsconfig.json               # TypeScript config
└── README.md                   # Manual file.
└── tslint.json                 # Extensible static analysis tool for TypeScript code
└── LICENSE                     # License for project
```

## Credits

This software uses code from several open source packages.

- [Nebular](https://akveo.github.io/nebular/)
- [Node.js](https://nodejs.org/)
- [Angular](https://angular.io/)
- [HabHub](http://habhub.org/)
- [Monchi Estevez](https://github.com/monchiestevez) - Developer and Founder

## Contributing

Please contact me before planning to contribute.

## Help

If you need help with anything or you have a suggestion contact me, If it is a bug or an error post it in the Issues tab.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ISPNearSpace/laika/LICENSE.md) file
