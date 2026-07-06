import urllib.request
import json
import sys
import os

# 1. Load Prolific token from config file
token = None
try:
    config_path = os.path.expanduser("~/.config/prolific-oss/prolific.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            for line in f:
                if "prolific_token:" in line:
                    token = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
except Exception as e:
    print(f"Error reading config: {e}", file=sys.stderr)

if not token:
    print("Error: Prolific token not found in config file.", file=sys.stderr)
    sys.exit(1)

# Helper function to make API requests
def make_request(url, method="GET", payload=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Token {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "prolific-oss/cli")
    if payload:
        req.data = json.dumps(payload).encode("utf-8")
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code} on {method} {url}: {e.reason} - Body: {body}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error calling {url}: {e}", file=sys.stderr)
        return None

# 2. Get Default Project ID
print("Fetching default project ID...")
workspaces_data = make_request("https://api.prolific.com/api/v1/workspaces/")
if not workspaces_data or "results" not in workspaces_data or not workspaces_data["results"]:
    print("Failed to retrieve workspaces.", file=sys.stderr)
    sys.exit(1)

# Get first workspace
workspace_id = workspaces_data["results"][0]["id"]
projects_data = make_request(f"https://api.prolific.com/api/v1/workspaces/{workspace_id}/projects/")
if not projects_data or "results" not in projects_data or not projects_data["results"]:
    print("Failed to retrieve projects.", file=sys.stderr)
    sys.exit(1)

project_id = projects_data["results"][0]["id"]
print(f"Using Project ID: {project_id}")

# 3. Parse ai-adoption-survey.yaml configuration dynamically
yaml_path = "/Users/allanyeung/Documents/June 17 prolific/ai-adoption-survey.yaml"
if not os.path.exists(yaml_path):
    print(f"Error: Configuration file not found at {yaml_path}", file=sys.stderr)
    sys.exit(1)

print(f"Parsing configuration from {yaml_path}...")
config = {}
filters = []
current_filter = None
in_device_comp = False
in_filters = False

with open(yaml_path, "r") as f:
    for line in f:
        raw_line = line
        line = line.split('#')[0].strip()
        if not line:
            continue
        
        # Detect list items
        is_list = False
        if line.startswith("-"):
            is_list = True
            line = line[1:].strip()
            
        if not line:
            continue
            
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            
            if key == "device_compatibility":
                in_device_comp = True
                in_filters = False
                continue
            elif key == "filters":
                in_device_comp = False
                in_filters = True
                continue
            elif key == "filter_id":
                current_filter = {"filter_id": val}
                filters.append(current_filter)
                continue
            elif key == "selected_values":
                current_filter["selected_values"] = []
                continue
            elif key == "selected_range":
                current_filter["selected_range"] = {}
                continue
            elif key == "lower" and current_filter and "selected_range" in current_filter:
                current_filter["selected_range"]["lower"] = int(val)
                continue
            elif key == "upper" and current_filter and "selected_range" in current_filter:
                current_filter["selected_range"]["upper"] = int(val)
                continue
            
            # Simple string and int fields
            if val.isdigit():
                config[key] = int(val)
            elif val.replace('.', '', 1).isdigit():
                config[key] = float(val)
            else:
                config[key] = val
        else:
            val = line.strip('"').strip("'")
            if in_device_comp:
                config.setdefault("device_compatibility", []).append(val)
            elif current_filter:
                if "selected_values" in current_filter:
                    current_filter["selected_values"].append(val)


# Build final payload
payload = {
    "name": config.get("name"),
    "internal_name": config.get("internal_name"),
    "description": config.get("description"),
    "external_study_url": config.get("external_study_url"),
    "prolific_id_option": config.get("prolific_id_option"),
    "completion_code": config.get("completion_code"),
    "completion_option": config.get("completion_option"),
    "total_available_places": int(config.get("total_available_places", 1)),
    "estimated_completion_time": int(config.get("estimated_completion_time", 3)),
    "reward": int(config.get("reward", 50)),
    "device_compatibility": config.get("device_compatibility", ["desktop", "tablet", "mobile"]),
    "project": project_id,
    "filters": filters
}

# 4. Check for existing unpublished study with the same internal_name
print("Checking for existing draft study...")
studies_data = make_request("https://api.prolific.com/api/v1/studies/")
existing_study = None

if studies_data and "results" not in studies_data:
    # Handle direct results list
    results = studies_data
else:
    results = studies_data.get("results", []) if studies_data else []

for study in results:
    if study.get("internal_name") == payload["internal_name"] and study.get("status") == "UNPUBLISHED":
        existing_study = study
        break

# 5. Create or Update Study
if existing_study:
    study_id = existing_study["id"]
    print(f"Found existing draft study (ID: {study_id}). Updating...")
    url = f"https://api.prolific.com/api/v1/studies/{study_id}/"
    result = make_request(url, method="PATCH", payload=payload)
    action = "Updated"
else:
    print("No matching draft study found. Creating new draft study...")
    url = "https://api.prolific.com/api/v1/studies/"
    result = make_request(url, method="POST", payload=payload)
    action = "Created"

if result:
    print(f"\nSuccess! Study {action} successfully:")
    print(f"  Study ID: {result.get('id')}")
    print(f"  Name: {result.get('name')}")
    print(f"  Status: {result.get('status')}")
    print(f"  Places: {result.get('total_available_places')}")
    print(f"  Survey URL: {result.get('external_study_url')}")
else:
    print("\nFailed to create or update study.", file=sys.stderr)
    sys.exit(1)
