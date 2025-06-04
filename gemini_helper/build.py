import time
from google.cloud import api_keys_v2 as keyapi
from google.auth import default
from googleapiclient.discovery import build
import os

def create_api_key(project_id):
    client = keyapi.ApiKeysClient()    
    api_target = keyapi.ApiTarget()
    api_target.service = "generativelanguage.googleapis.com"
    
    restrictions = keyapi.types.Restrictions(
        api_targets=[api_target]
    )
    
    keyname = "GeminiKey"
    key_info = keyapi.Key(
        display_name=keyname,
        restrictions = restrictions
    )

    # Initialize request argument(s)
    request = keyapi.CreateKeyRequest(
        parent=f"projects/{project_id}/locations/global",
        key=key_info
    )
    operation = client.create_key(request=request)
    print("Creating Restricted key...")

    response = operation.result()

    return response.key_string

def enable_apis_for_project(project_id):
    # List of APIs to enable
    api_names = [
        'apikeys.googleapis.com', 
        'generativelanguage.googleapis.com',
    ]
    
    print("Enabling APIs...")
    credentials, _ = default()
    service = build('serviceusage', 'v1', credentials=credentials)
    
    enabled_services = []
    max_retries = 3
    all_success = True  # Track if all APIs are enabled successfully
    
    for ser in api_names:
        success = False
        retries = 0
        
        while not success and retries < max_retries:
            print(f"Enabling API: {ser}")
            try:
                request = service.services().enable(
                    name=f'projects/{project_id}/services/{ser}'
                )
                response = request.execute()
                enabled_services.append(response)
                success = True
                print(f"API {ser} enabled successfully.")
            except Exception as e:
                print(f"Error enabling API {ser}: {e}")
                retries += 1
                print(f"Retrying... Attempt {retries}/{max_retries}")
                time.sleep(2 ** retries)  # Exponential backoff
        
        if not success:
            print(f"Failed to enable API: {ser} after {max_retries} retries")
            all_success = False  # If any API fails, set overall success to False
    
    print(f"Enabled {len(enabled_services)} APIs successfully.")
    
    return all_success

def get_api_key():
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project:
        return "GOOGLE_CLOUD_PROJECT is not set in environment variables"
    success = enable_apis_for_project(project)
    if not success:
        return "Failed to enable required APIs"
    else:
        print("Waiting for API propagation...")
        time.sleep(3)
        key = create_api_key(project)
        return key
