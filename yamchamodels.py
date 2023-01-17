import puar.hetare
import puar.kamaseinu
import http.client, urllib.request, urllib.parse, urllib.error, base64
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

endpoint = 'https://animals110-prediction.cognitiveservices.azure.com/'
projectID = 'cf5c50ed-d80e-4261-84cf-3f326efe68d4'
publish_iteration_name = 'Iteration1'
prediction_key = '1b662036cc1b423e8b155780d557009b'
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint, prediction_credentials)


# 予測確率のしきい値（パーセント）
threshold = 10

# モデルAPIの呼び出し
def callAPI(uploadFile):
	# 予測用インスタンスの作成
	#predictor = CustomVisionPredictionClient(prediction_key, endpoint=base_url)
	
	with open(uploadFile, mode='rb') as f:
		# 予測実行
		results = predictor.classify_image(projectID, publish_iteration_name, f.read())
    
	result = []

	for prediction in results.predictions:
		if len(get_yamcha_data(prediction.tag_name)) != 0:
			# 確率がしきい値より大きいものを採用する
			if prediction.probability * 100 > threshold:
				result.append(get_yamcha_data(prediction.tag_name))

	return result

# 魚情報をDBから取得し辞書型で返す
def get_yamcha_data(yamchaname):
	ses = puar.hetare.db_session()
	yamcha_master = puar.kamaseinu.YamchaMaster
	yamcha_data = ses.query(yamcha_master).filter(yamcha_master.yamcha_name == yamchaname).first()

	yamcha_data_dict = {}
    
	if not yamcha_data is None:
		yamcha_data_dict['yamcha_name'] = yamcha_data.yamcha_name
		yamcha_data_dict['picture_path']    = yamcha_data.picture_path

		'''if yamcha_data.poison == 1:
			yamcha_data_dict['poison'] = '毒あり'
		else:
			yamcha_data_dict['poison'] = ''
		yamcha_data_dict['poison_part']     = yamcha_data.poison_part
		yamcha_data_dict['wiki_url']        = yamcha_data.wiki_url
		yamcha_data_dict['picture_path']    = yamcha_data.picture_path
		yamcha_data_dict['copyright_owner'] = yamcha_data.copyright_owner
		yamcha_data_dict['copyright_url']   = yamcha_data.copyright_url
'''
	return yamcha_data_dict