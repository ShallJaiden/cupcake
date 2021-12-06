from googletrans import Translator
import wikipedia

translator = Translator()


print(translator.translate("我愛你").text)

value = "-pop team epic"
print(value[1:])
search = wikipedia.search(value[1:], results=5)

page = wikipedia.page("Frédéric_Chopin")

print(search)
print(page.url)
