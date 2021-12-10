from waitress import serve
from app import api

serve(api, host='0.0.0.0', port=80)