from requests_html import HTMLSession
import json

url = 'https://www.letras.mus.br/barao-vermelho/'

music_links = []
session = HTMLSession()

lyrics = []
def get_lirics(link):
    lyric = {
        "lyric": "",
        "name": ""
    }

    page = session.get(url + link)
    p_elements = page.html.find(".lyric-original", first=True).find("p")

    for idx, p in enumerate(p_elements):
        if idx < len(p_elements):
            lyric['lyric'] += p.text + "\n\n"
        else:
            lyric['lyric'] += p.text

    lyric['name'] = page.html.find(".head-title", first=True).text

    lyrics.append(lyric)


def get_music_links():
    try:
        page = session.get(url)

        for a in page.html.xpath('//*[@id="cnt_top"]/div[5]/div[3]/div/div[1]/div[2]/ol', first=True).find('a'):
            music_links.append(a.attrs['href'].replace("barao-vermelho/", ""))

    except Exception as e:
        print(e)


def get_all_lyrics():
    get_music_links()
    for link in music_links:
        get_lirics(link)

    with open("lyrics12.json", 'a') as file:
        json.dump(fp=file, obj=lyrics, indent=4)
    print("letras armazenadas em 'lyrics.json' com sucesso!")
    review_musics()

def review_musics():
    print("digite 'quit' para finalizar a aplicação e 'list' para ver o nome das músicas armazenadas")
    while True:
        text = input("@: ")
        if text.replace(" ", "") == "quit":
            break
        elif text.replace(" ", "") == "list":
            for lyric in lyrics:
                print(lyric['name'])
        else:
            found_lyric = False
            for lyric in lyrics:
                if lyric['name'].lower() == text.lower():
                    found_lyric = True
                    print("\n" + lyric['lyric'])
            if not found_lyric:
                print("essa música não está catalogada")

get_all_lyrics()
