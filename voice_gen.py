from gradio_client import Client, file

import shutil
import os
import time 


def generate(text, client):
	result = client.predict(
			text,	# str in 'Input Prompt' Textbox component
			"\n",	# str in 'Line Delimiter' Textbox component
			"None",	# Literal['Happy', 'Sad', 'Angry', 'Disgusted', 'Arrogant', 'Custom', 'None'] in 'Emotion' Radio component
			"",	# str in 'Custom Emotion' Textbox component
			"male1",	# Literal['beerus', 'daniel', 'eliah', 'geto', 'girl', 'gojo', 'gojo2', 'goku', 'gt', 'harvey', 'leo', 'male1', 'me', 'michal', 'sukuna', 'tom', 'trump', 'will', 'random', 'microphone'] in 'Voice' Dropdown component
			file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),	# filepath in 'Microphone Source' Audio component
			0,	# float in 'Voice Chunks' Number component
			1,	# float (numeric value between 1 and 6)
				#					in 'Candidates' Slider component
			0,	# float in 'Seed' Number component
			256,	# float (numeric value between 2 and 512)
				#					in 'Samples' Slider component
			200,	# float (numeric value between 0 and 512)
				#					in 'Iterations' Slider component
			0.8,	# float (numeric value between 0 and 1)
				#					in 'Temperature' Slider component
			"DDIM",	# Literal['P', 'DDIM'] in 'Diffusion Samplers' Radio component
			8,	# float (numeric value between 1 and 32)
					#				in 'Pause Size' Slider component
			0,	# float (numeric value between 0 and 1)
					#				in 'CVVP Weight' Slider component
			0.8,	# float (numeric value between 0 and 1)
					#				in 'Top P' Slider component
			1,	# float (numeric value between 0 and 1)
					#				in 'Diffusion Temperature' Slider component
			1,	# float (numeric value between 0 and 8)
					#				in 'Length Penalty' Slider component
			2,	# float (numeric value between 0 and 8)
					#				in 'Repetition Penalty' Slider component
			2,	# float (numeric value between 0 and 4)
					#				in 'Conditioning-Free K' Slider component
			[],	# List[Literal['Half Precision', 'Conditioning-Free']] in 'Experimental Flags' Checkboxgroup component
			False,	# bool in 'Use Original Latents Method (AR)' Checkbox component
			False,	# bool in 'Use Original Latents Method (Diffusion)' Checkbox component
			api_name="/generate"
	)
	return result[0]

def save_file(src_file, dest_path):
	shutil.copy(src_file, dest_path)


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def voice_main():
    client = Client("http://127.0.0.1:7860/")
    f = open('voice.txt')
    text_input = f.read().replace('\n',' ')
    folder_path = "./audio"
    create_folder_if_not_exists(folder_path)
    print("*"*25+"STARTING"+"*"*25)
    sentence = text_input
    result = generate(sentence.strip(), client)
    save_file(result,folder_path + f"/audio.wav")
