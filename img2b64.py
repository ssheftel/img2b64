import sys
import os
import base64
import json

OUTPUT_FILE_NAME = 'base64imgs.json'


class ImageFile(object):
	allowed_extensions = ['png', 'jpg']
	def __init__(self, path):
		self.path = path
		self.base_name = os.path.basename(path)
		self.file_name, file_ext = os.path.splitext(self.base_name)
		self.file_ext = file_ext[1:].lower()
	@property
	def base64(self):
		with open(self.path, "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		return encoded_string
	@classmethod
	def is_image(cls, path):
		is_file = os.path.isfile(path)
		file_ext = os.path.splitext(path)[1][1:]
		is_img_file = is_file and file_ext in cls.allowed_extensions
		return is_img_file


def convert_img_files_to_base64_dict(images):
	"""list of image files to base64 image dict
	:param: images is a list of image file paths
	:return: dict mapping file name to dict with format and base64 keys
	"""
	image_encoding_map = {}
	for image in images:
		image_file = ImageFile(image)
		image_encoding_map[image_file.base_name] = {
			"format": image_file.file_ext,
			"base64": image_file.base64
		}
	return image_encoding_map

def get_images_in_dir(path):
	"""gets a list of images in a directory
	:return: list of (image) file path string
	"""
	path = os.path.abspath(path)
	images_in_dir = []
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if ImageFile.is_image(file_path):
			print(file_path)
			images_in_dir.append(file_path)
	return images_in_dir

def run(location):
	"""runs the main conveter code and returns data dict"""
	images = get_images_in_dir(location)
	return convert_img_files_to_base64_dict(images)


def proscess_args(args):
	"""proscess the cmd line args returns the location of the images
	and the output location
	"""
	cmd_line_args = sys.argv
	cmd_line_args_count = len(cmd_line_args)
	current_directory = os.path.abspath(os.curdir)
	location = current_directory
	if cmd_line_args_count > 1:
		location = os.path.abspath(cmd_line_args[1])
	output_file = os.path.join(location, OUTPUT_FILE_NAME)
	if cmd_line_args_count > 2:
		output_file = cmd_line_args[2]
	return (location, output_file)

def main():
	location, output_file = proscess_args(sys.argv)
	data = run(location)
	with open(output_file, 'w') as f:
		json.dump(data, f, indent=4, separators=(',', ': '))
	print('Done file was save to {}'.format(output_file))

if __name__ == "__main__":
	main()