#!/usr/bin/python

import re
import requests
import argparse
from lxml import etree

START='start'
END='end'
EVENTS=(START, END)

def inspect_xml(xml_resource):
  xml = get_xml(xml_resource)

  tree = ''
  indent = ''
  feed = etree.fromstring(xml)
  for action,elem in etree.iterwalk(feed, events=EVENTS):
    if action == START:
      indent += '  '
      attrs = elem.keys()
      tree += '%s%s: %s :: %s\n'%(indent, elem.tag, ', '.join(attrs if attrs else ['None']), elem.text[:100].replace('\n', '') if elem.text else '')
    else:
      indent = indent[0:-2]

  return tree.encode('ascii', 'ignore') # TODO handle encoding more beter-er-est.

def get_from_url(url):
  response = None
  try:
    response = requests.get(url)
  except requests.exceptions.ConnectionError as e:
    print 'Got %s status while fetching URL: %s'%(response.status_code if response else '<timeout>', url)
    return None
  except requests.exceptions.MissingSchema as e:
    print 'how did you even HIT this????'
    return None

  return response.content

def get_from_file(file_name):
  text = None
  try:
    file_obj = open(file_name, 'r')
    text = file_obj.read()
    file_obj.close() # all the errors get thrown at open(), so putting this in 'finally:' is pointless.
  except IOError as e:
    print 'Yeaaah. Couldn\'t open that file.'

  return text

def get_xml(resource):
  is_url = re.match('https?\:\/\/', resource, re.I) # if this lib ever becomes more than a run-once utillity, then this regex should get compiled first.
  if is_url:
    return get_from_url(resource)
  return get_from_file(resource)


parser = argparse.ArgumentParser()
parser.add_argument('xml_resource', type=str, help='File name or URL of the XML doc. URLs must start with "http" or "https"')
args = parser.parse_args()

print inspect_xml(args.xml_resource)
