
#!python3
#-*- coding=utf-8 -*-#
#引入requests
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#github的api
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
#用get方法调用，并将响应对象存储在变量r中
r = requests.get(url)
print (type(r))
#打印状态码，200为请求成功
print ("Status code:",r.status_code)
#将返回的信息转为python字典
response_dict = r.json()
#打印字典的键
print(response_dict.keys())
#打印共存在多少项目
print ("total repositories",response_dict['total_count'])
#把字典列表存储在repo_dicts中，并且算出有多少个仓库信息
repo_dicts = response_dict['items']
print ("Repositories returned:",len(repo_dicts))
#把第一个仓库的信息存储到repo_dict中
# repo_dict = repo_dicts[0]

# print (type(repo_dict))

# print ("\nKeys:",len(repo_dict))
#打印这个字典的所有键
# for key in sorted(repo_dict.keys()):
# 	print(key)
#打印仓库的信息，如id,name,owner等
# names,stars = [],[]
names,plot_dicts = [],[]
for repo_dict in repo_dicts:

# 	print("\nwhat u see is what u see")
# 	print("id:",repo_dict['id'])
# 	print("name:",repo_dict['name'])
# 	print("url:",repo_dict['owner']['html_url'])
# 	print("owner:",repo_dict['owner']['login'])
# 	print("description:",repo_dict['description'])
# 	print("forks:",repo_dict['forks'])
# 	print("stargazers_count:",repo_dict['stargazers_count'])
	names.append(repo_dict['name'])
	# stars.append(repo_dict['stargazers_count'])
	plot_dict = {
	       'value': repo_dict['stargazers_count'],
	       'label': str(repo_dict['description']),
	       'xlink': repo_dict['html_url'],
	       }

	plot_dicts.append(plot_dict)

print (plot_dicts)



my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)

# chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'most popular python project on github'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('repos_okc.svg')






















