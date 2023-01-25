import nltk
import cherrypy
from HanTa import HanoverTagger as ht

nltk.download("punkt")

def convert_tag_to_obj(tag_array):
  if (len(tag_array) != 3): return {} 

  return {
    "original": tag_array[0],
    "normalized": tag_array[1],
    "word_class": tag_array[2]
  }

class NLPWordTagger:
  def __init__(self, lang="en"):
    hanta_model = "morphmodel_ger.pgz" if lang == "ger" else "morphmodel_en.pgz"
    self.tagger = ht.HanoverTagger(hanta_model)

  def tag_words_from_string(self, string):
    words = nltk.word_tokenize(string)
    tags = self.tagger.tag_sent(words)
    mapped_tags = list(map(convert_tag_to_obj, tags))
    return mapped_tags

class NLPWordTaggerServer(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def tag_words(self, lang="en"):
        data = str(cherrypy.request.body.read(), "utf-8")
        tagger = NLPWordTagger(lang)
        words = tagger.tag_words_from_string(data)
        return words

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8080,
                       })
cherrypy.quickstart(NLPWordTaggerServer())