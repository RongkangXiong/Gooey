from gooey import Gooey, GooeyParser

@Gooey(
  #菜单设置
  menu = [
  {
    'name': 'File',
    'items': 
    [
    ]
  },
  {
    'name': 'Tools',
    'items': []
  },
  {
    'name': 'Help',
    'items': 
    [
      
      {
        'type': 'Link',
        'menuTitle': 'Documentation',
        'url': 'https://cneuroustc.github.io'
      },
      {
        'type': 'AboutDialog',
        'menuTitle': 'About',
        'name': 'JC Update',
        'description': 'WenLab\'s JC Update Mini Program',
        'version': '0.1.1',
        'copyright': '2021',
        'website': 'https://cneuroustc.github.io/',
        'developer': 'https://github.com/CNeuroUSTC',
        'license': 'USTC WenLab'
      },
      {
        'type': 'Link',
        'menuTitle': 'Visit Our Site',
        'url': 'https://cneuroustc.github.io'
      }
    ],
  }
  ],

  ichtext_controls=True,                 # 打开终端对颜色支持
  program_name="JC Update Mini Program",        # 程序名称
  encoding="utf-8",                       # 设置编码格式，打包的时候遇到问题
  progress_regex=r"^progress: (\d+)%$"    # 正则，用于模式化运行时进度信息

)
def main():
  parser = GooeyParser(description="Update JC Information!") 
  #parser.add_argument('a','b',widget="Listbox")

  presenter = parser.add_argument('Presenter',widget='TextField')  #Presenter
  date = parser.add_argument('Date', widget='DateChooser')  # Date
  paper = parser.add_argument('Paper', widget='TextField')
  #parser.add_argument('JC',widget='RadioGroup')
  #parser.add_argument('Filename', widget="FileChooser")
  print(presenter)
  
  
  args=parser.parse_args()
  print(args)
  


if __name__ == '__main__':
   main()
   
