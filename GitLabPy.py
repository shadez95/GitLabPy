import json
# from gitlab_json import GitLabJSON
# with open(".\server-output\gitlab-output.json") as json_file:
#     d = json.load(json_file)

class GitLab:
    """
    Instantiate with 2 arguments, parsed json string <string> and settings <dict>
    """
    def __init__(self, arg1, arg2):
        self.json_data = arg1
        self.settings = arg2
        self.object_kind = arg1.get("object_kind", "")
        self.project_id = arg1.get("project_id", "")
        self.ref = arg1.get("ref", "")
        self.project_name = arg1.get("project_name", "")
        self.user = arg1.get("user", "")
        self.commit = arg1.get("commit", "")
        self.object_attributes = arg1.get("object_attributes", "")
        self.build_status = arg1.get("build_status", "")

        repo_obj = arg1.get("repository", "")
        if repo_obj != "":
            self.repository = repo_obj
            self.repo_name = repo_obj.get("name", "")
            self.repo_homepage = repo_obj.get("homepage", "")

    def check_repository_atttr(self):
        if self.repository == "":
            return False
        else:
            return True

    def get_repo_url(self, git_type=""):

        if check_repository_atttr():
            return False
        if git_type.lower() == "http":
            return self.repository.get("git_http_url")
        elif git_type.lower() == "ssh":
            return self.repository.get("git_ssh_url")
        else:
            return self.repository.get("url")

    def get_url(self, url=None):
        """
        Arguments:
            - json_data : parsed json <string>
            - git_type : type of git url <string>
                * input types:
                    - "http" : retrieve git http url
                    - "ssh" : retrieve git ssh url
                    - "homepage" : retrieve homepage url
                    - (no input) : retrieve default git url, which is: "repository": {"url": <url>}
        """
        if check_repository_atttr():
            return False
        if url.lower() == "ssh":
            return self.repository.get("git_ssh_url")
        elif url.lower() == "http":
            return self.repository.get("git_http_url")
        elif url.lower() == "homepage":
            return self.repository.get("homepage")
        else:
            return self.repository.get("url")

    def get_repo_description(self):
        if check_repository_atttr():
            return self.repository.get("description")
        else:
            return False

    def whoops_error(self, message=None, **kwargs):
        # In the future this needs to not show kwargs and other debug information
        if message:
            return "Whoops! An error occured.. object_kind = '{}'\n{}\nkwargs: {}\n".format(self.object_kind, message, kwargs)
        else:
            return "Whoops! An error occured.. object_kind = '{}'\nkwargs: {}\n".format(self.object_kind, kwargs)

    def build(self):
        conditions = self.settings.get("build_types")
        if "SUCCESS" in conditions:
            SUCCESS = True
        else:
            SUCCESS = False
        if "FAILED" in conditions:
            FAILED = True
        else:
            FAILED = False
        if "CREATED" in conditions:
            CREATED = True
        else:
            CREATED = False

        if self.build_status.upper() == "CREATED" and CREATED:
            msg = "[BUILD] Commit: '{}'\nAuthor: {}\nBuild Status: {}\nhttps://gitlab.com/71stSOG/71stWebsite/pipelines/{}".format(
                self.commit.get("message"), self.user.get("name"), self.build_status.upper()
            )
        elif self.build_status.upper() in {"SUCCESS", "FAILED"} and CREATED or FAILED:
            msg = "[BUILD] Commit: '{}'\nAuthor: {}\nBuild Duration: {}\nBuild Status: {}\nhttps://gitlab.com/71stSOG/71stWebsite/pipelines/{}".format(
                self.commit.get("message"), self.user.get("name"),
                self.json_data.get("build_duration"), self.build_status.upper(),
                self.commit.get("id")
            )
        else:
            msg = self.whoops_error(message="Error occurred in build function")
        return msg

    def note(self):
        conditions = self.settings.get("note_types")
        msg = ""
        if conditions:
            msg = "[{}] {} commented on {}\n'{}'\n{}".format(
                self.object_attributes.get("noteable_type"), self.user.get("name"),
                self.object_attributes.get("id"), self.object_attributes.get("note"),
                self.object_attributes.get("url")
            )
        return msg

    def merge_request(self):
        conditions = self.settings.get("merge_request")
        msg = ""
        if conditions:
            msg = "[MERGE REQUEST] {} wants to merge '{}' into '{}'\n{}\n{}".format(
                self.user.get("name"), self.object_attributes.get("source_branch"), self.object_attributes.get("target_branch"),
                self.object_attributes.get("title"), self.json_data.get("url")
            )
        return msg

    def issue(self):
        conditions = self.settings.get("issue_types")
        ALL = False
        if type(conditions) is list:
            for item in conditions:
                if item == "CREATED":
                    CREATED = True
                else:
                    CREATED = False
                if item == "UPDATE":
                    UPDATE = True
                else:
                    UPDATED = False
                if item == "CLOSED":
                    CLOSED = True
                else:
                    CLOSED = False
        elif type(conditions) is bool:
            ALL = True
        else:
            return self.whoops_error("Error occurred in issue function")
        if self.object_attributes.get("action") == "created" or ALL:
            msg = "[ISSUE] #{} {}\nCreated by {}\n{}".format(self.object_attributes.get("iid"),
                self.object_attributes.get("title"), self.user.get("name"),
                self.object_attributes.get("url")
            )
        elif self.object_attributes.get("action") == "update" or ALL:
            msg = "[ISSUE] #{} {}\nUpdated by {}\n{}".format(self.object_attributes.get("iid"),
                self.object_attributes.get("title"), self.user.get("name"),
                self.object_attributes.get("url")
            )
        elif self.object_attributes.get("action") == "closed" or ALL:
            msg = "[ISSUE] #{} {}\nClosed by {}\n{}".format(self.object_attributes.get("iid"),
                self.object_attributes.get("title"), self.user.get("name"),
                self.object_attributes.get("url")
            )
        return msg
