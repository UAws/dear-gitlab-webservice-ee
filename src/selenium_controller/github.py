from fileinput import FileInput
from dotenv import load_dotenv
from ghapi.all import GhApi

from utils.shell_executor.executor import execute_now
import os, fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


class Github:

    def __init__(self):
        load_dotenv()

        self.api = GhApi(owner='UAws', repo='dear-gitlab-webservice-ee')
        self.packages = list()
        self.tags = list()

    def fetch_github_available_docker_versions(self):
        self.packages = self.api.packages.get_all_package_versions_for_package_owned_by_org('uaws', 'container',
                                                                                            'dear-gitlab-webservice-ee',
                                                                                            '1', '100')

        for p in self.packages:

            tag = p['metadata']['container']['tags']

            if tag:
                self.tags.append(tag[0])

        return self.tags

    def create_new_branch(self, tag):

        execute_now('git checkout -b v{tag}.m1'.format(tag=tag))

        with FileInput(files=find('Dockerfile', '../../'), inplace=True) as f:
            for line in f:
                line = line.rstrip()
                if 'registry.gitlab.com' in line:
                    line = 'FROM registry.gitlab.com/gitlab-org/build/cng/gitlab-webservice-ee:v{}'.format(tag)
                print(line)

        execute_now(f'git add ../Dockerfile')
        execute_now(f'git commit -m add_{tag}')
        execute_now(f'git remote set-url origin https://$GITHUB_TOKEN@github.com/UAws/dear-gitlab-webservice-ee.git')
        out, err, status = execute_now('git push --set-upstream origin v{tag}.m1'.format(tag=tag))

        if status != 0:
            exit(status)

