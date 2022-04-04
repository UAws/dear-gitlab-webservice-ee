# Dear Gitlab Webservice EE

Magic modification of Gitlab Webservices EE (partial and core component of Gitlab Helm Chart), explore all ultimate features on Gitlab EE

## Get Started

In the deployment response file `values.yaml`, specific following conditions which `ghcr.io/uaws/dear-gitlab-webservice-ee` is the container registry  contains pre-built images, and `tag` must be identical to your global gitlab charts version, only `webservice` subset container needs to be modified and rest of services should directly pull from gitlab CNG unless you know how to customize:

```yaml
gitlab:
  webservice:
    image:
      repository: ghcr.io/uaws/dear-gitlab-webservice-ee
      tag: v14.9.2.m1
```

Reference doc : 
1. https://docs.gitlab.com/charts/charts/gitlab/webservice/index.html#imagepullsecrets
2. https://helm.sh/docs/chart_template_guide/values_files/

## Version mapping of Chart version to GitLab build version 

https://docs.gitlab.com/charts/installation/version_mappings.html


## Check out Latest build action 

https://github.com/UAws/dear-gitlab-webservice-ee/actions/workflows/build.yaml

## Pull the pre-build image by tag

https://github.com/UAws/dear-gitlab-webservice-ee/pkgs/container/dear-gitlab-webservice-ee


## Licensed under MIT

```
Copyright 2022 UAWS/AkideLiu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
