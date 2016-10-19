# GitLabPy
A Python module to help sort GitLab's Webhooks

Some of the JSON data coming from GitLab's webhooks are set as attributes to the GitLab class. Their are functions within the GitLab class that allow for easy handling of the JSON data.

## Requirements
* Python3 (has only been tested with Python 3.5.2)


## Install
* `pip install GitLabPy`

## How to use
Below is a list of the attributes and methods of the GitLab class. Each allows for easy handling of the GitLab webhook JSON data.

### Attributes
Some of the common JSON keys are assigned as attributes to the GitLab class. Here is a list of them...

`issue_types`, `object_kind`, `project_id`, `ref`, `project_name`, `user`, `commit`, `object_attributes`, `build_status`, `repository`, `repo_name`, `repo_homepage`

The JSON data that is instantiated with the GitLab class is also attribute of the class as well. `json_data` is the attribute name.

### Methods
##### get_url(url=None)
    Arguments:
        - url : type of url to return <string>
            * input types:
                - "http" : retrieve git http url
                - "ssh" : retrieve git ssh url
                - "homepage" : retrieve homepage url
                - (no input) : retrieve default git url, which is: "repository": {"url": <url>}
                    
##### get_repo_description()
    Arguments: None
    Checks to see if the key 'description' is in the webhook
    
##### build()
    Checks to see if JSON data from GitLab is build data and also checks to see that you want build data. If so, return True
    Arguments: *args <bool><string><list>
        - can be a list of certain build data  you want
        - build types are 'success', 'failed', 'runnning'
        
##### note(note_types=False)
    Checks to see if JSON data is a note (comment) and you want note JSON data. If so, return True
    Arguments: note_types <bool>
        - Returns True if you want note type JSON data to return True and JSON data is a note
        - Default - False
        
##### merge_request(merge_request_types=False)
    Checks to see if JSON data is a merge request and if you want merge_request data. If so, return True
    Arguments: merge_request_types <bool>
        - True if you want merge request data from GitLab to be returned if JSON data is merge request.
        - Default - False
        
##### issue()
    Checks to see if JSON data is an issue from GitLabJSON
    Arguments: *args <bool><string><list>
        - can be list of issue types or boolean
        - issue types are 'open', 'update', 'closed'
        - True if you want all issues pass this conditional function
