
This is a minimal reimplementation of [certifi](https://pypi.org/project/certifi/), 
hardcoded to use the RHEL/CentOS/Fedora system certificate store.

It was built for use in AWX and similar projects where using an OS-provided
certifi is not possible when constructing virtual environments.

Contributing
------------

- All code submissions are done through pull requests against the `devel` branch.
- All contributors must use git commit --signoff for any commit to be merged, and agree that usage of --signoff constitutes agreement with the terms of [DCO 1.1](./DCO_1_1.md)
- Take care to make sure no merge commits are in the submission, and use `git rebase` vs `git merge` for this reason.

Code of Conduct
---------------

We ask all of our community members and contributors to adhere to the [Ansible code of conduct](http://docs.ansible.com/ansible/latest/community/code_of_conduct.html). If you have questions, or need assistance, please reach out to our community team at [codeofconduct@ansible.com](mailto:codeofconduct@ansible.com)   

License
-------

[Mozilla Public License v2.0](./LICENSE)
