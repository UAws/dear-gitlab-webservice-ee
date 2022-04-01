import os
from unittest import TestCase

from ghapi.core import print_summary

from selenium_controller.github import Github, find
from selenium_controller.gitlab import Gitlab


class Test(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.gitlab = Gitlab()
        self.github = Github()

    def test_gitlab(self):
        self.gitlab.fetch_gitlab_map_versions()

        print(len(self.gitlab.gitlab_versions))

        print(self.gitlab.gitlab_versions[0])

    def test_github(self):

        self.github.api.debug = print_summary

        # print(os.getenv('GITHUB_TOKEN'))

        self.github.fetch_github_available_docker_versions()

        print(self.github.packages)

        tags_list = list()

        for p in self.github.packages:

            tag = p['metadata']['container']['tags']

            if tag:
                tags_list.append(tag[0])

        print(tags_list)

    def test_find(self):
        print(find('Dockerfile', '../../../'))

    def test_find_dockerfile(self):
        self.github.create_new_branch('10.0.0')

    def test_compare(self):
        gitlab_versions = self.gitlab.fetch_gitlab_map_versions()
        github_tags = self.github.fetch_github_available_docker_versions()

        new_tags = list()

        github_tags = [t.replace('v', '').replace('.m1', '') for t in github_tags]

        # match the gitlab version which not inside GitHub tags, the github tags contains gitlab version
        for gitlab_version in gitlab_versions:
            if gitlab_version not in github_tags:
                new_tags.append(gitlab_version)

        print(new_tags)
