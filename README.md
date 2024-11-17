## Kom i gang

Følg disse trinnene for å sette opp og bruke `chat`-kommandoen.

### 1. Klon prosjektet

- Klon repo:
```bash
git clone https://github.com/Blackh-t/OPENAI_xfile-0700.git ~/git/blackh-t
```

Lagre OpenAI API nøkkel fra [OpenAI](https://platform.openai.com/) 
```bash
export OPENAI_API_KEY="ditt API her"
```

### 2. Sett opp miljø og kjør programmet
Alternativ 1: Manuell kjøring
Kjør følgende kommandoer i terminalen:
```bash
    cd ~/git/blackh-t/
    python3 -m venv myenv
    source myenv/bin/activate
    pip install openai
    clear
    python3 main.py
```

Alternativ 2: 
Opprett en tilpasset Bash-kommando ved å legge til følgende funksjon i ~/.bashrc:

```bash
chat() {
    cd ~/git/blackh-t/
    python3 -m venv myenv
    source myenv/bin/activate
    pip install openai
    clear
    python3 main.py
}
```

Bruk av chat
Når funksjonen er konfigurert, kan du bruke kommandoen slik i terminal:
```bash
chat
```
Denne kommandoen vil:

- Navigere til prosjektkatalogen.
- Opprette og aktivere et virtuelt miljø hvis nødvendig.
- Installere openai-pakken hvis den mangler.
- Starte Python-programmet main.py.

### DEMO
```bash
Enter a string: la os starte med Nagel


Hva er betydningen av standpunkt eller «points of view» i erfaring og kunnskap ifølge Nagel, og hvordan påvirker det vår forståelse av bevissthet? 

Vurdering: Dette spørsmålet utfordrer din evne til å knytte sammen konsepter i Nagels verk, samt å reflektere over hvordan perspektivet påvirker vår opplevelse av virkeligheten. Vil du utdype svaret ditt?


Input: The point of view gir oss en perspektiv på at vi ikke kan forstår andre art fullstendig, selv om vi vet mye om andres art sensor. dette gir også en forståelse om andre mennesker hvor vi ikke kan alltid vite hvordan andre mennesker observere det samme hendelse


Bra analysert! Du har identifisert en viktig komponent i Nagels argumentasjon, nemlig at det er en begrensning i vår evne til å forstå andres erfaringer fullt ut, selv om vi har kunnskap om deres biologiske og fysiske betingelser. Dette peker på kompleksiteten i bevissthet og hvordan individuelle perspektiver former vår opplevelse av virkeligheten. 

Kan du utdype videre hvordan denne innsikten kan påvirke vår forståelse av etikk eller moral? Dette kan være en god måte å knytte Nagels ideer til praktiske spørsmål vi står overfor i hverdagen.


Input:
```
