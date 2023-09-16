from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
import requests
import re
from bs4 import BeautifulSoup

from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

resp = requests.get("https://srd.dndtools.org/srd/magic/spells/spells/")

soup = BeautifulSoup(resp.text, "html.parser")

sources = []

source_map = {
    'divineNewSpells.html': {'name': 'Divine New Spells', 'abbr': 'DNS', 'type': 3},
    'spellsAllCore.html': {'name': 'Players Handbook', 'abbr': 'PHB', 'type': 1},
    'spellsCA.html': {'name': 'Complete Arcane', 'abbr': 'CA', 'type': 1},
    'spellsCAdv.html': {'name': 'Complete Adventurer', 'abbr': 'CAdv', 'type': 1},
    'spellsCC.html': {'name': 'Complete Champion', 'abbr': 'CC', 'type': 3},
    'spellsCDiv.html': {'name': 'Complete Divine', 'abbr': 'CDiv', 'type': 1},
    'spellsCMage.html': {'name': 'Complete Mage', 'abbr': 'CMage', 'type': 1},
    'spellsCScou.html': {'name': 'Complete Scoundrel', 'abbr': 'CScou', 'type': 1},
    'spellsCWar.html': {'name': 'Complete Warrior', 'abbr': 'CWar', 'type': 1},
    'spellsFC1.html': {'name': 'Fiendish Codex I', 'abbr': 'FC1', 'type': 1},
    'spellsFC2.html': {'name': 'Fiendish Codex II', 'abbr': 'FC2', 'type': 1},
    'spellsboed.html': {'name': 'Book of Exalted Deeds', 'abbr': 'BoED', 'type': 1},
    'spellscity.html': {'name': 'Cityscape', 'abbr': 'City', 'type': 1},
    'spellsdotu.html': {'name': 'Drow of the Underdark', 'abbr': 'DoTU', 'type': 3},
    'spellsdrac.html': {'name': 'Draconomicon', 'abbr': 'Drac'},
    'spellsdragonmagic.html': {'name': 'Dragon Magic', 'abbr': 'DraMa'},
    'spellsfrost.html': {'name': 'Frostburn', 'abbr': 'F'},
    'spellshob.html': {'name': 'Heroes of Battle', 'abbr': 'HoB'},
    'spellshoh.html': {'name': 'Heroes of Horror', 'abbr': 'HoH'},
    'spellslm.html': {'name': 'Libris Mortis', 'abbr': 'LM'},
    'spellslom.html': {'name': 'Lords of Madness', 'abbr': 'LoM'},
    'spellsmh.html': {'name': 'Miniatures Handbook', 'abbr': 'MH'},
    'spellsmm4.html': {'name': 'Monster Manual IV', 'abbr': 'MM4'},
    'spellsmm5.html': {'name': 'Monster Manual V', 'abbr': 'MM5'},
    'spellsmoi.html': {'name': 'Magic of Incarnum', 'abbr': 'MoI'},
    'spellsph.html': {'name': 'Planar Handbook', 'abbr': 'PH'},
    'spellsphb2.html': {'name': 'Player\'s Handbook II', 'abbr': 'PHBII'},
    'spellsrod.html': {'name': 'Races of Destiny', 'abbr': 'RoD'},
    'spellsros.html': {'name': 'Races of Stone', 'abbr': 'RoS'},
    'spellsrotd.html': {'name': 'Races of the Dragon', 'abbr': 'RotD'},
    'spellsrotw.html': {'name': 'Races of the Wild', 'abbr': 'RotW'},
    'spellssand.html': {'name': 'Sandstorm', 'abbr': 'SS'},
    'spellsstorm.html': {'name': 'Stormwrack', 'abbr': 'SW'},
    'spellstom.html': {'name': 'Tome of Magic', 'abbr': 'ToM'},
    'spellswol.html': {'name': 'Weapons of Legacy', 'abbr': 'WoL'}
}


def fetch_file(filename: str):
    resp = requests.get(f"https://srd.dndtools.org/srd/magic/spells/spells/{filename}")
    print(process_file(resp.text, filename))


def parse_type1(page_content: str) -> List[str]:
    pass
    # discard everything before this table
    m = re.findall(r'\n<tr width="100%">\n?<td class="line"></td>\n?</tr>\n</table>(?:\n<br/>)?\n?', page_content, re.MULTILINE | re.DOTALL)
    if m:
        s = page_content.rfind(m[-1])+len(m[-1])
        e = page_content.rfind('<br/>')
        interesting_part = page_content[s:e]
        return interesting_part.split('<h6>')
    raise ValueError('The source did not match the type')
    # discard everything after the last <br/>
    # split on <h6>

def parse_type3(page_content: str) -> List[str]:
    pass
    # discard everything before this <h6>
    # discard everything after the last <br/>


def get_or_create_source(source_name, session: Session = Depends(get_db)):
    pass


def process_file(page_content: str, source_name: str, session: Session = Depends(get_db)):
    source = get_or_create_source(source_name)
    for spell in parse_type1(page_content):
        
        session.add()


for row in soup.find('table').find_all('tr'):
    pattern = re.compile(r'<a href="(.*?\.html)">.*?\.html<\/a>')

    link = row.find('a')
    match = re.match(pattern, str(link))
    if match:
        sources.append(match.group(1))

for book in sources:
    fetch_file(book)
#foreach file
#parse file for spells
#for each spell
#write to database