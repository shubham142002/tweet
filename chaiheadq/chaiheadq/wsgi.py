"""
WSGI config for chaiheadq project.
"""

import os
import sys

# Add the project directory to the Python path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chaiheadq.settings')

application = get_wsgi_application()
app = application  # for Vercel compatibility
