from nlu_converters.luis_converter import LuisConverter
from nlu_converters.watson_converter import WatsonConverter
from nlu_converters.dialogflow_converter import DialogflowConverter

from nlu_analysers.luis_analyser import LuisAnalyser
from nlu_analysers.watson_analyser import WatsonAnalyser
from nlu_analysers.dialogflow_analyser import DialogflowAnalyser
from nlu_analysers.rasa_analyser import RasaAnalyser



##dialogflow (also works for rasa)
dialogflow_converter = DialogflowConverter()
dialogflow_converter.import_corpus("WebApplicationsCorpus.json")
dialogflow_converter.export("WebApplicationsTraining_Dialogflow.zip")


##dialogflow
#dialogflow_analyser = DialogflowAnalyser("70e660fe4df04d209f159bb9a38b3da9")
#dialogflow_analyser.get_annotations("WebApplicationsCorpus.json", "WebApplicationsAnnotations_Dialogflow.json")
#dialogflow_analyser.analyse_annotations("WebApplicationsAnnotations_Dialogflow.json", "WebApplicationsCorpus.json", "WebApplicationsAnalysis_Dialogflow.json")

##rasa
rasa_analyser = RasaAnalyser("http://localhost:5000/parse")
rasa_analyser.get_annotations("WebApplicationsCorpus.json", "WebApplicationsAnnotations_Rasa.json")
rasa_analyser.analyse_annotations("WebApplicationsAnnotations_Rasa.json", "WebApplicationsCorpus.json", "WebApplicationsAnalysis_Rasa.json")
