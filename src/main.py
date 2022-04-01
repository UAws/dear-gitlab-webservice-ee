from selenium_controller.github import Github
from selenium_controller.gitlab import Gitlab
from utils.shell_executor.executor import execute_now


def main():
    github = Github()
    gitlab = Gitlab()

    new_tags = list()

    execute_now('git fetch --all')

    gitlab_versions = gitlab.fetch_gitlab_map_versions()
    github_tags = github.fetch_github_available_docker_versions()

    github_tags = [t.replace('v', '').replace('.m1', '') for t in github_tags]

    # match the gitlab version which not inside GitHub tags, the github tags contains gitlab version
    for gitlab_version in gitlab_versions:
        if gitlab_version not in github_tags:
            new_tags.append(gitlab_version)

    for tag in new_tags:
        github.create_new_branch(tag)

if __name__ == "__main__":
    main()
