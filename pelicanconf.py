# Core
AUTHOR = 'Vote 4 West Ada'
SITENAME = 'Vote 4 West Ada'
SITEURL = "http://localhost:8000"
PATH = "content"
TIMEZONE = 'America/Boise'
DEFAULT_LANG = 'en'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Basic
DELETE_OUTPUT_DIRECTORY = True
USE_FOLDER_AS_CATEGORY = False

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DEFAULT_DATE = 'fs'

STATIC_PATHS = [
]

PAGE_EXCLUDES = STATIC_PATHS

LOG_FILTER = [
    (30, 'Empty alt attribute for image %s in %s'),
]

DEFAULT_PAGINATION = False

PLUGINS = [
    'plugins.bootstrapify',
]

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_URL = ""
AUTHOR_SAVE_AS = ""

CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""

TAG_URL = ""
TAG_SAVE_AS = ""

THEME = 'themes/bootstrap'

TYPOGRIFY = True
TYPOGRIFY_DASHES = 'default'

DIRECT_TEMPLATES = [
    'index',
]

TEMPLATE_PAGES = {
}
