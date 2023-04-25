from datetime import date

AUTHOR = 'Kavya Gokul'
SITENAME = 'Kavya Gokul'
SITEURL = ''

DCOPY_DATE = date.today().year

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en_IN'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/prpl'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

MENUITEMS = (('About', '/about'),
             ('Blog', '/category/blog'),
             ('Photos', '/category/photos'),
             ('Projects', '/projects'),)

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social icons(please keep the title lowercase, for now)
SOCIAL = (('github', 'https://github.com/properlypurple'),
          ('instagram', 'https://instagram.com/properlypurple'),
          ('mastodon', 'https://tech.lgbt/@properlypurple'),
          ('linkedin', 'https://www.linkedin.com/in/properlypurple/'),
          ('youtube', 'https://www.youtube.com/channel/UCk1NmoSVZN_vdVPYIlXkBKg'),
          ('twitch', 'https://www.twitch.tv/properlypurple'))

DEFAULT_PAGINATION = 100

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DEBUG=1
CACHE_CONTENT = False


PHOTO_LIBRARY = 'static/images/uploads'
PHOTO_THUMB = (290, 290, 70)
PHOTO_SQUARE_THUMB = True
PHOTO_RESIZE_JOBS = 5
PHOTO_ARTICLE = (880, 660, 80)


PLUGINS = [
    "webassets",
    "jinja_filters",
    "more_categories",
    'photos',
    'series',
]