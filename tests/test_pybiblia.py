import pybiblia

import json
import os
import pytest

ARR_BIBLE = ['asv', 'kjv', 'leb', 'rsvce', 'ylt']
STR_PASSAGE = 'Ps24.7-8'
STR_SEARCH = 'repent'

@pytest.fixture
def obj_Pybiblia():
  #---------------------------
  # Load environment variables
  str_api_key = os.getenv('BIBLIA_API_KEY')

  #--------------------------------------
  # A JSON file supercedes os environment
  if os.path.exists("config.json"):
    with open("config.json", 'r') as f:
      config = json.load(f)
      if 'BIBLIA_API_KEY' in config:
        str_api_key = config['BIBLIA_API_KEY']

  return pybiblia.Pybiblia(str_api_key)

#--------------------------------------
# Test bible content API for all bibles
def test_content(obj_Pybiblia):
  for str_bible in ARR_BIBLE:
    #--------------------------------------
    # Function content() should return a str
    str_return = obj_Pybiblia.content(str_bible, STR_PASSAGE)
    assert str_return
    assert type(str_return) == str

def test_rsvce(obj_Pybiblia):
  str_return = obj_Pybiblia.rsvce(STR_PASSAGE)
  assert str_return
  assert type(str_return) == str

#-------------------------------------
# Test bible search API for each bible
#   exclude 'rsvce'
def test_search_0(obj_Pybiblia):
  obj_return = obj_Pybiblia.search(ARR_BIBLE[0], STR_SEARCH)
  assert type(obj_return) == dict
def test_search_1(obj_Pybiblia):
  obj_return = obj_Pybiblia.search(ARR_BIBLE[1], STR_SEARCH)
  assert type(obj_return) == dict
def test_search_2(obj_Pybiblia):
  obj_return = obj_Pybiblia.search(ARR_BIBLE[2], STR_SEARCH)
  assert type(obj_return) == dict
def test_search_4(obj_Pybiblia):
  obj_return = obj_Pybiblia.search(ARR_BIBLE[4], STR_SEARCH)
  assert type(obj_return) == dict

#--------------------------------------
# Test bible content API for each bible
#   exclude 'rsvce'
def test_toc_0(obj_Pybiblia):
  obj_return = obj_Pybiblia.toc(ARR_BIBLE[0])
  assert type(obj_return) == dict
def test_toc_1(obj_Pybiblia):
  obj_return = obj_Pybiblia.toc(ARR_BIBLE[1])
  assert type(obj_return) == dict
def test_toc_2(obj_Pybiblia):
  obj_return = obj_Pybiblia.toc(ARR_BIBLE[2])
  assert type(obj_return) == dict
def test_toc_4(obj_Pybiblia):
  obj_return = obj_Pybiblia.toc(ARR_BIBLE[4])
  assert type(obj_return) == dict

#-----------------------------------------
# Test verseoftheday plugin for all bibles
def test_votd(obj_Pybiblia):
  for str_bible in ARR_BIBLE:
    #------------------------------------
    # Function votd() should return a str
    str_return = obj_Pybiblia.votd(str_bible)
    assert str_return
    assert type(str_return) == str
