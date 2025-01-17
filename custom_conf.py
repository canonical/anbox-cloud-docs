import datetime
import os
import subprocess


# Custom configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# The file is included in the common conf.py configuration file.
# You can modify any of the settings below or add any configuration that
# is not covered by the common conf.py file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# If you're not familiar with Sphinx and don't want to use advanced
# features, it is sufficient to update the settings in the "Project
# information" section.

############################################################
### Project information
############################################################

# Product name
project = 'Canonical Anbox Cloud'
author = 'Anbox Cloud team'

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = 'Anbox Cloud documentation'

# The default value uses the current year as the copyright year.
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = '%s, %s' % (datetime.date.today().year, author)

## Open Graph configuration - defines what is displayed as a link preview
## when linking to the documentation from another website (see https://ogp.me/)
# The URL where the documentation will be hosted (leave empty if you
# don't know yet)
# NOTE: If no ogp_* variable is defined (e.g. if you remove this section) the
# sphinxext.opengraph extension will be disabled.
ogp_site_url = 'https://canonical-anbox-cloud.readthedocs-hosted.com/'
# The documentation website name (usually the same as the product name)
ogp_site_name = 'Anbox Cloud documentation'
# The URL of an image or logo that is used in the preview
ogp_image = 'https://assets.ubuntu.com/v1/04242fd4-Anbox-logo-2022_square.svg'

# Update with the local path to the favicon for your product
# (default is the circle of friends)
html_favicon = '.sphinx/_static/favicon.png'

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {

    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    'product_page': 'anbox-cloud.io',

    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    'product_tag': '_static/logo.svg',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': 'https://discourse.ubuntu.com',
    'discourse_users': 'https://discourse.ubuntu.com/c/anbox-cloud/users/148',

    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    'mattermost': '',

    # Change to the GitHub URL for your project
    'github_url': 'https://github.com/canonical/anbox-cloud-docs',

    # Change to the branch for this version of the documentation
    'github_version': 'main',

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'github_folder': '/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    'sequential_nav': 'both',
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug = "docs"

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',
# You can also configure redirects in the Read the Docs project dashboard
# (see https://docs.readthedocs.io/en/stable/guides/redirects.html).
# NOTE: If this variable is not defined, set to None, or the dictionary is empty,
# the sphinx_reredirects extension will be disabled.
redirects = {

    'reference/roadmap': '../release-notes/release-notes',
    'reference/supported-versions': '../release-notes/release-notes',
    'explanation/gpus-instances': '../rendering-graphics',
    'howto/update/landing': '../../upgrade/landing',
    'howto/update/upgrade-anbox': '../../upgrade/upgrade-anbox',
    'howto/update/upgrade-appliance': '../../upgrade/upgrade-appliance',
    'howto/update/control-updates': '../../upgrade/landing',
    'howto/addons/customise-android-example': '../customize-android-example',
    'howto/install/customise-installation': '../customize-installation',
}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links
linkcheck_ignore = [
    'http://127.0.0.1:8000',
    'https://support.canonical.com/',
    'https://assets.ubuntu.com/manager',
    'https://images.anbox-cloud.io/stable/',
    'https://10.2.9.2/',
    'http://Add-SECURITY.md'
    ]

# This setting will check the links but not the anchors
linkcheck_anchors = False

# This list will be appended to linkcheck_anchors_ignore_for_url
custom_linkcheck_anchors_ignore_for_url = [
    r'https://matrix\.to/.*',
    r'https://canonical\.github\.io/anbox-cloud\.github\.com/.*',
    r'https://juju.is/docs/juju/.*',
]

# Pages to ignore for link check
linkcheck_exclude_documents = [
    r'.*/release-notes/.*'
]

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.
# NOTE: Remove this variable to disable the MyST parser extensions.
custom_myst_extensions = []

# Add custom Sphinx extensions as needed.
# This array contains recommended extensions that should be used.
# NOTE: The following extensions are handled automatically and do
# not need to be added here: myst_parser, sphinx_copybutton, sphinx_design,
# sphinx_reredirects, sphinxcontrib.jquery, sphinxext.opengraph
custom_extensions = [
    'sphinx_tabs.tabs',
    'canonical.youtube-links',
    'canonical.related-links',
    'canonical.custom-rst-roles',
    'canonical.terminal-output'
	    ]

# Add custom required Python modules that must be added to the
# .sphin	x/requirements.txt file.
# NOTE: The following modules are handled automatically and do not need to be
# added here: canonical-sphinx-extensions, furo, linkify-it-py, myst-parser,
# pyspelling, sphinx, sphinx-autobuild, sphinx-copybutton, sphinx-design,
# sphinx-reredirects, sphinx-tabs, sphinxcontrib-jquery, sphinxext-opengraph
custom_required_modules = []

# Add files or directories that should be excluded from processing.
custom_excludes = [
    'doc-cheat-sheet*',
    ]

# Add CSS files (located in .sphinx/_static/)
custom_html_css_files = []

# Add JavaScript files (located in .sphinx/_static/)
custom_html_js_files = []

## The following settings override the default configuration.

# Specify a reST string that is included at the end of each file.
# If commented out, use the default (which pulls the reuse/links.txt
# file into each reST file).
# custom_rst_epilog = ''

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

# Add tags that you want to use for conditional inclusion of text
# (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tags)
custom_tags = []

############################################################
### Additional configuration
############################################################

## Add any configuration that is not covered by the common conf.py file.

# Define a :center: role that can be used to center the content of table cells.
rst_prolog = """
.. role:: center
   :class: align-center
"""

## Generate dynamic configuration using scripts
# Inject AMS configuration valuues and Node configuration values from the swagger
# specification hosted on Github.
def generate_ams_configuration():
    from scripts.ams_configuration import parse_swagger

    with open("scripts/requirements.txt", "r") as f:
        for req in f.readlines():
            custom_required_modules.append(req)
    ams_configuration_file = "reference/ams-configuration.md"
    import yaml

    with open("reference/api-reference/ams-api.yaml", "r") as f:
        swagger = yaml.safe_load(f)
    parse_swagger(swagger, ams_configuration_file)


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
