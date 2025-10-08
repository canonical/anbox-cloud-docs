import datetime
import ast
import os
import subprocess

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Our starter pack uses the custom Canonical Sphinx extension
# to keep all documentation based on it consistent and on brand:
# https://github.com/canonical/canonical-sphinx


#######################
# Project information #
#######################

# Project name
#
# Update with the official name of your project or product

project = "Canonical Anbox Cloud"
author = "Canonical Ltd."


# Sidebar documentation title; best kept reasonably short
#
# To include a version number, add it here (hardcoded or automated).
#
# To disable the title, set to an empty string.

html_title = "Anbox Cloud" + " documentation"


# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
# If your docs need another license, specify it instead of 'CC-BY-SA'.
#
# If your documentation is a part of the code repository of your project,
# it inherits the code license instead; specify it instead of 'CC-BY-SA'.
#
# For static works, it is common to provide the first publication year.
# Another option is to provide both the first year of publication
# and the current year, especially for docs that frequently change,
# e.g. 2022–2023 (note the en-dash).
#
# A way to check a repo's creation date is to get a classic GitHub token
# with 'repo' permissions; see https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the API's output:
#
#       curl -H 'Authorization: token <TOKEN>' \
#         -H 'Accept: application/vnd.github.v3.raw' \
#         https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "%s CC-BY-SA, %s" % (datetime.date.today().year, author)


# Documentation website URL
#
# Update with the official URL of your docs or leave empty if unsure.
#
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/

ogp_site_url = "https://documentation.ubuntu.com/anbox-cloud/"


# Preview name of the documentation website
#
# To use a different name for the project in previews, update as needed.

ogp_site_name = "Anbox Cloud"


# Preview image URL
#
# To customise the preview image, update as needed.

ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"


# Product favicon; shown in bookmarks, browser tabs, etc.

# To customise the favicon, uncomment and update as needed.

html_favicon = '.sphinx/_static/favicon.png'


# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context

html_context = {
    # Product page URL; can be different from product docs URL
    #
    # Change to your product website URL,
    #       dropping the 'https://' prefix, e.g. 'ubuntu.com/lxd'.
    #
    # If there's no such website,
    #       remove the {{ product_page }} link from the page header template
    #       (usually .sphinx/_templates/header.html; also, see README.rst).
    "product_page": "canonical.com/anbox-cloud",
    # Product tag image; the orange part of your logo, shown in the page header
    #
    # To add a tag image, uncomment and update as needed.
    'product_tag': '_static/logo.svg',
    # Your Discourse instance URL
    #
    # Change to your Discourse instance URL or leave empty.
    #
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.ubuntu.com/c/project/anbox-cloud/49",
    # Your Mattermost channel URL
    #
    # Change to your Mattermost channel URL or leave empty.
    "mattermost": "",
    # Your Matrix channel URL
    #
    # Change to your Matrix channel URL or leave empty.
    "matrix": "https://matrix.to/#/#anbox-cloud:ubuntu.com",
    # Your documentation GitHub repository URL
    #
    # Change to your documentation GitHub repository URL or leave empty.
    #
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    "github_url": "https://github.com/canonical/anbox-cloud-docs",
    # Docs branch in the repo; used in links for viewing the source files
    #
    # To customise the branch, uncomment and update as needed.
    'repo_version': 'main',
    # Docs location in the repo; used in links for viewing the source files
    #


    # To customise the directory, uncomment and update as needed.
    "repo_folder": "/",
    # To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "both",
    # To enable listing contributors on individual pages, set to True
    "display_contributors": True,

    # Required for feedback button
    'github_issues': 'enabled',
}

# To enable the edit button on pages, uncomment and change the link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
# html_theme_options = {
# 'source_edit_link': 'https://github.com/canonical/anbox-cloud-docs',
# }

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897
#
# If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.

slug = 'anbox-cloud'

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# Base URL of RTD hosted project
# Include the trailing slash in the URL, it makes a difference

html_baseurl = 'https://documentation.ubuntu.com/anbox-cloud/'

# URL scheme; {link} is the default configuration

sitemap_url_scheme = "{link}"

# Template and asset locations

html_static_path = [
    ".sphinx/_static",
    # This is required for Google Analytics to work till we unify
    # all the static files into one well-known directory.
    "_static",
]
templates_path = [
    # This is required for Google Analytics to work.
    "_templates",
]

# Exclude unnecessary URLs for better indexing

sitemap_excludes = [
    "genindex/",
    "404/",
    "search/",
]


#############
# Redirects #
#############

# To set up redirects: https://documatt.gitlab.io/sphinx-reredirects/usage.html
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# NOTE: If undefined, set to None, or empty,
#       the sphinx_reredirects extension will be disabled.

redirects = {

    'reference/roadmap': '../release-notes/release-notes',
    'reference/supported-versions': '../release-notes/release-notes',
    'reference/api-reference/landing': '../',
    'reference/cmd-ref/landing': '../',
    'reference/landing': '../',
    'explanation/gpus-instances': '../rendering-graphics',
    'explanation/cryptography/crypto_ams': '../../security/ams',
    'explanation/cryptography/crypto_anbox_runtime': '../../security/anbox-runtime',
    'explanation/cryptography/crypto_charms': '../../security/charms',
    'explanation/cryptography/crypto_dashboard': '../../security/dashboard',
    'explanation/cryptography/crypto_stream_agent': '../../security/streaming-stack',
    'explanation/cryptography/crypto_stream_gateway': '../../security/streaming-stack',
    'explanation/anbox-security': '../security/',
    'explanation/landing': '../',
    'explanation/security/landing': '../',
    'howto/update/landing': '../../upgrade/',
    'howto/update/upgrade-anbox': '../../upgrade/upgrade-anbox',
    'howto/update/upgrade-appliance': '../../upgrade/upgrade-appliance',
    'howto/update/control-updates': '../../upgrade/',
    'howto/addons/customise-android-example': '../customize-android-example',
    'howto/install/customise-installation': '../customize-installation',
    'howto/anbox/manage-images': '../../images/',
    'howto/install-appliance/enable-oidc': '../setup-custom-idp/',
    'howto/android/access-instance': '../access-android-instance',
    'howto/aar/landing': '../',
    'howto/addons/landing': '../',
    'howto/anbox-runtime/landing': '../',
    'howto/anbox/landing': '../',
    'howto/android/landing': '../',
    'howto/application/landing': '../',
    'howto/cluster/landing': '../',
    'howto/dashboard/landing': '../',
    'howto/images/landing.md': '../',
    'howto/landing': '../',
    'howto/install-appliance/landing': '../',
    'howto/install-appliance/setup-oidc/landing': '../',
    'howto/install-appliance/setup-oidc': '../../setup-custom-idp/',
    'howto/install-appliance/setup-oidc/auth0': '../../../setup-custom-idp/',
    'howto/install-appliance/setup-oidc/keycloak': '../../../setup-custom-idp/',
    'howto/install-appliance/setup-oidc/ory': '../../../setup-custom-idp/',
    'howto/install-appliance/setup-oidc/configure-oidc': '../../../setup-custom-idp/configure-oidc',
    'howto/install/landing': '../',
    'howto/instance/landing': '../',
    'howto/monitor/landing': '../',
    'howto/port/landing': '../',
    'howto/stream/landing': '../',
    'howto/troubleshoot/landing': '../',
    'howto/upgrade/landing': '../',
    'tutorial/getting-started-aaos': '../../howto/android/set-automotive-properties',
    'tutorial/getting-started-dashboard': '../create-test-virtual-device',
    'tutorial/getting-started': '../create-test-virtual-device',
    'tutorial/landing': '../',
    'tutorial/creating-addon': '../../howto/addons/create-addon',
    'contribute/landing': '../',
}


###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
#
# Remove or adjust the ACME entry after you update the contributing guide

linkcheck_ignore = [
    'http://127.0.0.1:8000',
    'https://support.canonical.com/',
    'https://assets.ubuntu.com/manager',
    'https://images.anbox-cloud.io/stable/',
    'https://10.2.9.2/',
    'http://Add-SECURITY.md',
    'https://jwt.io/'
    ]

# This setting will check the links but not the anchors
linkcheck_anchors = False


# A regex list of URLs where anchors are ignored by 'make linkcheck'

custom_linkcheck_anchors_ignore_for_url = [
    r'https://matrix\.to/.*',
    r'https://canonical\.github\.io/anbox-cloud\.github\.com/.*',
    r'https://juju.is/docs/juju/.*',
]

# Pages to ignore for link check
linkcheck_exclude_documents = [
    r'.*/release-notes/.*'
]

# give linkcheck multiple tries on failure
linkcheck_timeout = 30
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify

myst_enable_extensions = set({"colon_fence"})


# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html

# NOTE: The canonical_sphinx extension is required for the starter pack.
#       It automatically enables the following extensions:
#       - custom-rst-roles
#       - myst_parser
#       - notfound.extension
#       - related-links
#       - sphinx_copybutton
#       - sphinx_design
#       - sphinx_reredirects
#       - sphinx_tabs.tabs
#       - sphinxcontrib.jquery
#       - sphinxext.opengraph
#       - terminal-output
#       - youtube-links

extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx_sitemap",
]

# Excludes files or directories from processing

exclude_patterns = [
    'contribute/doc-cheat-sheet.md',
    'README.md',
    'SECURITY.md',
    '.github/pull_request_template.md',
    'venv/**',
    '**/*.dist-info/**',
]

# Adds custom CSS files, located under 'html_static_path'

html_css_files = [
    "css/cookie-banner.css"
]


# Adds custom JavaScript files, located under 'html_static_path'

html_js_files = [
    "js/cookie-banner-bundle.js"
]


# Specifies a reST snippet to be appended to each .rst file

rst_epilog = """
.. include:: /reuse/links.txt
"""

# Feedback button at the top; enabled by default
#
# To disable the button, uncomment this.

# disable_feedback_button = True


# Your manpage URL
#
# To enable manpage links, uncomment and update as needed.
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.

# manpages_url = f'https://manpages.ubuntu.com/manpages/{codename}/en/' + \
#     f'man{section}/{page}.{section}.html'


# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34

if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

#============================================#
# Anbox Cloud specific configurations
# The following configuration won't be available
# in the starter pack. It is maintained by the
# Anbox cloud team.
#============================================#

## Generate dynamic configuration using scripts
# Inject AMS configuration valuues and Node configuration values from the swagger
# specification hosted on Github.

custom_required_modules = []

def generate_ams_configuration():
    import sys
    sys.path.append(os.path.dirname(__file__))
    from scripts.ams_configuration import parse_swagger

    with open("scripts/requirements.txt", "r") as f:
        for req in f.readlines():
            custom_required_modules.append(req)
    ams_configuration_file = "reference/ams-configuration.md"
    import yaml

    with open("reference/api-reference/ams-api.yaml", "r") as f:
        swagger = yaml.safe_load(f)
    parse_swagger(swagger, ams_configuration_file)

# Anbox specific function to generate dynamic AMS configuration
# Add this change to conf.py every time the starter pack is upgraded to a later version.
generate_ams_configuration()


## The following code is to automatically load the API from swagger into documentation.

# Path to copy the YAML files during build
html_extra_path = ['.sphinx/_extra']

# The swagger-ui repository is required to be able to render the swagger YAML
# file as browseable API documentation. The below variable specifies which
# git repository to fetch it from.
swagger_ui_repository = "https://github.com/swagger-api/swagger-ui"

# Download and link swagger-ui files
if not os.path.isdir('.sphinx/deps/swagger-ui'):
    subprocess.check_call(["git", "clone", "--depth=1", swagger_ui_repository, ".sphinx/deps/swagger-ui"])

os.makedirs('.sphinx/_static/swagger-ui/', exist_ok=True)

if not os.path.islink('.sphinx/_static/swagger-ui/swagger-ui-bundle.js'):
    os.symlink('../../deps/swagger-ui/dist/swagger-ui-bundle.js', '.sphinx/_static/swagger-ui/swagger-ui-bundle.js')
if not os.path.islink('.sphinx/_static/swagger-ui/swagger-ui-standalone-preset.js'):
    os.symlink('../../deps/swagger-ui/dist/swagger-ui-standalone-preset.js', '.sphinx/_static/swagger-ui/swagger-ui-standalone-preset.js')
if not os.path.islink('.sphinx/_static/swagger-ui/swagger-ui.css'):
    os.symlink('../../deps/swagger-ui/dist/swagger-ui.css', '.sphinx/_static/swagger-ui/swagger-ui.css')
