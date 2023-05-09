import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://aibuddy.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'UJkoYhwerltuqo0IFHR6XFuT3bLYvITOgj7uikx3KihollttowhHG1E7RKBGGdV3i0DKnsD7ebWRACDb1IHUcQ=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'aibuddy'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}