from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1442814217:AAEovdATuh5zbjNfeWisXQ-3jD28IKhvrK4"
	APP_ID = 2865840
	API_HASH = "610823c1999519c8261b215dbb372eee"
	OWNER_ID = "126110134"
	AUTH_CHANNEL = [-1001470368690]
	DESTINATION_FOLDER = "HK ROBOT" #Name of your folder read readme
	RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0AfH6SMAJA9D504m5oQrShJzrnATfrWS--2qa7_Ia2cV6Lwo4VqNbO2XhAsHkE3TlnoxzsQQ1bT3TgOlA8ysG0LRgcbl1FXz3jwnJuW6ZYNC5bmIq5dODFLlipo7PMnAYmNuHDk4Z-x1KPtwI5cRSNnftrpLqG4bG0qbCrdTciYA","token_type":"Bearer","refresh_token":"1//0gQ7W5XLBdHI6CgYIARAAGBASNwF-L9IrZCQ5l0xZA9KkqD-9CTZFeR65IWR-SrbXCmxVi-CnNrK8dC4kn7AxaG2r1KeBYwmoVeI","expiry":"2020-12-21T15:19:36.015520994Z"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
