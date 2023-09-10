import mypackage.module2 as md2

text = "Hello world"
dest = 'uk'
lang = 'en'

print(md2.TransLate(text=text, dest=dest))
print(md2.LangDetect(text=text, set='all'))
print(md2.CodeLang(lang=lang))
md2.LanguageList(out='screen', text=text)
