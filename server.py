import nltk
import cherrypy
import os
from HanTa import HanoverTagger as ht

nltk.download("punkt", "/app-nltk/")
nltk.download("punkt_tab", "/app-nltk/")

def convert_tag_to_obj(tag_array):
  if (len(tag_array) != 3): return {} 

  return {
    "original": tag_array[0],
    "normalized": tag_array[1],
    "wordClass": tag_array[2]
  }

class NLPWordTagger:
  def __init__(self, lang="en"):
    hanta_model = "morphmodel_ger.pgz" if lang == "de" else "morphmodel_en.pgz"
    self.tagger = ht.HanoverTagger(hanta_model)

  def tag_words_from_string(self, string):
    words = nltk.word_tokenize(string)
    tags = self.tagger.tag_sent(words)
    mapped_tags = list(map(convert_tag_to_obj, tags))
    return mapped_tags

class NLPWordTaggerServer(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def tagged_words(self, lang="en"):
        data = str(cherrypy.request.body.read(), "utf-8")
        tagger = NLPWordTagger(lang)
        words = tagger.tag_words_from_string(data)
        return words

userpassdict = {os.environ.get('BASIC_AUTH_USER_NAME') or 'admin': os.environ.get('BASIC_AUTH_USER_PASSWORD') or 'admin'}

conf = {
   '/': {
       'tools.auth_basic.on': os.environ.get('BASIC_AUTH_ENABLED') or True,
       'tools.auth_basic.realm': os.environ.get('SERVER_HOST') or '0.0.0.0',
       'tools.auth_basic.checkpassword': cherrypy.lib.auth_basic.checkpassword_dict(userpassdict),
       'tools.auth_digest.get_ha1': cherrypy.lib.auth_digest.get_ha1_dict_plain(userpassdict),
       'tools.auth_basic.accept_charset': 'UTF-8',
    },
    'global': {
      'server.socket_host': os.environ.get('SERVER_HOST') or '0.0.0.0',
      'server.socket_port': int(os.environ.get('SERVER_PORT')) if os.environ.get('SERVER_PORT') else 8080
    }
}
cherrypy.quickstart(NLPWordTaggerServer(), '/', config=conf)
