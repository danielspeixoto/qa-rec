from src.main.data.elasticsearch.AnalysisIndex import AnalysisIndex
from src.main.data.elasticsearch.Config import Config
from src.main.data.elasticsearch.QuestionIndex import QuestionIndex
from src.main.data.pickle.PickleRepository import PickleRepository
from src.main.domain.Test import Test

# repo = PickleRepository("/home/daniel/ufba/rec/")
config = Config("localhost", "9200")
repo = AnalysisIndex(config, 'recsys')
index = QuestionIndex(config)
test = Test(index, repo)

test.test()
