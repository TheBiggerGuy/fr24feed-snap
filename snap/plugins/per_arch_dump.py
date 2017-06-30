#!/bin/usr/env python3

import logging

import snapcraft

ARCHITECTURE = ['i386', 'amd64', 'armhf']

logger = logging.getLogger(__name__)

class PerArchDump(snapcraft.BasePlugin):
  @classmethod
  def schema(cls):
    print('schema')
    logger.warn('schema')
    schema = super().schema()

    for arch in ARCHITECTURE:
      schema['properties'][arch] = {
        'type': 'string'
      }
    schema.pop('required')
    schema.pop('pull-properties')
    schema.pop('build-properties')

    return schema

  @classmethod
  def get_pull_properties(cls):
    return ARCHITECTURE

  def __init__(self, name, options, project):
    print('init')
    options.source = getattr(options, project.deb_arch)
    super(PerArchDump, self).__init__(name, options, project)

  def pull(self):
    print('pull')
    snapcraft.get()
    super().pull()

  def build(self):
    print('build')
    snapcraft.file_utils.link_or_copy_tree(self.builddir, self.installdir)
